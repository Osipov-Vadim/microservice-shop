
import hug


from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Text, String, Float




def main():
    db_engine = create_engine("sqlite:///items.db", echo=True)
    Base.metadata.create_all(db_engine)

    Session = sessionmaker(bind=db_engine)
    session = Session()

    new_element = Item("TestItem", 73, 100.50)
    session.add(new_element)

    print("-----")

    for instance in session.query(Item).order_by(Item.id):
            print(instance.name, instance.amount, instance.price)

    session.commit()

if (__name__ == "__main__"):
    main()
