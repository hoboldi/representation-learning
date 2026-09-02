"""Download the PANDA competition dataset from Kaggle.
https://www.kaggle.com/competitions/prostate-cancer-grade-assessment/data

Prerequisites: run ``kaggle auth login`` once, and accept the competition rules
on the website.

Usage:
    python -m src.data.download /path/to/data/raw/panda
"""

import argparse
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "dest",
    type=Path,
    nargs="?",
    default=Path(__file__).parent.parent.parent / "data" / "raw" / "panda",
)

dest = parser.parse_args().dest.expanduser()
dest.mkdir(parents=True, exist_ok=True)

api = KaggleApi()
api.authenticate()

api.competition_download_files("prostate-cancer-grade-assessment", path=str(dest), quiet=False)
