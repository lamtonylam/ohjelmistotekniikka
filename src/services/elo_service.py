from entities.user import User

from repositories.user_repository import user_repository as default_user_repository


class UsernameExistsError(Exception):
    pass


class EloService:

    def __init__(self, user_repostory=default_user_repository):
        self._user_repository = user_repostory

    def create_user(self, name):
        print("nimiii", name)
        existing_user = self._user_repository.find_user_by_username(name)

        if existing_user:
            raise UsernameExistsError(f"Username {name} already exists")

        user = self._user_repository.create_user(User(name))

        return user
