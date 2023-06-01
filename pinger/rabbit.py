"""
rabbit.py: module to ping RabbitMQ
"""
import pika
from clize import run


def rabbit_running(host: str = "localhost") -> bool:
    """
    Check if Rabbit MQ is running

    Args
    ----
        host : str, optional, default 'localhost'
        port : str, optional, default '5672'
    """
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        channel = connection.channel()
        channel.queue_declare(queue="ping", durable=True)
        channel.close()
        connection.close()
        return True
    except Exception as rabbit_error:  # pylint: disable=W0718
        print(rabbit_error)
        return False


if __name__ == "__main__":
    run(rabbit_running)
