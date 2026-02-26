from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Parable(Base):
    __tablename__ = 'parables'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    lesson = Column(String)

engine = create_engine('sqlite:///bible.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

parable = Parable(title="Prodigal Son", lesson="Forgiveness")
session.add(parable)
session.commit()

results = session.query(Parable).all()
for p in results:
    print(p.title)