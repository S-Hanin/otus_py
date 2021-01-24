# -*- coding: utf-8 -*-
import logging
import os
from wsgiref.simple_server import make_server
from request import Request
from urllib.parse import urlparse

from response import Response

DEBUG = True
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def check_url(parsed_url, urls_map_item):
    return urls_map_item == parsed_url.path
    # return re.match(urls_map_item[0], parsed_url.path.lower())


class CommonHandlersMixin:
    """
    Standard handlers
    """

    @staticmethod
    def page_not_found_handler(request, p):
        return Response("Page not found", response_code=404)

    @staticmethod
    def debug_handler(request, p, err):
        return Response("Debug page", response_code=500)

    @staticmethod
    def redirect(request, p):
        return Response("", response_code=301, headers={"location": request.request_uri.rstrip("/")})


class Application(CommonHandlersMixin):
    urls_map = []

    def handler(self, path):
        def wrap(func):
            self.urls_map.append({"path": path,
                                  "handler": func})

            def wwrap(*args, **kwargs):
                return func(*args, **kwargs)

            return wwrap
        return wrap

    def dispatch(self, request):
        parsed_url = urlparse(request.request_uri)
        if parsed_url.path.endswith("/") and parsed_url.path != "/":
            return self.redirect(request, request.parameters)

        for item in self.urls_map:
            if check_url(parsed_url, item["path"]):
                try:
                    return item["handler"](request, request.parameters)
                except Exception as err:
                    if DEBUG:
                        logger.debug(err)
                        return self.debug_handler(request, request.parameters, err)

        return self.page_not_found_handler(request, request.parameters)

    def __call__(self, env, start_response):
        request = Request.parse_environment(env)
        logger.info(request.request_uri)
        response = self.dispatch(request)

        start_response(response.status, response.headers)
        return [response.body]

    def run(self):
        try:
            server = make_server("", 8000, self)
            print("Serving on port http://localhost:8000...")
            server.serve_forever()
        except KeyboardInterrupt:
            logger.info("Server stopped")
            os._exit(1)


application = Application()


