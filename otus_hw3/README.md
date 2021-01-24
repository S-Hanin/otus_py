# otus_hw3
very simple wsgi framework just for study.
Kind of looks like flask. Very very slashed.

### Requirements
```text
Works good with python >= 3.5
No third-party libs required, only standard
```

### Installation
```bash
git clone https://github.com/S-Hanin/otus_hw3.git
cd otus_hw3
python setup.py install
```

### Code example
```python
from otus_hw3 import app

application = app.application

# each view function gets two parameters:
# request object and query parameters as dict


@application.route("/")
def index(request, p):
    return "{} index page".format(request.request_uri)


@application.route("/help")
def help(request, p):
    return "{} help page query={}".format(request.request_uri, p.get('q', None))


@application.route("/about")
def about(request, p):
    return "{} about page".format(request.request_uri)


if __name__ == "__main__":
    application.run()
```

