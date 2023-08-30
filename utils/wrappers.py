import http

from loguru import logger
from starlette.responses import JSONResponse

from utils.errors import ErrEntityNotFound, ErrEntityConflict


def error_wrapper(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except ErrEntityNotFound as e:
        logger.debug(f"err = {e}")
        return JSONResponse(status_code=http.HTTPStatus.NOT_FOUND, content={"msg": str(e)})
    except ErrEntityConflict as e:
        logger.debug(f"err = {e}")
        return JSONResponse(status_code=http.HTTPStatus.CONFLICT, content={"msg": str(e)})
    except Exception as e:
        logger.error(f"err = {e}")
        return JSONResponse(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, content={"msg": str(e)})