import jwt
SK = "secret key"
x = jwt.encode({"x": "y"}, SK, algorithm="HS256")
print(x)

print(jwt.decode(x, SK))