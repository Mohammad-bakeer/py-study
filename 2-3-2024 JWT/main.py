import jwt

#json
t={"some":"thing"}

en_jwt = jwt.encode(t, "secret", algorithm="HS256")
print(en_jwt)

de_jwt = jwt.decode(en_jwt, "secret", algorithms="HS256")
print(de_jwt)