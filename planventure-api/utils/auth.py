import hashlib
import os

def generate_salt() -> bytes:
    """Generate a random salt for password hashing."""
    return os.urandom(32)

def hash_password(password: str, salt: bytes) -> str:
    """Hash password with salt using SHA-256."""
    hash_obj = hashlib.sha256()
    hash_obj.update(salt + password.encode('utf-8'))
    return hash_obj.hexdigest()

def verify_password(stored_hash: str, password: str, salt: bytes) -> bool:
    """Verify if provided password matches stored hash."""
    return stored_hash == hash_password(password, salt)
