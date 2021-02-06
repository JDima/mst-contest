import math
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
        name='base1',
        n=3,
        freckles=[
            [1.0, 1.0],
            [2.0, 2.0],
            [2.0, 4.0],
        ],
        answer=3.41,
    ),
    Case(
        name='base2',
        n=1,
        freckles=[
            [2.0, 1.0]
        ],
        answer=0.0,
    ),
    Case(
        name='base3',
        n=4,
        freckles=[
            [1.0, 1.0],
            [1.0, 1.0],
            [1.0, 1.0],
            [3.0, 1.5]
        ],
        answer=2.06,
    ),
    Case(
        name='base4',
        n=4,
        freckles=[
            [1.0, 1.0],
            [-1.0, -1.0],
            [5.0, 2.0],
            [3.0, 1.5]
        ],
        answer=6.95,
    ),
    Case(
        name='base5',
        n=6,
        freckles=[
            [1.0, 1.0],
            [2.0, 0.0],
            [0.0, 0.0],
            [-1.0, 3.0],
            [5.0, -2.5],
            [2.9, 1.8]
        ],
        answer=11.57,
    ),
    Case(
        name='base6',
        n=5,
        freckles=[
            [0, 0],
            [2, 2],
            [3, 10],
            [5, 2],
            [7, 0]
        ],
        answer=16.72,
    ),
    Case(
        name='base7',
        n=5,
        freckles=[
            [1.0, 1.0],
            [2.0, 2.0],
            [3.0, 3.0],
            [4.0, 4.0],
            [5.0, 5.0],
        ],
        answer=round(math.sqrt(2) * 4, 2),
    ),
    Case(
        name='base8',
        n=6,
        freckles=[
            [1.0, 5.0],
            [3.0, 7.0],
            [5.0, 1.0],
            [5.0, 2.0],
            [2.0, 2.0],
            [7.0, 6.0],
        ],
        answer=14.11,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = task2(
        n=case.n,
        freckles=case.freckles,
    )
    assert answer == case.answer
