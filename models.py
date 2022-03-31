from sqlalchemy import Column, Integer, String, create_engine, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

db = create_engine('sqlite:///db.sqlite')
Base = declarative_base()


class Clients(Base):
    __tablename__ = 'Clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    is_vip = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, is_vip: {self.is_vip}"


class Drivers(Base):
    __tablename__ = 'Drivers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    car = Column(String(25), nullable=False)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, car: {self.car}"


class Orders(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Идентификатор")
    client_id = Column(String, ForeignKey('Clients.id'), comment="Клиент")
    driver_id = Column(String, ForeignKey('Drivers.id'), comment="Водитель")
    clients = relationship("Clients", foreign_keys=[client_id])
    drivers = relationship("Drivers", foreign_keys=[driver_id])
    address_from = Column(String(50), unique=True, comment="Откуда")
    address_to = Column(String(50), comment="Куда")
    date_created = Column(DateTime, comment="Дата создания")
    status = Column(String(25), comment="Статус")

    def __repr__(self):
        return f"id: {self.id}, client_id: {self.client_id}, driver_id: {self.driver_id}, " \
               f"address_from: {self.address_from}, address_to: {self.address_to}, date_created: {self.date_created}," \
               f" status: {self.status}"
