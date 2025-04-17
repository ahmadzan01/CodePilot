import re
from pathlib import Path

def parse_c_file(file_path: str):
    with open(file_path, 'r') as f:
        code = f.read()

    funcs = re.findall(r'\b\w+\s+\**(\w+)\s*\(.*?\)\s*{', code)
    return {
        "file": file_path,
        "functions": funcs
    }

def scan_c_project(root_dir: str):
    results = []
    for path in Path(root_dir).rglob("*.c"):
        results.append(parse_c_file(str(path)))
    return results
