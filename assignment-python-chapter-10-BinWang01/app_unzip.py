# Bin Wang
from zipfile import ZipFile
from pathlib import Path

source_directory = "worldbank_zipfiles"
target_directory = "worldbank_data"
path = Path(source_directory)
list_of_files = [file for file in path.rglob("*.zip")]

for file in list_of_files:
    with ZipFile(file) as zip:
        zip.extractall(target_directory)
