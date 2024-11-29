from abc import ABC, abstractmethod
from uuid import UUID
from domain.user.user_entity import User

class UserRepositoryInterface(ABC):
  
  @abstractmethod
  def save(self, user: User) -> None:
    raise NotImplementedError
  
  @abstractmethod
  def get_user_by_id(self, user_id: UUID) -> User:
    raise NotImplementedError 
  
  @abstractmethod
  def update(self, user: User) -> None:
    raise NotImplementedError
