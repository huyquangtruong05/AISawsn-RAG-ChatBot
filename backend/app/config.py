from pydantic import BaseModel

class Settings(BaseModel) :
    PROJECT_NAME: str = "AISawsn Platform"
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./app.db"

settings = Settings()

