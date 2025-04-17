def detect_singleton(java_file: dict):
    """
    Detects if a Java class follows a basic Singleton pattern.
    Looks for: private static instance + getInstance() method
    """
    file_path = java_file["file"]
    with open(file_path, "r") as f:
        code = f.read()

    class_name = java_file["classes"][0] if java_file["classes"] else None
    has_static_instance = False
    has_get_instance = False

    if class_name:
        # Look for something like: private static Example instance;
        if f"private static {class_name}" in code or f"private static {class_name} " in code:
            has_static_instance = True

    # Look for getInstance()
    if "getInstance()" in code:
        has_get_instance = True

    return {
        "file": file_path,
        "is_singleton": has_static_instance and has_get_instance,
        "has_static_instance": has_static_instance,
        "has_get_instance": has_get_instance
    }
