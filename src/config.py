import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # CodeProject.AI settings
    CODEPROJECT_AI_URL = os.getenv('CODEPROJECT_AI_SERVER_URL')
    CODEPROJECT_AI_KEY = os.getenv('CODEPROJECT_AI_KEY')
    
    # OpenAI settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
