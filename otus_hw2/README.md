# otus_hw2
Python code verbs and functions using statistic

## Installation
```bash
git clone https://github.com/S-Hanin/otus_hw2.git
cd otus_hw2
pip install -r requirements.txt
python -c "import nltk; nltk.download('averaged_perceptron_tagger')"
```
or install as a lib
```bash
git clone https://github.com/S-Hanin/otus_hw1.git
cd otus_hw2
pip install -r requirements.txt
python -c "import nltk; nltk.download('averaged_perceptron_tagger')"
python setup.py install
```

For more information about NLTK

http://www.nltk.org


## Usage

```bash
usage: pycode_stat_cli.py [-h] [-c COUNT] [-w WORDS] [-f FORMAT]
                          [-r REPORT_FILE] [--vcs VCS]
                          path

Collect statistics from python scripts about most common used verbs

positional arguments:
  path                  Path to scan for .py files

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        Count of most common used words to collect
  -w WORDS, --words WORDS
                        Find verbs(default) or nouns.
  -f FORMAT, --format FORMAT
                        Output format. Variants: console(default), json, csv
  -r REPORT_FILE, --report-file REPORT_FILE
  --vcs VCS             Clone repository from version control system. 'path'
                        will be used as target dir
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


python.exe pycode_stat_cli.py . -c 10 --vcs https://github.com/BorisPlus/otus_webpython_002
python.exe pycode_stat_cli.py C:\Python36\Lib\site-packages\nltk -c 10 -f csv -r report.csv
