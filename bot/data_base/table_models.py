from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class AllData(Base):
    __tablename__ = 'new'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(default=0)
    name: Mapped[str] = mapped_column(default='0')
    photo: Mapped[str] = mapped_column(default='0')
    price: Mapped[int] = mapped_column(default=0)
    quantity: Mapped[int] = mapped_column(default=0)
    size: Mapped[int] = mapped_column(default=0)



