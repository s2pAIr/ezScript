import jwt
sk = open("jwt").read()
pk = open("jwt.pub").read()
token = jwt.encode({"x": "y"}, sk, algorithm="ES256")
print(token)
print(jwt.decode(token, pk))