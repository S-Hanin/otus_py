# -*- coding: utf-8 -*-
import http.client


class Response:
    """
    Used for making response from views
    """
    def __init__(self, response_body, response_code=200, content_type="text/html", headers=None):
        """
        :param response_body: string
        :param response_code: int
        :param content_type: string, default: 'text/html'
        :param headers: dict, additional response headers
        """
        self._response_body = response_body
        self._response_code = response_code
        self._headers = dict()
        self._headers["Content-type"] = content_type
        if headers:
            self._headers.update(headers)

    @property
    def body(self):
        return self._response_body.encode("utf-8")

    @property
    def code(self):
        return self._response_code

    @property
    def status(self):
        return '{0} {1}'.format(self._response_code, http.client.responses[self._response_code])

    @property
    def headers(self):
        headers = [(k, self._headers[k]) for k in self._headers.keys()]
        return headers

    def __bool__(self):
        return True if self.body else False
