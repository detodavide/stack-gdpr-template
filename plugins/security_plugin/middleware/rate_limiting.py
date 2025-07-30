from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
r = redis.Redis.from_url(REDIS_URL)
RATE_LIMIT = 100  # richieste per IP ogni 60 secondi
WINDOW = 60

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        ip = request.client.host
        key = f"rate:{ip}"
        now = int(time.time())
        window_start = now - WINDOW
        r.zremrangebyscore(key, 0, window_start)
        r.zadd(key, {str(now): now})
        count = r.zcard(key)
        r.expire(key, WINDOW)
        if count > RATE_LIMIT:
            return Response("Rate limit exceeded", status_code=429)
        return await call_next(request)
