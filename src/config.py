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
    
    # FfeDFramework settings
    FFE_D_FRAMEWORK_SETTING_1 = os.getenv('FFE_D_FRAMEWORK_SETTING_1', 'default_value_1')
    FFE_D_FRAMEWORK_SETTING_2 = os.getenv('FFE_D_FRAMEWORK_SETTING_2', 'default_value_2')
    
    # GPT2FlaskAPI settings
    GPT2_FLASK_API_SETTING_1 = os.getenv('GPT2_FLASK_API_SETTING_1', 'default_value_1')
    GPT2_FLASK_API_SETTING_2 = os.getenv('GPT2_FLASK_API_SETTING_2', 'default_value_2')
