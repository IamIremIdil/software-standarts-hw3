
import os
import redis
from flask import Flask

app = Flask(__name__)

GREETING = os.environ.get("APP_GREETING", "Hello")

r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", "6379")),
    password=os.environ.get("REDIS_PASSWORD") or None,
    decode_responses=True,
    socket_connect_timeout=3,
)

@app.route("/health")
def health():
    return {"status": "ok"}
# liveness probe to check if the app is running and responsive

@app.route("/ready")
def ready():
    try:
        r.ping()
        return {"status": "ready"}
    except redis.RedisError:
        return {"status": "not_ready"}, 503
    # readiness probe to check if the app is ready to serve requests and can connect to Redis

@app.route("/greet")
def greet():
    return {"message": GREETING}

@app.route("/visit")
def visit():
    count = r.incr("visits")
    return {"visits": count}

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8000"))
    )
