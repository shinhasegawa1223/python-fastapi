## database.py

データベースへの接続セッション管理<br>
sqlalchemy create_engine でセッション作成<br>
sqlalchemy declarative_base を使用して基盤クラスを作成 Base<br>

## models.py

DB 内にできあるテーブルをクラスとして作成<br>
その際 Base クラスを継承<br>

## schemas.py

Pydantic スキーマを定義する pydantic baseModel を継承<br>
リクエストの際のバリデーションに使用する<br>

## crud.py

crud 処理を記載
各関数の引数には、DB セッションを含むこと<br>
各関数には、バリデーションを用いる schemas.py で定義<br>
各関数で models.py で使用下 class を用いる<br>

## main.py

ルーティング設定、サーバーの起動を記載<br>
セッションの作成（database.py から取得<br>
crud.py へ処理をつなげる　関数や関数の戻り値返却<br>
各関数の戻り値に対してバリデーションを行う schemas.py で定義したやつ

### サーバーの立ち上げ方

docker

fastapi-study

```bash
docker compose up -d
```

DB クライアントツール

> localhost:81

uvicorn sql_app.main:app --host=0.0.0.0 --port=8686 --reload

swagger

> /docs で開ける
> localhost:8686/docs

```bash
[ pip or conda ] install sql alchemy
[ pip or conda ] install alembic psycopg2-binary


```

postgresql のアダプター
psycopg2

```bash
alembic init 任意の環境名
alembic init migrations

```

### 実際の DB の情報に合わせる

alembic.ini

```
sqlalchemy.url = postgresql://fastapiuser:fastapipass@0.0.0.0:5454/fleamarket
```

migrations/env.py

```
 alembic revision --autogenerate -m "create table"
 alembic upgrade head
```
