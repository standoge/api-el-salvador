import time
from pydantic import ValidationError

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request, Response


class SyntaxisErrorMiddleware(BaseHTTPMiddleware):
    """Handle exceptions related with syntaxis errors."""

    async def dispatch(self, request: Request, call_next) -> Response:
        """Handle ValidationError and KeyError that comes commonly from syntax errors."""
        try:
            response = await call_next(request)
            return response
        except (ValidationError, KeyError):
            return JSONResponse(
                content={"query error": "That value doesn't exists"}, status_code=404
            )
        except Exception as e:
            return JSONResponse(content={"error": str(e)}, status_code=500)


class TimeMiddleware(BaseHTTPMiddleware):
    """Calculate the time that takes to process a request."""

    async def dispatch(self, request: Request, call_next) -> Response:
        """Add result to response header."""
        start = time.time()
        response = await call_next(request)
        total_time = time.time() - start
        response.headers["Process-Time"] = str(total_time)
        return response
