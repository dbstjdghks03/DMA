# 데이터 관리와 분석 2023-2학기

### 팀원

김건형, 박석우, 송형석, 윤성환, 이준성

### 사용 스펙

python version 3.9.12

### 버전 테스트

```shell
version_test.py 실행
True가 나오면 3.9.12 버전이 정상적으로 실행중이다.
```

<!-- ### pre-commit 세팅

터미널 실행 후 DMA git 폴더에서 아래 명령어 실행

```shell
pip install husky
husky install

#윈도우
husky add .husky/pre-commit "yarn lint-staged --no-stash --verbose && yarn build"
#그 외
husky add .husky/pre-commit "lint-staged --no-stash --verbose && yarn build"
``` -->

### 커밋 메세지 컨벤션

- 커밋은 최대한 잘게잘게 쪼개서

- 메시지 형식: `[커밋 유형] : 작업내용을 한글로 한줄설명`

  `ex) COMMENT : 함수 인자 설명 주석 추가`

- 이때 [커밋 유형]:
  - FEAT: 새로운 기능이나 파트를 작업한 경우
  - FIX: 오류를 수정한 경우
  - REFACTOR: 코드 리팩토링
  - COMMENT: 주석만 단 경우
  - REMOVE: 파일 삭제한 경우
