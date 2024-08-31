# Bin Wang
from pathlib import Path
from time import ctime
import shutil

# Chapter 9.2 - Working With Paths
print("Chapter 9.2 - Working With Paths " + "-" * 20)
path = Path(r"ecommerce/shipping.py")
print(f"Is the path object a file? {path.is_file()}")

path = Path("ecommerce/__init__.py")
print(f"Does the path object exist? {path.exists()}")
print(f"Is the path object a file? {path.is_file()}")
print(f"Is the path object a directory ? {path.is_dir()}")
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_suffix(".txt")
print(path)

# Chapter 9.3 - Working With Directories
print("\nChapter 9.3 - Working With Directories " + "-" * 20)
path = Path("blog")
if not path.exists():
    print("Directory does not yet exists")
    path.mkdir()
else:
    print("Directory already exists.")

path = Path(".")
print("List of directories:")
path_of_directories = [p for p in path.iterdir() if p.is_dir()]

print(path_of_directories)

print("List of .py files:")
path_of_pyfiles = [p for p in path.rglob("*.py")]

print(path_of_pyfiles)

one_file = path_of_pyfiles[0]
print(one_file.name)
print(one_file.stem)
print(one_file.suffix)

# Chapter 9.4 - Working With Files
print("\nChapter 9.4 - Working With Files " + "-" * 20)
path = Path("ecommerce/__init__.py")
print(ctime(path.stat().st_ctime))

print(path.read_text())
path_tax = Path("ecommerce/tax.py")
message = "# Add another comment to the file"
path_tax.write_text(message)


source = Path("ecommerce/__init__.py")
target = Path("ecommerce/__init__backup.py")
shutil.copy(source, target)
