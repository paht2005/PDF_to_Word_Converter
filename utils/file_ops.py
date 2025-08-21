import os, hashlib

def safe_basename(name: str, default="file") -> str:
    name = (name or "").strip().replace("\\", "/").split("/")[-1]
    allowed = "-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    cleaned = "".join(c for c in name if c in allowed)
    return cleaned or default

def stem_with_hash(name: str, data: bytes, suffix: str) -> str:
    base = os.path.splitext(safe_basename(name))[0]
    h = hashlib.sha1(data).hexdigest()[:8]
    return f"{base}-{h}{suffix}"
