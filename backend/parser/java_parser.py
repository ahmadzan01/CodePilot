import re
from pathlib import Path

def parse_java_file(file_path: str):
    with open(file_path, 'r') as f:
        code = f.read()

    classes = re.findall(r'class\s+(\w+)', code)
    methods = re.findall(r'(public|private|protected)?\s*(static)?\s*\w+\s+(\w+)\s*\(', code)

    return {
        "file": file_path,
        "classes": classes,
        "methods": [match[2] for match in methods]
    }

def scan_java_project(root_dir: str):
    results = []
    for path in Path(root_dir).rglob("*.java"):
        results.append(parse_java_file(str(path)))
    return results
