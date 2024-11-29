from unittest.mock import MagicMock
from uuid import UUID
from domain.user.user_repository_interface import UserRepositoryInterface
import application.user.create_user_use_case as create_user


class TestCreateUser:
  
  def test_create_user_with_valid_data(self):
    mock_repository = MagicMock(UserRepositoryInterface)
    use_case = create_user.CreateUserUseCase(repository=mock_repository)
    request = create_user.CreateUserRequest(name="John Doe")
    response = use_case.execute(request)

    assert response.id is not None
    assert isinstance(response, create_user.CreateUserResponse)
    assert isinstance(response.id, UUID)
    assert mock_repository.save.called is True