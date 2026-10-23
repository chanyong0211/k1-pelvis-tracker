# k1-pelvis-tracker

K1 골반 명령 추종 하체 정책(dev12)을 한 페이지로 정리한 곳.

- [index.html](https://chanyong0211.github.io/k1-pelvis-tracker/) — 개요, 그림 1(실기 경로·학습 구성), 목차 7절: 명령 공간, 정책 구조, 보상·판정, 자연스러운 걸음(대표 영상 `media/`), 학습 환경, 검증·스모크, 진행·결정. 2026-10-23 옛 페이지(학습 환경 계획·설계·걸음 모음·DreamWaQ 해설·판 2 계획)를 이 한 페이지로 합쳤다.
- `dev12_design.json` — 설계 데이터(판 31), `dev12_env_plan.json` — 학습 환경 계획 데이터. 페이지에서 고치는 도구는 없앴다(JSON 을 직접 고친다).

## 로컬에서 보기

```
git pull
python3 docs_server.py        # http://<이 PC 주소>:8099/
```
