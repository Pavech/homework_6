from models import Base, Drivers, Clients, db, Orders
from flask import Flask, request
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

app = Flask(__name__)
Base.metadata.create_all(db)
Session = scoped_session(sessionmaker(autoflush=True, autocommit=False, bind=db))


@contextmanager
def session_scope():
    """Создание сессий."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


@app.route('/drivers', methods=['GET', "POST", 'DELETE'])
def get_drivers():
    if request.method == 'GET':
        with session_scope() as session:
            req_ = request.args.get("driverId")
            driver_ = session.query(Drivers).filter(Drivers.id == int(req_)).all()
            return f'Список водителей {driver_}'
    if request.method == 'POST':
        with session_scope() as session:
            req_ = request.get_json()
            new_data = Drivers(name=req_['name'], car=req_['car'])
            session.add(new_data)
            return 'Done'
    if request.method == 'DELETE':
        with session_scope() as session:
            req_ = request.args.get("driverId")
            session.query(Drivers).filter(Drivers.id == int(req_)).delete()
            return f'Водитель был удален'
    else:
        return "fail"


@app.route('/clients', methods=['GET', "POST", 'DELETE'])
def get_clients():
    if request.method == 'GET':
        with session_scope() as session:
            req_ = request.args.get("clientId")
            client_ = session.query(Clients).filter(Clients.id == int(req_)).all()
            return f'Список клиентов {client_}'
    if request.method == 'POST':
        with session_scope() as session:
            req_ = request.get_json()
            new_data = Clients(name=req_["name"], is_vip=req_["is_vip"])
            session.add(new_data)
            return 'Done'
    if request.method == 'DELETE':
        with session_scope() as session:
            req_ = request.args.get("clientId")
            session.query(Clients).filter(Clients.id == int(req_)).delete()
            return f'Клиент был удален'
    else:
        return "fail"


@app.route('/orders', methods=['GET', "POST", 'PUT'])
def get_orders():
    if request.method == 'GET':
        with session_scope() as session:
            req_ = request.args.get("orderId")
            order_ = session.query(Orders).filter(Orders.id == int(req_)).all()
            return f'Список заказов {order_}'
    if request.method == 'POST':
        req_ = request.get_json()
        with session_scope() as session:
            new_data = Orders(address_from=req_['address_from'], caaddress_tor=req_['address_to'],
                              cadate_createdr=req_['date_created'], status=req_['status'],
                              clients=req_['clients'], drivers=req_['drivers'])
            session.add(new_data)
            return 'Done'
    if request.method == 'PUT':
        with session_scope() as session:
            ...


app.run(host='0.0.0.0', port=5000)
