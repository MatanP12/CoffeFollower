from .CoffeeModel import Coffee,CoffeeCreate, CoffeeView, CoffeeUpdate ,SQLModel
from sqlmodel import create_engine
import os
sqlite_url = os.environ.get("DATABASE_URL","sqlite:///coffee.db") 

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)
