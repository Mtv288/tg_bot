from sqlalchemy import create_engine, MetaData, update, exists, or_, and_
from sqlalchemy.orm import Session
from bot_obuv.data_base.table_models import AllData, Base, Catalog, CatalogAll, Users
import csv

engine = create_engine('sqlite:///data_all.db')
metadata = MetaData()
session = Session()
Base.metadata.create_all(engine)

path_to_foto = 'H:\Photo'
photo_for_mistake = 'Нет фото.jpg'


def great_all_goods_table():
    """
    Собираем основную таблицу всех товаров с дублированными товарами и товарами с нулевым остатком из csv файла
    :return: Ничего не возвращает
    """
    try:
        with open(r'C:\TrueShop2site\All.csv') as exs:
            reader = csv.DictReader(exs, delimiter=";")
            with Session(engine) as session:
                for i in reader:
                    user = AllData(code=i['code'], group_code=i['group_code'], name=(str(i['name'])), photo=i['photo'],
                                   price=i['price'], quantity=i['quantity'], size=i['Размер'])
                    session.add(user)
                session.commit()

    except FileNotFoundError:
        with open(r'All.csv') as exs:
            reader = csv.DictReader(exs, delimiter=";")
            with Session(engine) as session:
                for i in reader:
                    user = AllData(code=i['code'], group_code=i['group_code'], name=(str(i['name'])),
                                   photo=photo_for_mistake,
                                   price=i['price'], quantity=i['quantity'], size=i['Размер'])

                    session.add(user)
                session.commit()


def great_catalog_all():
    """
    Собираем таблицу CatalogAll здесь определенные виды товара и отсутствует товары с нулевым остатком
    В случае если путь к папкам с фото и бд не найден вставляем старый образец бд и заглушку для фото
    :return: Ничего не возвращает
    """
    with Session(engine) as session:
        for i in session.query(AllData).filter(or_(AllData.name.like('МУЖ%'),
                                                   AllData.name.like('ЖЕН%'),
                                                   AllData.name.like('ДЕТ%'),
                                                   AllData.name.like('Тапки%'))).filter(AllData.quantity != 0):

            try:
                if i.photo:
                    cat = CatalogAll(name=i.name, photo="\\".join([path_to_foto, i.photo]),
                                     price=i.price, size=i.size, quantity=i.quantity)

                else:
                    i.photo == photo_for_mistake
                    cat = CatalogAll(name=i.name, photo=photo_for_mistake,
                                     price=i.price, size=i.size, quantity=i.quantity)

            except FileNotFoundError:
                i.photo = photo_for_mistake

            session.add(cat)
        session.commit()


def check_table(table_name):
    """
    Проверяем таблицы на их содержание и если таблица пустая заполняем
    :param table_name: Список таблиц для проверки
    :return: Ничего не возвращаем
    """
    with Session(engine) as session:
        for i in table_name:
            table_instance = session.query(exists().where(i.id.isnot(None))).scalar()

            if table_instance:
                session.close()

            elif i.__tablename__ == 'all_goods':
                great_all_goods_table()

            elif i.__tablename__ == 'catalog_all':
                great_catalog_all()

            elif i.__tablename__ == 'catalog':
                great_catalog_shoes()

        session.commit()


def great_catalog_shoes():
    """
    Убираем дубли товаров с помощью словаря и создаем таблицу Catalog для получения полноценного каталога
    с ценой и фото товара
    :return: Ничего не возращаем
    """
    values_for_the_catalog_table = dict()
    with Session(engine) as session:
        dict_values = session.query(CatalogAll.name, CatalogAll.price, CatalogAll.photo)
        for i in dict_values:
            new_values_in_dict = dict()
            new_values_in_dict[i[0]] = i[1], i[2]
            values_for_the_catalog_table.update(new_values_in_dict)

    with Session(engine) as ses:
        if session.query(exists().where(CatalogAll.id.isnot(None))).scalar():
            for i in values_for_the_catalog_table:
                catalog = Catalog(name=i, price=values_for_the_catalog_table[i][0],
                                  photo=values_for_the_catalog_table[i][1])
                ses.add(catalog)
            ses.commit()
        else:
            for i in values_for_the_catalog_table:
                catalog = Catalog(name=i, price=values_for_the_catalog_table[i][0],
                                  photo=values_for_the_catalog_table[i][1])
                ses.add(catalog)
            ses.commit()



def list_name_goods():
    list_goods = []
    with Session(engine) as ses:
        goods = ses.query(Catalog.name)
        for i in goods:
            list_goods.append(i[0][8:14])
    return list_goods


def get_price_and_size_good_and_photo(good_name):
    """
    Функция получает на вход название товара и находит в базе данных соответсвующий товар, фото товара
    его цену, размеры и количество по каждому размеру
    :param good_name: Имя товара
    :return: Список размеров с количеством каждого размера, цена и фото товара
    """
    size_list = []
    photo = ''
    price = ''
    with Session(engine) as ses:
        for i in ses.query(CatalogAll):
            if good_name in i.name:
                photo = i.photo
                price = i.price
                size_list.append(f'{str(i.size)} - {str(i.quantity)}пар., ')
        list_size_str = f'В наличии есть размеры: {" ".join(size_list)}'
    return list_size_str, photo, price


def update_user_visits(user_nickname):
    with Session(engine) as ses:
        user = ses.query(Users).filter_by(user_name=user_nickname).first()
        if user is None:
            user = Users(user_name=user_nickname, number_of_visits=1)
        else:
            user.number_of_visits += 1

        ses.add(user)
        ses.commit()


def update_all_tables(list_table):
   with Session(engine) as ses:
       for i in list_table:
           ses.query(i).delete()
       ses.commit()
       check_table(list_table)


table_name_list = [AllData, CatalogAll, Catalog]
check_table(table_name_list)
