import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "app/__init__.py",
    "app/helper.py",
    "app/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    if filedir != "":
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
