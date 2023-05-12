from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound


class DirectorsService:
    def __init__(self, dao: BaseDAO):
        self.dao = dao

    def get_item(self, pk: int):
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def get_all(self, page: int | None, status=None):
        return self.dao.get_all(page=page, status=status)
