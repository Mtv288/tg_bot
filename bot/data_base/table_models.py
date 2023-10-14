from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String



class Base(DeclarativeBase):
    pass


class AllData(Base):
    __tablename__ = 'all_goods'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(default=0)
    group_code: Mapped[int]
    name: Mapped[str] = mapped_column(String(25), default='0')
    photo: Mapped[str] = mapped_column(default='0')
    price: Mapped[int] = mapped_column(default=0)
    quantity: Mapped[int] = mapped_column(default=0)
    size: Mapped[int] = mapped_column(default=0)


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


