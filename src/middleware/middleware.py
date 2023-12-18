from flask import Request


class CleanUpMiddleware:
    def __init__(self, app):
        self.app = app
        self.denied_symbols = "#-*()\\`\'\"="

    def __call__(self, environ, start_response):
        request = Request(environ)
        # Удаление знака решетки из данных запроса
        if request.data:
            for denied_symbol in self.denied_symbols:
                request.data = request.data.replace(bytes(denied_symbol, encoding="ascii"), b'')
        # передача запроса дальше по стеку Middleware
        return self.app(environ, start_response)
