from sqlalchemy import String, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(primary_key=True)
    symbol: Mapped[str] = mapped_column(String, unique=True, index=True)
    name: Mapped[str] = mapped_column(String)
    asset_type: Mapped[str] = mapped_column(String)

    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="asset"
    )


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    asset_id: Mapped[int] = mapped_column(ForeignKey("assets.id"))
    date: Mapped[Date] = mapped_column(Date)
    quantity: Mapped[float] = mapped_column(Float)
    price: Mapped[float] = mapped_column(Float)
    type: Mapped[str] = mapped_column(String)

    asset: Mapped["Asset"] = relationship(back_populates="transactions")