from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from bot.data_base.table_models import AllData, Base, MenShoes, Catalog

import csv


engine = create_engine('sqlite:///data_all.db')
metadata = MetaData()
session = Session()
Base.metadata.create_all(engine)

d = 'Y:\Обувь\Photo'


def great_all_goods_table():
    with open(r'C:\TrueShop2site\All.csv') as exs:
        reader = csv.DictReader(exs, delimiter=";")
        with Session(engine) as session:
            for i in reader:
                user = AllData(code=i['code'], group_code=i['group_code'], name=(str(i['name'])[:15]), photo=i['photo'],
                               price=i['price'], quantity=i['quantity'], size=i['Размер'])

                session.add(user)
            session.commit()


def add_data_in_table(table_class, filter_data):
    with Session(engine) as session:
        for i in session.query(AllData).filter(AllData.group_code.like(filter_data)).filter(AllData.quantity > 0):
            men_shoes = table_class(code=i.code, group_code=i.group_code, name=i.name, photo="\\".join([d, i.photo]),
                                    price=i.price, quantity=i.quantity, size=i.size)
            session.add(men_shoes)
        session.commit()



great_all_goods_table()
add_data_in_table(MenShoes, 12)

with Session(engine) as session:
    d = session.query(MenShoes.name).distinct().all()
    for i in d:
        print(i[0])