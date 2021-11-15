import logging

from typing import Callable

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.WARN)


def with_logging(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        logger.info(f"Calling '{func.__name__}' method", extra=kwargs)
        try:
            result = func(*args, **kwargs)
        except Exception as ex:
            logger.exception(f"'{func.__name__}' method threw an exception", extra=kwargs)
            raise ex from ex
        return result

    return inner
