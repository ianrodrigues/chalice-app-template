import os
from pathlib import Path

current_dir = Path.cwd().name.lower()

if app_name := input(f"Application Name [{current_dir}]: ") == "":
    app_name = current_dir

for file in ["app.py", ".chalice/config.json"]:
    contents = Path(file).read_text()
    contents = contents.replace(":app-name:", app_name)

    with Path(file).open("w") as file:
        file.write(contents)

os.system("pip install -r requirements-dev.txt")

Path("configure.py").unlink()
