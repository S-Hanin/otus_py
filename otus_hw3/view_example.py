import app
from response import Response

application = app.application


@application.handler("/")
def index(request, p):
    return Response("{} index page".format(request.request_uri))


@application.handler("/help")
def help(request, p):
    return Response("{}: q={} help page".format(request.request_uri, p.get('q', None)))


@application.handler("/about")
def about(request, p):
    return Response("{} about page".format(request.request_uri))


if __name__ == "__main__":
    application.run()
