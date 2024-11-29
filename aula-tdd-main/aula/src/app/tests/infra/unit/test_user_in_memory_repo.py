from domain.user.user_entity import User
from infra.user.in_memory_user_repo import InMemoryUserRepository
from uuid import uuid4


class TestSaveUser:
  
  def test_can_save_user(self):
    '''
    Test if it is possible to save users in the repository
    '''
    repository = InMemoryUserRepository()
    user1 = User(id=uuid4(), name="John Doe")
    user2 = User(id=uuid4(), name="Mary Doe")

    repository.save(user1)
    repository.save(user2)

    assert len(repository.users) == 2
    assert repository.users[0] == user1
    assert repository.users[1] == user2



class TestGetUserById:
  '''
  Test if it is possible to return an user by ID
  '''
  def test_can_get_user_by_id(self):
    repository = InMemoryUserRepository()
    user1 = User(id=uuid4(), name="John Doe")
    user2 = User(id=uuid4(), name="Mary Doe")

    repository.save(user1)
    repository.save(user2)

    user = repository.get_user_by_id(user1.id)

    assert user == user1

  def test_when_user_does_not_exists_should_return_none(self) -> None:
    repository = InMemoryUserRepository()
    user1 = User(id=uuid4(), name="John Doe")
    user2 = User(id=uuid4(), name="Mary Doe")

    repository.save(user1)
    repository.save(user2)

    user = repository.get_user_by_id(user_id=uuid4())

    assert user == None



class TestUpdateUser:
  '''
  Test if it is possible updating the user name
  '''
  def test_can_update_user_name(self):
    repository = InMemoryUserRepository()
    user1 = User(id=uuid4(), name="John Doe")
    user2 = User(id=uuid4(), name="Mary Doe")

    repository.save(user1)
    repository.save(user2)

    updated_user = User(id=user1.id, name="Harry Potter")
    repository.update(updated_user)

    retrieved_user = repository.get_user_by_id(user_id=user1.id)
    assert retrieved_user.name == "Harry Potter"

