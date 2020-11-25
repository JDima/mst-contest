import pytest

from .task import task1


class Case:
    def __init__(self, name: str, n: int, g: int, s: int, roads: list,
                 answer: int):
        self._name = name
        self.n = n
        self.g = g
        self.s = s
        self.roads = roads
        self.answer = answer

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=3,
        g=2,
        s=1,
        roads=[
            [1, 2, 10, 15],
            [1, 2, 4, 20],
            [1, 3, 5, 1],
        ],
        answer=30,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = task1(
        n=case.n,
        g=case.g,
        s=case.s,
        roads=case.roads,
    )
    assert answer == case.answer
