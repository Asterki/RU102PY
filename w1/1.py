import redis
import os

import dotenv

dotenv.load_dotenv()

HOST = os.getenv("REDIS_HOST")
PORT = os.getenv("REDIS_PORT")

client_kwargs = {
    "host": HOST,
    "port": int(PORT),
}


class RedisClient:
    def __init__(self, **kwargs):
        self.client = redis.Redis(**kwargs)

    def set(self, key, value):
        self.client.set(key, value)

    def get(self, key):
        return self.client.get(key)


if __name__ == "__main__":
    client = RedisClient(**client_kwargs)
    client.set("name", "Alice")
    print(client.get("name"))
