# 데이터 관리와 분석 2023-2학기

### 팀원

김건형, 박석우, 송형석, 윤성환, 이준성

### 사용 스펙

python version 3.9.12

### 버전 테스트 <중요!!! git clone 이후에 반드시 진행할 것>

```shell
version_test.py 실행
 => True가 나오면 3.9.12 버전이 정상적으로 설정된 것
```

### pre-commit 세팅 <중요!!! git clone 이후에 반드시 진행할 것>

pre-commit 세팅은
commit을 하기 전 commit할 내용이 '설정된 코드 규정'을 잘 따르고 있는지를 자동으로 확인, 수정하게 해주는 세팅이다.
('설정된 코드 규정'은 `.pre-commit-config.yaml`에 작성해두었음. __수정X요함__)

변경 내용이 설정된 코드 규정에 어긋나는 경우 commit을 방지해주며, 어긋난 부분을 고쳐준다.

> 따라서 commit을 시도했는데 설정해둔 pre-commit에 의해 commit이 되지 않은 경우, pre-commit이 고쳐준 내용까지 git add를 하여 다시 한번 commit해주면 된다.

> pre-commit 세팅 방법은 다음과 같음.

터미널 실행 후 DMA git 폴더에서 아래 명령어 실행

```shell
pip install pre-commit
# 설치가 완료되면 터미널을 껐다가 재실행한 후 아래 내용을 이어서 진행
pre-commit install
# >>> pre-commit installed at .git/hooks/pre-commit 문구가 뜨면 성공적으로 설치된 것

pre-commit run # 성공적으로 세팅되었는지 확인
```
마지막 run 시에 아래와 같이 결과가 나오면 성공적으로 세팅된 것이다.
```
black................................................(no files to check)Skipped
flake8...............................................(no files to check)Skipped
isort................................................(no files to check)Skipped
pyright..............................................(no files to check)Skipped
```

### 커밋 메세지 형식 규칙

- 서로 간 작업 확인이 용이하도록 commit 메세지를 아래와 같은 형식을 지켜서 하자.

- 커밋은 최대한 잘게잘게 쪼개서

- 메시지 형식: `[커밋 유형] : 작업내용을 한글로 한줄설명`

  `ex) COMMENT : 함수 인자 설명 주석 추가`

- 이때 [커밋 유형]:
  - FEAT: 새로운 기능이나 파트를 작업한 경우
  - FIX: 오류를 수정한 경우
  - REFACTOR: 코드 리팩토링
  - COMMENT: 주석만 단 경우
  - REMOVE: 파일 삭제한 경우


### 작업 방법
작업은 다음과 같은 순서로 진행하자.

1. 메인 브랜치로 이동
2. git pull (github에 저장된 main 브랜치의 내용을 컴퓨터로 가져온다.)
3. 작업할 브랜치 생성. 
  
    브랜치명의 경우 hyungsuk-1, hyungsuk-2와 같이 자기 이름에 숫자 붙여서.
4. 작업. 작업은 아래 4-1~4-2의 반복으로, 즉 일정부분 작업하고 커밋, 또 일정부분 작업하고 커밋, 일정부분 작업하고 커밋. 될 수 있으면 모든 내용을 한번에 작업하고 커밋하는 게 아니라 이렇게 잘게잘게 쪼개서 한다.

    4-1. 작업한 내용 중 commit 올릴 내용 git add (내가 작업한 내용 중에서 commit할 내용들을 고르는 것임. commit한다는 것은 내 컴퓨터에 변경 내용을 세이브해두는 거라고 생각하면 편함)

    4-2.  git commit 이때 메시지 형식 규칙을 지켜서.

5. git push (commit해둔 내용들을 github로 보내버린다.)
6. github 접속 후 pull request를 올린다. (pull request란, main 브랜치에다가 너의 branch를 병합해달라고 올려두는 것. pull request를 올려두면 다같이 이거를 main에다가 병합해도 되는지 안되는지 딱딱 확인해본 후 병합한다. 병합한다는 것은 너의 브랜치의 변경 내용을, 메인 브랜치에도 반영한다는 것임)

    pull request 올리는 방법은 [링크](https://www.youtube.com/watch?v=Ru9qv-tHj7I) 를 참고