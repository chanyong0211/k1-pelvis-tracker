#!/usr/bin/env python3
"""이 폴더를 LAN 에 띄우고, 설계 페이지(index.html)의 저장 요청을 받아 dev12_design.json 에 쓴다.

실행: python3 docs_server.py [--port 8099] 후 브라우저로 http://<이 PC 주소>:8099/
저장할 때마다 이전 판을 design_backups/ 에 남기고, 옛 판 위에서 고친 저장은 거절한다(409).
"""
import argparse
import json
import shutil
import time
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
DESIGN = HERE / "dev12_design.json"
BACKUPS = HERE / "design_backups"
MAX_BYTES = 2 * 1024 * 1024


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _send(self, code, body, ctype="text/plain; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.split("?")[0] == "/__design_api/ping":
            return self._send(200, b"ok")
        return super().do_GET()

    def do_POST(self):
        if self.path.split("?")[0] != "/__design_api/save":
            return self._send(404, b"not found")
        n = int(self.headers.get("Content-Length", 0))
        if n <= 0 or n > MAX_BYTES:
            return self._send(413, b"size")
        try:
            state = json.loads(self.rfile.read(n).decode("utf-8"))
            base = int(self.headers.get("X-Base-Rev", "-1"))
        except ValueError:
            return self._send(400, b"bad json")
        if not isinstance(state, dict) or not {"meta", "groups", "items", "tables"} <= set(state):
            return self._send(400, b"not a design")
        cur = json.loads(DESIGN.read_text(encoding="utf-8"))["meta"]["rev"]
        if base != cur:
            return self._send(409, f"saved revision is {cur}, page was {base}".encode())
        if state["meta"].get("rev") != cur + 1:
            return self._send(400, b"rev must be base + 1")
        BACKUPS.mkdir(exist_ok=True)
        shutil.copy2(DESIGN, BACKUPS / f"dev12_design.rev{cur}.{time.strftime('%Y%m%d_%H%M%S')}.json")
        tmp = DESIGN.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        tmp.replace(DESIGN)
        self._send(200, json.dumps({"rev": cur + 1}).encode(), "application/json")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8099)
    ap.add_argument("--host", default="0.0.0.0")
    a = ap.parse_args()
    print(f"serving {HERE} on http://{a.host}:{a.port}/", flush=True)
    ThreadingHTTPServer((a.host, a.port), partial(Handler, directory=str(HERE))).serve_forever()
