# Project Documentation

## 개인 branch 생성 및 사용 방법

1. 새로운 branch 생성 후 해당 브랜치로 이동

```bash
git checkout -b [branch_name]
```

2. 작업 후 commit

```bash
git add .
git commit -m "[commit_message]"
```

3. 처음에 자신의 branch에 push: upstream을 설정함

```bash
git push -u origin [branch_name]
```

4. 이후에 자신에 branch에 push

```bash
git push origin [branch_name]
```

## Github 사용 규칙

- 자신의 코드의 버전관리를 위해서 본인의 branch에 본인이 작업한 내용을 `git push origin [branch_name]`로 push합니다.

- 주기적으로 자신의 branch와 main 브랜치를 병합합니다. main branch는 다른 조원의 작업으로 계속해서 바뀌기 때문에 병합으로 충돌을 최소화합니다. 충돌이 발생했을 때는 기본적으로 main branch의 내용을 따르고, 본인의 branch를 main branch에 병합을 해야한다고 생각될 경우에는 저에게 말해주세요. 바로 병합을 진행하도록 하겠습니다.

- 자신의 branch에만 병합하도록 합니다. 어차피 저 이외에 main branch 권한은 부여하지 않았지만, 특정 작업이 끝나면 repository에서 pull request를 통해 main branch에 병합을 요청합니다.

- `[본인의 이름].md` 파일을 만들어서 본인이 만들거나 수정한 코드에 대해서 기본적인 설명을 적어주세요. 다른 팀원들이 본인의 코드를 이해할 수 있도록 하면 좋을 것 같아요.

- 저도 협업이 처음이라서 기본적인 규칙만 정해봤는데, 추가적인 제안 사항이 있다면 말해주세요.