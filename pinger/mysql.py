from clize import run
from pymysql import connect
from pymysql.cursors import DictCursor


def mysql_running(
    host: str = "localhost",
    port: int = 3306,
    user: str = "www",
    password: str = "j8Kuc00n",
    db: str = "licensedb",
) -> bool:
    """
    Check if MySQL is running

    Args
    ----
        host : str, optional, default 'localhost'
        port : str, optional, default '9200'
        user : str, optional, default 'www'
        password : str, optional, default 'j8Kuc00n'
        db : str, optional, default 'licensedb'
    """
    # create the connection
    connection = connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        cursorclass=DictCursor,
    )

    # get the cursor
    cursor = connection.cursor()

    # if the connection was lost, then it reconnects
    connection.ping(reconnect=True)


if __name__ == "__main__":
    run(mysql_running)
