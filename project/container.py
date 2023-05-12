from project.dao.director import DirectorsDAO
from project.dao.genre import GenresDAO
from project.dao.movie import MoviesDAO
from project.dao.user import UserDAO
from project.services import GenresService
from project.services.auth_service import AuthService
from project.services.directors_service import DirectorsService
from project.services.movies_service import MoviesService
from project.services.user_service import UserService
from project.setup.db import db

# DAO
movie_dao = MoviesDAO(db.session)
director_dao = DirectorsDAO(db.session)
genre_dao = GenresDAO(db.session)
user_dao = UserDAO(db.session)

# Services
movie_service = MoviesService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
genre_service = GenresService(dao=genre_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)
