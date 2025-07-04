from dotenv import load_dotenv
import os
from typing import Dict

def load_environment() -> Dict[str, str]:
    """Load and validate all required environment variables"""
    load_dotenv()  
    
    required_vars = {
        'NVIDIA_API_KEY':'Nvidia NIM key',
    }
    
    config = {}
    for var, description in required_vars.items():
        value = os.getenv(var)
        if not value:
            raise ValueError(f"Missing required environment variable: {var} ({description})")
        config[var] = value
    
    return config

# Initialize and export all configs
try:
    CONFIG = load_environment()
except ValueError as e:
    print(f"Configuration error: {str(e)}")
    raise