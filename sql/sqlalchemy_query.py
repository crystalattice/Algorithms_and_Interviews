from sql.sqlalchemy_declarative import Base, Tools
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sqlalchemy_example.db")

Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Query all entries in database
tools = session.query(Tools).all()
for tool in tools:
    print(tool.name)

# Return first entry in database
tool = session.query(Tools).first()
print("\n" + tool.name)

# Return the tool with given price
priced_tool = session.query(Tools).filter(Tools.price == 10).one()
print("\n" + priced_tool.name + "\n")

# Return all the tools with a given price
priced_tools = session.query(Tools).filter(Tools.price == 25).all()
for tool in priced_tools:
    print(tool.name)
