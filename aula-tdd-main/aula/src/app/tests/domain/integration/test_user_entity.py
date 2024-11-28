from domain.user.user_entity import User
from domain.task.test_entity import Task
from uuid import uuid4


class TestUserWithTask:

    def test_collect_tasks(self):
        user = User(id=uuid4(), name="Test User")
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 1",
            description="Description 1",
            completed=False,
        )
        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 2",
            description="Description 2",
            completed=True,
        )

        user.collect_tasks([task1, task2])
        assert len(user.tasks) == 2
        assert task1 in user.tasks
        assert task2 in user.tasks


    def test_count_pending_tasks(self):
        user = User(id=uuid4(), name="John Doe")
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 1",
            description="Description 1",
            completed=False,
        )
        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 2",
            description="Description 2",
            completed=False,
        )
        task3 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 3",
            description="Description 3",
            completed=False
        )

        user.collect_tasks([task1, task2, task3])
        pending_count = user.count_pending_tasks()
        assert pending_count == 3

    def test_count_pending_tasks_list_empty(self):
        user = User(id=uuid4(), name="John Doe")
        count_pendint_tasks = user.count_pending_tasks()

        assert count_pendint_tasks == 0

    def test_all_tasks_completed(self):
        user = User(id=uuid4(), name="John Doe")
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 1",
            description="Description 1",
            completed=False,
        )
        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 2",
            description="Description 2",
            completed=False,
        )

        user.collect_tasks([task1, task2])
        user.tasks[0].mark_as_completed()
        user.tasks[1].mark_as_completed()
        task2.mark_as_completed()

        count_pending_tasks = user.count_pending_tasks()

        assert count_pending_tasks == 0
