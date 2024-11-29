from domain.user.user_entity import User
from uuid import UUID
from domain.user.user_repository_interface import UserRepositoryInterface


class InMemoryUserRepository(UserRepositoryInterface):

  def __init__(self):
    self.users: list[User] = []
  
  def save(self, user: User) -> None:
    return self.users.append(user)
  
  def get_user_by_id(self, user_id: UUID) -> User:
    for user in self.users:
      if user.id == user_id:
        return user
    return None
  
  def update(self, user: User) -> None:
    for i, existing_user in enumerate(self.users):
      if existing_user.id == user.id:
        self.users[i] = user
        return
