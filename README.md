## database.py

データベースへの接続セッション管理<br>
sqlalchemy create_engine でセッション作成<br>
sqlalchemy declarative_base を使用して基盤クラスを作成 Base<br>

## models.py

DB 内にできあるテーブルをクラスとして作成<br>
その際 Base クラスを継承<br>

## schemas.py

Pydantic スキーマを定義する pydantyc baseModel を継承<br>
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

uvicorn sql_app.main:app --host=0.0.0.0 --port=8686 --reload
