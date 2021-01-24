# -*- coding: utf-8 -*-
import logging
from wsgiref import util

logger = logging.getLogger(__name__)


class Request:
    """
    Wrapper for request environment
    """
    @staticmethod
    def parse_parameters(query_string):
        """
        splits request parameters
        :param query_string:
        :return: dict
        """
        parameters = {}
        if not query_string:
            return parameters
        params = query_string.split("&")
        for param in params:
            pair = param.split("=")
            parameters.setdefault(pair[0], pair[1])
        return parameters

    @staticmethod
    def parse_environment(env):
        request = Request()

        request.request_uri = util.request_uri(env, True)
        for k, v in env.items():
            request.__dict__.setdefault(k.lower(), v)
        request.query_parameters = Request.parse_parameters(request.query_string)
        return request

    @property
    def method(self):
        """
        request method
        :return: string
        """
        return self.request_method

    @property
    def parameters(self):
        """

        :return: dict
        """
        return self.query_parameters

    def _log(self):
        for k, v in sorted(self.__dict__.items()):
            logger.info("{}: {}".format(k, v))
