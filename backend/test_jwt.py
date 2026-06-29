from app.auth.jwt_handler import create_access_token, verify_token

token = create_access_token(
    {"sub": "jeevan@example.com"}
)

print("TOKEN:")
print(token)

print()

print("PAYLOAD:")
print(verify_token(token))