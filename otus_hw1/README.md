# otus_hw1
Python code verbs and functions using statistic

## Installation
```bash
git clone https://github.com/S-Hanin/otus_hw1.git
cd otus_hw1
pip install -r requirements.txt
python -c "import nltk; nltk.download('averaged_perceptron_tagger')"
```
or install as a lib
```bash
git clone https://github.com/S-Hanin/otus_hw1.git
cd otus_hw1
pip install -r requirements.txt
python -c "import nltk; nltk.download('averaged_perceptron_tagger')"
python setup.py install
```

For more information about NLTK

http://www.nltk.org


## Usage

```bash
python pycode_stat_cli.py -h
usage: pycode_stat_cli.py [-h] [-c COUNT] path

Collect statistics from python scripts about most common functions and used verbs

positional arguments:
  path                  Path to scan for .py files

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        Optional. Count of most common used words to collect
```

## Example

```bash
python.exe pycode_stat_cli.py C:\Python36\Lib\site-packages\nltk -c 5
--------------------------------------------------------------------------------
total 501 words, 28 unique
--------------------------------------------------------------------------------
get                 :   126
apply               :    61
make                :    54
tokenize            :    49
add                 :    47
--------------------------------------------------------------------------------
total 4672 functions, 2956 unique
--------------------------------------------------------------------------------
demo                :    76
words               :    37
train               :    32
apply               :    31
raw                 :    30
