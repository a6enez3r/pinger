"""
elasticsearch_.py: module to ping Elasticsearch
"""
import requests
from clize import run

from pinger.log import logfunc


@logfunc
def elasticsearch_running(
    host: str = "localhost", port: str = "9200", timeout: int = 5
) -> bool:
    """
    Check if Elasticsearch is running

    Args
    ----
        host : str, optional, default 'localhost'
        port : str, optional, default '9200'
    """
    try:
        res = requests.get(f"http://{host}:{port}/_cluster/health", timeout=timeout)
        if res.status_code == 200:
            if res.json()["number_of_nodes"] > 0:
                return True
        return False
    except Exception as elasticsearch_error:  # pylint: disable=W0718
        print(elasticsearch_error)
        return False


if __name__ == "__main__":
    run(elasticsearch_running)
