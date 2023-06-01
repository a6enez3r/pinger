"""contains various functions for creating a custom logger object"""
import inspect
import time
from sys import stdout
from typing import Any, Dict

from loguru import logger as custom_logger


def formatter(  # pylint: disable=too-many-return-statements
    record: Dict[str, Any]
) -> str:
    """
    custom log formatter (for loguru)

    Args
    ----
        - record (Dict(str, Any)): log object (already has metadata & message)
    """
    if record["level"].name == "TRACE":
        return "<fg #70acde>{time:MM-DD-YYYY HH:mm:ss}</fg #70acde> | <fg #cfe2f3>{level}</fg #cfe2f3>: <light-white>{message}</light-white>\n"  # pylint: disable=line-too-long
    if record["level"].name == "INFO":
        return "<fg #70acde>{time:MM-DD-YYYY HH:mm:ss}</fg #70acde> | <fg #9cbfdd>{level}</fg #9cbfdd>: <light-white>{message}</light-white>\n"  # pylint: disable=line-too-long
    if record["level"].name == "DEBUG":
        return "<fg #70acde>{time:MM-DD-YYYY HH:mm:ss}</fg #70acde> | <fg #8598ea>{level}</fg #8598ea>: <light-white>{message}</light-white>\n"  # pylint: disable=line-too-long
    if record["level"].name == "WARNING":
        return "<fg #70acde>{time:MM-DD-YYYY HH:mm:ss}</fg #70acde> |  <fg #dcad5a>{level}</fg #dcad5a>: <light-white>{message}</light-white>\n"  # pylint: disable=line-too-long
    if record["level"].name == "SUCCESS":
        return "<fg #70acde>{time:MM-DD-YYYY HH:mm:ss}</fg #70acde> | <fg #3dd08d>{level}</fg #3dd08d>: <light-white>{message}</light-white>\n"  # pylint: disable=line-too-long
    if record["level"].name == "ERROR":
        return "<fg #70acde>{time:MM-DD-YYYY HH:mm:ss}</fg #70acde> | <fg #ae2c2c>{level}</fg #ae2c2c>: <light-white>{message}</light-white>\n"  # pylint: disable=line-too-long
    return "<fg #70acde>{time:MM-DD-YYYY HH:mm:ss}</fg #70acde> | <fg #b3cfe7>{level}</fg #b3cfe7>: <light-white>{message}</light-white>\n"  # pylint: disable=line-too-long


def create():
    """
    Create a custom logger object based on loguru

    Returns
    -------
        - A a loguru object
    """
    custom_logger.remove()
    custom_logger.add(stdout, colorize=True, format=formatter)
    return custom_logger


LOGGER = create()


def logfunc(func: Any):
    """
    Decorator for easily logging all functions & methods

    by default this logs the args used, the returned value,
    any exceptions raised, & how long it took

    Args
    -----
        - func (Any): function to log
    """

    def logged(*args, **kwargs):
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        LOGGER.debug(
            f"calling: {func.__name__}, \
            filename: {caller.filename}:{caller.function}:{caller.lineno}"
        )
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return_time = time.time()
            LOGGER.debug(
                f"returning: {func.__name__}, \
                returned: {result}, \
                args: {args}, \
                kwargs: {kwargs}, \
                time: {round((return_time - start_time)*1000,1)} ms"
            )
            return result
        except Exception as exn:
            return_time = time.time()
            LOGGER.error(
                f"raised: {func.__name__}, \
                exception: {exn}, \
                args: {args}, \
                kwargs: {kwargs}, \
                time: {round((return_time - start_time)*1000,1)} ms"
            )
            raise

    return logged
