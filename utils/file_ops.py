import os
import hashlib
import time

def safe_basename(filename: str) -> str:
    return os.path.basename(filename)

def stem_with_hash(filename: str, data: bytes, suffix: str) -> str:
    stem, _ = os.path.splitext(safe_basename(filename))
    h = hashlib.md5(data).hexdigest()[:8]
    return f"{stem}-{h}{suffix}"

def timestamp() -> str:
    """Return a safe timestamp string for filenames."""
    return time.strftime("%Y%m%d-%H%M%S")
