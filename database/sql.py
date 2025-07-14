from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///sqlite3.db")

SQLModel.metadata.create_all(engine)
