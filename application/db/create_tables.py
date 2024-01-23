import application.db as db

from application.db.tables import Product


def run():
    pass


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()
