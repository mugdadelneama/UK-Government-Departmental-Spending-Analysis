import pandas as pd
from pathlib import Path

# # Check your current working directory
# import os
# print("Current directory:", os.getcwd())

# # Define paths
# raw_data_path = Path('data/raw data')

# # Check if path exists
# print(f"\nDoes path exist? {raw_data_path.exists()}")

# # Try to find files
# csv_files_2024 = list((raw_data_path / '2024').glob('*.csv'))
# csv_files_2025 = list((raw_data_path / '2025').glob('*.csv'))

# print(f"\nFiles found in 2024: {len(csv_files_2024)}")
# print(f"Files found in 2025: {len(csv_files_2025)}")

# # Show first few files
# if csv_files_2024:
#     print("\nFirst 2024 file:", csv_files_2024[0])
# if csv_files_2025:
#     print("First 2025 file:", csv_files_2025[0])



# # Define the path
# raw_data_path = Path('data') / 'raw data'

# # Get CSV files from both folders
# csv_files_2024 = list((raw_data_path / '2024').glob('*.csv'))
# csv_files_2025 = list((raw_data_path / '2025').glob('*.csv'))

# # Combine the lists
# all_files = csv_files_2024 + csv_files_2025

# # Debug: print what was found
# print(f"Files in 2024: {len(csv_files_2024)}")
# print(f"Files in 2025: {len(csv_files_2025)}")
# print(f"Total files: {len(all_files)}")

# # If files found, combine them
# if all_files:
#     df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)
#     print(f"\n✓ Combined successfully!")
#     print(f"Shape: {df.shape}")
#     df.head()
# else:
#     print("\n✗ No files found - check the path!")



import pandas as pd
from pathlib import Path

# Define the path
raw_data_path = Path('data') / 'raw data'

# Get CSV files from both folders
csv_files_2024 = list((raw_data_path / '2024').glob('*.csv'))
csv_files_2025 = list((raw_data_path / '2025').glob('*.csv'))

# Combine the lists
all_files = csv_files_2024 + csv_files_2025

# CHECK HOW MANY FILES WERE FOUND
print(f"Files in 2024: {len(csv_files_2024)}")
print(f"Files in 2025: {len(csv_files_2025)}")
print(f"Total files: {len(all_files)}")

# Print first few filenames if found
if len(all_files) == 0:
    print("No files found! Current working directory:")
    print(Path.cwd())
    print("\nChecking if path exists:")
    print(f"Path exists: {raw_data_path.exists()}")
else:
    # Combine into DataFrame with proper encoding
    dfs = []
    for f in all_files:
        try:
            # Try UTF-8 first
            df_temp = pd.read_csv(f, encoding='utf-8')
        except UnicodeDecodeError:
            # Fall back to Windows-1252 (common for UK government data with £ symbols)
            df_temp = pd.read_csv(f, encoding='windows-1252')
        dfs.append(df_temp)
    
    df = pd.concat(dfs, ignore_index=True)
    print(f"✓ Combined! Shape: {df.shape}")
    print(df.head())




