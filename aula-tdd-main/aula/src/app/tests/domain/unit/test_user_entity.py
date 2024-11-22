import pytest # type: ignore
from uuid import uuid4
from domain.user.user_entity import User

class TestUser:

    def test_user_initialization(self):
        user_id = uuid4()
        user_name = "John Doe"
        user = User(id=user_id, name=user_name)

        assert user.id == user_id
        assert user.name == user_name

    def test_user_id_validation(self):
        with pytest.raises(Exception, match="id must be an UUID"):
            User(id="invalid_id", name="John Doe")

    def test_user_name_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="name is required"):
            User(id=user_id, name="")