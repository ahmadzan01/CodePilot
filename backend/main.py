from fastapi import FastAPI
from backend.parser.java_parser import scan_java_project
from backend.parser.c_parser import scan_c_project
from backend.patterns.singleton import detect_singleton

app = FastAPI() 

@app.get("/")
def root():
    return {"message": " CodePilot backend is live!"}

@app.get("/scan/java")
def scan_java():
    return scan_java_project("test_projects/java")

@app.get("/scan/c")
def scan_c():
    return scan_c_project("test_projects/c")

@app.get("/detect/singleton")
def check_singleton():
    files = scan_java_project("test_projects/java")
    results = [detect_singleton(f) for f in files]
    return results
