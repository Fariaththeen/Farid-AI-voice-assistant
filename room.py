import jwt
import time

# Replace with your credentials from https://cloud.livekit.io
API_KEY = "APIREmYxHqw9n42"
API_SECRET = "fpJfpVrN07qYI6ip46YfbcPhVJe32w34fKpRS2T8mgNC"
ROOM_NAME = "farid-room"
IDENTITY = "farid-assistant"

# Token expiration (1 hour from now)
now = int(time.time())
exp = now + 60 * 60  # 1 hour

# JWT payload
payload = {
    "jti": f"{IDENTITY}-{now}",
    "iss": API_KEY,
    "sub": IDENTITY,
    "nbf": now,
    "exp": exp,
    "video": {
        "room_join": True,
        "room": ROOM_NAME,
        "can_publish": True,
        "can_subscribe": True,
    }
}

# Generate token
token = jwt.encode(payload, API_SECRET, algorithm="HS256")

print("Generated token:\n", token)
