from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Tools, Base

engine = create_engine("sqlite:///sqlalchemy_example.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

box_knife = Tools(name="Box Knife", size="Small", price=15)
drill = Tools(name="Drill", size="Medium", price=35)
axe = Tools(name="Axe", size="Large", price=55)
putty_knife = Tools(name="Putty Knife", size="Small", price=25)
hammer = Tools(name="Hammer", size="Small", price=25)
screwdriver = Tools(name="Screwdriver", size="Small", price=10)
crowbar = Tools(name="Crowbar", size="Large", price=60)

items = (box_knife, drill, axe, putty_knife, hammer, screwdriver, crowbar)

session.add_all(items)

session.commit()
