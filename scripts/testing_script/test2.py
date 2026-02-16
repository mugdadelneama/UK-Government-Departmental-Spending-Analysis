import pandas as pd
from pathlib import Path

# From 'processed data', go up to parent, then into 'data/raw data'
raw_data_path = Path('..') / 'raw data'

# Get CSV files from both folders
csv_files_2024 = list((raw_data_path / '2024').glob('*.csv'))
csv_files_2025 = list((raw_data_path / '2025').glob('*.csv'))

# Combine the lists
all_files = csv_files_2024 + csv_files_2025

print(f"Total files found: {len(all_files)}")

if len(all_files) == 0:
    print("No files found! Current working directory:")
    print(Path.cwd())
    print("\nChecking if path exists:")
    print(f"Path exists: {raw_data_path.exists()}")
else:
    # Combine into DataFrame
    df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)
    print(f"✓ Combined! Shape: {df.shape}")
    print(df.head())