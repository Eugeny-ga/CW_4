from sqlite3 import IntegrityError

from project.exceptions import UserAlreadyExists
from project.models import User


class UserDAO:

    def __init__(self, db_session):
        self.db_session = db_session

    # def get_one(self, uid):
    #     return self.db_session.query(User).get(uid)
    #
    # def get_all(self):
    #     return self.db_session.query(User).all()

    def get_by_email(self, email):
        return self.db_session.query(User).filter(User.email == email).first()

    def create(self, new_user):
        try:
            data = User(**new_user)

            self.db_session.add(data)
            self.db_session.commit()
        except IntegrityError:
            raise UserAlreadyExists
        return data

    def update(self, user):
        self.db_session.add(user)

        self.db_session.commit()
        self.db_session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self.db_session.delete(user)
        self.db_session.commit()
