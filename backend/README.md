# backend

## Directory Tree
```
backend/
│
├── main.py             # FastAPI 애플리케이션의 진입점(라우터를 실행하고 애플리케이션을 실행함)
├── database.py         # DataBase 연결을 설정(PostgreSql 사용한다고 가정함)
├── models.py           # DataBase의 모델들을 정의함
├── routers/            # 라우터 모음
│   └── items.py        # 아이템과 관련된 API엔드포인트 정의
└── requirements.txt    # 필요 라이브러리
```

## Project setup
1. Install Library
```
pip install -r requirements.txt
```
2. Setup DB Id and pw
- `.env` 파일을 만들고 안에 아래와 같은 내용 입력하기.
    - DATABASE_URL=postgresql://`사용자 이름`:`비밀번호`@localhost/`사용할 DataBase 이름`
    - 예를 들어, 사용자 이름이 gm
    - 비밀번호가 1234
    - 사용할 DB 이름이 test_db이면
    - DATABASE_URL=postgresql://gm:1234@localhost/test_db
### Compiles and hot-reloads for development
```
uvicorn main:app --reload
```