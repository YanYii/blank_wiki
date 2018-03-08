from wiki import app
from app import db
from app.models import Post


def create_table():
    with app.app_context():
        db.create_all()
        print('create db done.')


def delete_table():
    with app.app_context():
        db.delete_all()
        print('delete db done.')


def test():
    create_table()


if __name__ == '__main__':
    test()
