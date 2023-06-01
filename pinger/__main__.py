"""
__main__.py: CLI interface to pinger
"""
from clize import run

from pinger.elasticsearch_ import elasticsearch_running
from pinger.mysql import mysql_running
from pinger.rabbit import rabbit_running
from pinger.redis_ import redis_running

run(
    {
        "elasticsearch": elasticsearch_running,
        "mysql": mysql_running,
        "rabbit": rabbit_running,
        "redis": redis_running,
    }
)
