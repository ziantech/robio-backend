from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class BlockExploitPathsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path.lower()
        known_bots = [
            "/ws/ec/vendor/phpunit/phpunit/src/util/php/eval-stdin.php",
            "/.env", "/.git", "/wp-login.php"
        ]
        if path in known_bots:
            return Response("Forbidden", status_code=403)
        return await call_next(request)
