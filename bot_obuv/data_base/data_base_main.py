from sqlalchemy import create_engine, MetaData, update, exists, or_
from sqlalchemy.orm import Session
from bot_obuv.data_base.table_models import AllData, Base, Catalog, CatalogAll
import csv

engine = create_engine('sqlite:///data_all.db')
metadata = MetaData()
session = Session()
Base.metadata.create_all(engine)

d = 'Y:\Обувь\Photo'
g = 'Нет фото.jpg'


def great_all_goods_table():
    with open(r'C:\TrueShop2site\All.csv') as exs:
        reader = csv.DictReader(exs, delimiter=";")
        with Session(engine) as session:
            for i in reader:
                user = AllData(code=i['code'], group_code=i['group_code'], name=(str(i['name'])[:15]), photo=i['photo'],
                               price=i['price'], quantity=i['quantity'], size=i['Размер'])

                session.add(user)
            session.commit()


def great_catalog_all():
    with Session(engine) as session:
        for i in session.query(AllData).filter(or_(AllData.name.like('МУЖ%'),
                                                   AllData.name.like('ЖЕН%'),
                                                   AllData.name.like('ДЕТ%'),
                                                   AllData.name.like('Тапки%'))).filter(AllData.quantity > 0):
            if i.photo:
                cat = CatalogAll(name=i.name, photo="\\".join([d, i.photo]),
                                 price=i.price)
            else:
                i.photo = g
            session.add(cat)
        session.commit()


def check_table(table_name):
    with Session(engine) as session:
        for i in table_name:
            rt = session.query(exists().where(i.id.isnot(None))).scalar()

            if rt:
                session.close()

            elif i.__tablename__ == 'all_goods':
                great_all_goods_table()

            elif i.__tablename__ == 'catalog_all':
                great_catalog_all()

            elif i.__tablename__ == 'catalog':
                great_catalog_shoes()

        session.commit()


def great_catalog_shoes():
    values_for_the_catalog_table = dict()
    with Session(engine) as session:
        dict_values = session.query(CatalogAll.name, CatalogAll.price, CatalogAll.photo)
        for i in dict_values:
            new_values_in_dict = dict()
            new_values_in_dict[i[0]] = i[1], i[2]
            values_for_the_catalog_table .update(new_values_in_dict)

    with Session(engine) as ses:
        for i in values_for_the_catalog_table :
            catalog = Catalog(name=i, price=values_for_the_catalog_table [i][0],
                              photo=values_for_the_catalog_table[i][1])
            ses.add(catalog)
        ses.commit()


table_name_list = [AllData, CatalogAll, Catalog]

check_table(table_name_list)
