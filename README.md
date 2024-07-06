# RepoScanner

RepoScanner는 주어진 디렉토리의 파일과 디렉토리 구조를 스캔하고, 프로젝트 개요 및 상세 정보를 수집하는 Python 스크립트입니다. 이 스크립트는 `.gitignore` 파일과 추가 무시 패턴을 참조하여 특정 파일 및 디렉토리를 제외할 수 있습니다.

repo의 구조와 내용을 LLM에게 쉽게 파악시키기 위한 목적으로 만들었습니다.

## 기능

- 디렉토리 구조를 스캔하고, 파일 및 디렉토리 목록을 생성
- `.gitignore` 파일과 사용자 정의 무시 패턴을 사용하여 특정 파일 및 디렉토리 제외
- 프로젝트 개요와 상세 정보를 별도의 파일에 저장
- 처리 로그를 작성하여 어떤 파일이 포함되었고, 어떤 파일이 제외되었는지 기록

## 설치

1. 이 레포지토리를 클론합니다:

    ```sh
    git clone https://github.com/kubony/reposcanner.git
    cd reposcanner
    ```

2. Python 3.x가 설치되어 있는지 확인합니다.

## 사용법

1. `collect_project_files.py` 파일을 실행합니다:

    ```sh
    python collect_project_files.py
    ```

2. 스크립트가 실행된 디렉토리의 루트에서 `project_info` 폴더가 생성되고, 다음과 같은 파일들이 생성됩니다:
    - `overview_project.txt`: 디렉토리 구조 개요
    - `detailed_project_info.txt`: 각 파일의 내용 상세 정보
    - `project_log.txt`: 처리 로그

### 추가 무시 패턴

`additional_ignore.txt` 파일을 생성하여 추가적인 무시 패턴을 정의할 수 있습니다. 이 파일은 프로젝트 루트에 위치해야 하며, 각 패턴은 새로운 줄에 작성됩니다.

예시:

```
### 무시할 디렉토리
node_modules/
dist/
.build/

### 무시할 파일
*.log
*.tmp
```

## 예제

프로젝트 구조 예제:

```
reposcanner/
├── collect_project_files.py
└── project_info/
    ├── additional_ignore.txt
    ├── overview_project.txt
    ├── detailed_project_info.txt
    └── project_log.txt
```

## 기여

기여를 환영합니다! 버그를 보고하거나 기능 요청을 남기려면 [Issues](https://github.com/kubony/reposcanner/issues) 페이지를 방문하세요.

1. 이 레포지토리를 포크합니다.
2. 새로운 브랜치를 만듭니다 (`git checkout -b feature/your-feature`).
3. 변경 사항을 커밋합니다 (`git commit -am 'Add some feature'`).
4. 브랜치에 푸시합니다 (`git push origin feature/your-feature`).
5. 풀 리퀘스트를 생성합니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.

## 문의

질문이나 도움이 필요하면 레포지토리 소유자에게 문의하십시오.

- 이메일: [your-email@example.com](mailto:your-email@example.com)
- GitHub: [kubony](https://github.com/kubony)
