from datetime import datetime, timedelta, timezone

from fastapi import Depends, FastAPI, Header, HTTPException
from jose import JWTError, jwt
from pydantic import BaseModel

app = FastAPI(title="JWT Authentication Assignment")

# Replace this with an environment variable in real projects.
SECRET_KEY = "replace-with-a-strong-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class LoginRequest(BaseModel):
    username: str
    password: str


USERS = {
    "student1": {"password": "pass123", "role": "student"},
    "teacher1": {"password": "teach123", "role": "admin"},
}


def create_access_token(username: str, role: str, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    # Task 1: Generate a signed JWT containing subject, role, and expiration.
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    payload = {"sub": username, "role": role, "exp": expires_at}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    # Task 2: Parse and validate the Bearer token, then return payload claims.
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    token = authorization.removeprefix("Bearer ").strip()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as err:
        raise HTTPException(status_code=401, detail="Invalid or expired token") from err

    username = payload.get("sub")
    role = payload.get("role")
    if not username or not role:
        raise HTTPException(status_code=401, detail="Token payload is missing required fields")

    return {"username": username, "role": role}


@app.post("/login")
def login(body: LoginRequest):
    # Task 1: Verify credentials and return an access token.
    user = USERS.get(body.username)
    if not user or user["password"] != body.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(body.username, user["role"])
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/me")
def read_me(current_user: dict = Depends(get_current_user)):
    # Task 2: Return authenticated user info.
    return {"username": current_user["username"]}


@app.get("/admin/report")
def admin_report(current_user: dict = Depends(get_current_user)):
    # Task 3: Restrict this endpoint to admin role.
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return {
        "report": "Confidential admin report",
        "generated_by": current_user["username"],
    }
