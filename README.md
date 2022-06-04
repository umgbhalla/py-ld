# py-ld



https://user-images.githubusercontent.com/67634565/172013559-f5e67566-6adb-47bd-8bcb-e185fb880c81.mp4



## setup dev

```bash
pip install pipenv
pipenv install --python python3.9 twine --dev
pipenv shell
pip install -e .
```

## Usage

```bash
$ assault --help
Usage: assault [OPTIONS] URL

Options:
  -r, --requests INTEGER     Number of requests
  -c, --concurrency INTEGER  Number of concurrent requests
  -j, --json-file TEXT       Path to output json file
  --help
```

## tests

```bash
python -m doctest assault/stats.py
```
