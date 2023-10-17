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

with Session(engine) as session:
    for i in session.query(AllData).filter(AllData.name.like("МУЖ%")).filter(AllData.quantity > 0):
        men_shoes = MenShoes(code=i.code, group_code=i.group_code, name=i.name, photo=i.photo,
                             price=i.price, quantity=i.quantity, size=i.size)
        session.add(men_shoes)
    session.commit()

with Session(engine) as session:
    for i in session.query(AllData).filter(AllData.name.like("ЖЕН%")).filter(AllData.quantity > 0):
        women_shoes = WomenShoes(code=i.code, group_code=i.group_code, name=i.name, photo=i.photo,
                                 price=i.price, quantity=i.quantity, size=i.size)
        session.add(women_shoes)
    session.commit()

with Session(engine) as session:
    for i in session.query(AllData).filter(AllData.name.like("ДЕТ%")).filter(AllData.quantity > 0):
        children_shoes = ChildrenShoes(code=i.code, group_code=i.group_code, name=i.name, photo=i.photo,
                                       price=i.price, quantity=i.quantity, size=i.size)
        session.add(children_shoes)
    session.commit()

with Session(engine) as session:
    for i in session.query(AllData).filter(AllData.name.like("ДЕТ%")).filter(AllData.quantity > 0):
        children_shoes = ChildrenShoes(code=i.code, group_code=i.group_code, name=i.name, photo=i.photo,
                                       price=i.price, quantity=i.quantity, size=i.size)
        session.add(children_shoes)
    session.commit()

with Session(engine) as session:
    for i in session.query(AllData).filter(AllData.name.like("%Тм%")).filter(AllData.quantity > 0):
        men_slippers = MenSlippers(code=i.code, group_code=i.group_code, name=i.name, photo=i.photo,
                                   price=i.price, quantity=i.quantity, size=i.size)
        session.add(men_slippers)
    session.commit()

with Session(engine) as session:
    for i in session.query(AllData).filter(AllData.name.like("%Тж%")).filter(AllData.quantity > 0):
        women_slippers = WomenSlippers(code=i.code, group_code=i.group_code, name=i.name, photo=i.photo,
                                       price=i.price, quantity=i.quantity, size=i.size)
        session.add(women_slippers)
    session.commit()



