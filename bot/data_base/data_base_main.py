from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from table_models import AllData, Base, MenShoes, WomenShoes, ChildrenShoes, MenSlippers, WomenSlippers
import csv

engine = create_engine('sqlite:///data_all.db')
metadata = MetaData()

Base.metadata.create_all(engine)

with open(r'C:\TrueShop2site\All.csv') as exs:
    reader = csv.DictReader(exs, delimiter=";")
    with Session(engine) as session:
        for i in reader:
            user = AllData(code=i['code'], group_code=i['group_code'], name=i['name'], photo=i['photo'],
                           price=i['price'], quantity=i['quantity'], size=i['Размер'])

            session.add(user)
        session.commit()


def add_data_in_table(table_class, filter_data):
    with Session(engine) as session:
        for i in session.query(AllData).filter(AllData.name.like(filter_data)).filter(AllData.quantity > 0):
            men_shoes = table_class(code=i.code, group_code=i.group_code, name=i.name, photo=i.photo,
                                    price=i.price, quantity=i.quantity, size=i.size)
            session.add(men_shoes)
        session.commit()


add_data_in_table(MenShoes, "МУЖ%")
