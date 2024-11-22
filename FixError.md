# 책 출간 후 오류가 발견된 부분을 수정합니다.

## 62
원문
```
with SessionLocal() as db:
    db = SessionLocal()  //(3)
    db.add(new_user)  //(4)
    db.commit()  //(5)
```
(3): 앞서 만든 `SessionLocal`을 이용해 새로운 세션 객체를 생성한다.

수정
```
with SessionLocal() as db:  //(3)
    db.add(new_user)  //(4)
    db.commit()  //(5)
```

(3): `SessionLocal` 객체를 생성한다. with 구문을 이용하여 세션이 자동으로 닫히도록 하였다.

## p82
원문
```
password=crypto.encrypt("test")
```
수정
```
password=Crypto().encrypt("test")
```

