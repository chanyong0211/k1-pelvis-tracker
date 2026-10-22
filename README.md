# k1-pelvis-tracker

K1 하체 정책 설계 페이지 (dev12).

- [index.html](https://chanyong0211.github.io/k1-pelvis-tracker/) — 첫 페이지 = 학습 환경 계획(2026-10-21 계획서): 단계·관문, 학습 흐름, 결정, 과제 14개와 테스트, 결과. 아래에 "학습 설계"·"궤적 최적화"로 넘어가는 제목이 있다. 데이터는 `dev12_env_plan.json`, 설계 항목은 `dev12_design.json` 에서 읽어 설계 페이지 행으로 연결한다(읽기 전용).
  - [design.html](https://chanyong0211.github.io/k1-pelvis-tracker/design.html) — 학습 설계: dev12 골반 명령 추종 보행 정책 설계. 데이터는 `dev12_design.json`. GitHub Pages 에서는 읽기 전용이다(고친 내용은 "JSON 내보내기").
  - [gait_library.html](https://chanyong0211.github.io/k1-pelvis-tracker/gait_library.html) — 궤적 최적화: 걸음 모음 첫 판(아래 설명).
- [v2_sonic.html](https://chanyong0211.github.io/k1-pelvis-tracker/v2_sonic.html) — 2026-10-13 계획(판 2, 동결 SONIC + 걸음 생성기 안). 이 페이지의 저장 버튼은 v2_sonic.html 자신에 쓴다.
- [dreamwaq.html](https://chanyong0211.github.io/k1-pelvis-tracker/dreamwaq.html) — DreamWaQ 해설: 논문 전체, 인코더(CENet)가 배우는 방식, dev2 코드에서 잠재가 죽어 있던 원인, dev12 인코더 결정(설계 판 16).
- [gait_library.html](https://chanyong0211.github.io/k1-pelvis-tracker/gait_library.html) — 궤적최적화 걸음 모음(2026-10-21): 높이 0.46–0.74 m · 숙임 0–45° × 앞·뒤·옆·제자리 회전·걸으며 돌기 422칸, 421칸 통과, dev12 AMP 참조용. 영상은 `gait_library_media/`(960 px 축소본).

## 설계 고치기

```
git clone https://github.com/chanyong0211/k1-pelvis-tracker
cd k1-pelvis-tracker
git pull
python3 docs_server.py        # http://localhost:8099/design.html 에서 고치고 저장
git commit -am "설계 판 N"
git push
```

- 고치기 전에 꼭 `git pull`. 두 곳에서 동시에 고치면 나중 push 가 거절되고 JSON 충돌을 손으로 풀어야 한다.
- 저장할 때마다 이전 판이 `design_backups/` 에 남는다(git 에는 안 올라감).
