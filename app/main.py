from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from app.sentiment_model import get_sentiment
import jwt
from datetime import datetime, timedelta
from typing import List

app = FastAPI()

# JWT Configuration
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Schema for input
class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    score: float

# Token Generation
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Protected Route
def get_current_user(token: str = Depends()):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise credentials_exception

@app.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: SentimentRequest):
    sentiment, score = get_sentiment(request.text)
    return SentimentResponse(sentiment=sentiment, score=score)

def main():
    print("Hello, World!")

def broken_function():
    # این تابع عمداً ارور می‌دهد
    return 1 / 0  # تقسیم بر صفر