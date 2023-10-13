from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class AllData(Base):
    __tablename__ = 'new'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int]
    name: Mapped[str]
    photo: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
    size: Mapped[int]

