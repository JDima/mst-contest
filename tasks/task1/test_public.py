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
        name='base1',
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
    Case(
        name='base2',
        n=1,
        g=2,
        s=1,
        roads=[
            [1, 1, 10, 15],
        ],
        answer=0,
    ),
    Case(
        name='base3',
        n=4,
        g=1,
        s=1,
        roads=[
            [1, 2, 20, 100],
            [1, 2, 30, 40],
            [1, 3, 25, 23],
            [1, 3, 1, 30],
            [2, 4, 1, 20]
        ],
        answer=70,
    ),
    Case(
        name='base4',
        n=5,
        g=2,
        s=1,
        roads=[
            [1, 2, 5, 10],
            [2, 3, 5, 10],
            [3, 4, 5, 10],
            [4, 5, 20, 30],
            [5, 2, 5, 10],
        ],
        answer=20,
    ),
    Case(
        name='base5',
        n=5,
        g=1,
        s=1,
        roads=[
            [1, 3, 5, 7],
            [3, 4, 1, 3],
            [3, 4, 7, 0],
            [2, 3, 5, 6],
            [2, 4, 2, 5],
            [1, 2, 4, 3],
            [5, 4, 7, 8],
            [1, 5, 10, 12]
        ],
        answer=15,
    ),
    Case(
        name='base6',
        n=5,
        g=5,
        s=9,
        roads=[
            [3, 4, 5, 10],
            [4, 5, 20, 30],
            [5, 2, 5, 10],
            [1, 3, 5, 7],
            [3, 4, 1, 3],
            [3, 4, 7, 0],
            [2, 3, 5, 6],
            [2, 4, 2, 5],
            [1, 2, 20, 100],
            [1, 2, 30, 40],
            [1, 3, 25, 23],
            [1, 2, 4, 3],
            [5, 4, 7, 8],
            [1, 5, 10, 12]
        ],
        answer=107,
    )
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
