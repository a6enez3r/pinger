from clize import run
from redis import Redis


def redis_running(host: str = "localhost", port: int = 6379) -> bool:
    """
    Check if Redis is running

    Args
    ----
        host : str, optional, default 'localhost'
        port : int, optional, default 6379
    """
    try:
        client = Redis(host=host, port=port)
        return client.ping()
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    run(redis_running)
