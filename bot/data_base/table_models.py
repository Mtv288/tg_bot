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


class MenShoes(Base):
    __tablename__ = 'men_shoes'

    id: Mapped[int] = mapped_column(primary_key=True)
    group_code: Mapped[int]
    code: Mapped[int]
    name: Mapped[str]
    photo: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
    size: Mapped[int]


class WomenShoes(Base):
    __tablename__ = 'women_shoes'

    id: Mapped[int] = mapped_column(primary_key=True)
    group_code: Mapped[int]
    code: Mapped[int]
    name: Mapped[str]
    photo: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
    size: Mapped[int]


class ChildrenShoes(Base):
    __tablename__ = 'children_shoes'

    id: Mapped[int] = mapped_column(primary_key=True)
    group_code: Mapped[int]
    code: Mapped[int]
    name: Mapped[str]
    photo: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
    size: Mapped[int]


class MenSlippers(Base):
    __tablename__ = 'men_slippers'

    id: Mapped[int] = mapped_column(primary_key=True)
    group_code: Mapped[int]
    code: Mapped[int]
    name: Mapped[str]
    photo: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
    size: Mapped[int]


class WomenSlippers(Base):
    __tablename__ = 'women_slippers'

    id: Mapped[int] = mapped_column(primary_key=True)
    group_code: Mapped[int]
    code: Mapped[int]
    name: Mapped[str]
    photo: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
    size: Mapped[int]


class Catalog(Base):
    __tablename__ = 'catalog'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    photo: Mapped[Optional[str]]

class Cat(Base):
    __tablename__ = 'cat'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    photo: Mapped[Optional[str]]