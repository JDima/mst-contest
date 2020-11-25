import pytest

from .task import task2


class Case:
    def __init__(self, name: str, n: int, freckles: list, answer: float):
        self._name = name
        self.n = n
        self.freckles = freckles
        self.answer = answer

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=3,
        freckles=[
            [1.0, 1.0],
            [2.0, 2.0],
            [2.0, 4.0],
        ],
        answer=3.41,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = task2(
        n=case.n,
        freckles=case.freckles,
    )
    assert answer == case.answer
