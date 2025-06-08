from datetime import datetime, timedelta
import jwt
from typing import Dict, Optional
from flask import current_app

def generate_token(user_id: int, expires_delta: Optional[timedelta] = None) -> str:
    """Generate JWT token for user."""
    now = datetime.utcnow()
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES'])
    
    payload = {
        'user_id': user_id,
        'exp': expire,
        'iat': now
    }
    return jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')

def validate_token(token: str) -> Optional[Dict]:
    """Validate JWT token and return payload if valid."""
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
