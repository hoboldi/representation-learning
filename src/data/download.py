from pathlib import Path

import kagglehub

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

path = kagglehub.competition_download(
    'prostate-cancer-grade-assessment',
    output_dir=str(RAW_DIR),
)

print("Path to competition files:", path)
