from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from typing import Optional


class Base(DeclarativeBase):
    pass


class AllData(Base):
    __tablename__ = 'all_goods'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[Optional[int]]
    group_code: Mapped[int]
    name: Mapped[Optional[str]]
    photo: Mapped[Optional[str]]
    price: Mapped[Optional[int]]
    quantity: Mapped[Optional[int]]
    size: Mapped[Optional[int]]


class CatalogAll(Base):
    __tablename__ = 'catalog_all'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    size: Mapped[int]
    quantity: Mapped[int]
    photo: Mapped[Optional[str]]


class Catalog(Base):
    __tablename__ = 'catalog'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    photo: Mapped[Optional[str]]


class Users(Base):
    __tablename__ = 'quantity_user'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    number_of_visits: Mapped[int]
    message_id: Mapped[int]







