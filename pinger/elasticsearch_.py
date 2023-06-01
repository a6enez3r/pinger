import requests
from clize import run


def elasticsearch_running(host: str = "localhost", port: str = "9200") -> bool:
    """
    Check if Elasticsearch is running

    Args
    ----
        host : str, optional, default 'localhost'
        port : str, optional, default '9200'
    """
    try:
        res = requests.get("http://{}:{}/_cluster/health".format(host, port))
        if res.status_code == 200:
            if res.json()["number_of_nodes"] > 0:
                return True
        return False
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    run(elasticsearch_running)
