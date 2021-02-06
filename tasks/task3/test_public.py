import pytest

from .task import task3


class Case:
    def __init__(self, name: str, n: int, set_t: list, set_k: list,
                 set_m: list, answer: tuple):
        self._name = name
        self.n = n
        self.set_t = set_t
        self.set_k = set_k
        self.set_m = set_m
        self.answer = answer

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=5,
        set_t=[
            [1, 2, 5],
            [1, 3, 5],
            [1, 4, 5],
            [1, 5, 5],
        ],
        set_k=[
            [2, 3, 2],
        ],
        set_m=[
            [1, 2, 5],
            [1, 3, 5],
            [1, 4, 5],
            [1, 5, 5],
            [3, 4, 8],
            [4, 5, 8],
        ],
        answer=(20, 17),
    ),
    Case(
        name='base2',
        n=4,
        set_t=[
            [1, 2, 3],
            [1, 3, 2],
            [2, 4, 2]
        ],
        set_k=[
            [2, 3, 1],
        ],
        set_m=[
            [1, 2, 3],
            [1, 3, 2],
            [2, 4, 2],
            [1, 4, 5]
        ],
        answer=(7, 5),
    ),
    Case(
        name='base3',
        n=4,
        set_t=[
            [1, 2, 3],
            [1, 3, 2],
            [2, 4, 2]
        ],
        set_k=[
            [1, 2, 2],
        ],
        set_m=[
            [1, 2, 3],
            [1, 3, 2],
            [2, 4, 2],
            [1, 4, 5]
        ],
        answer=(7, 6),
    ),
    Case(
        name='base4',
        n=5,
        set_t=[
            [1, 3, 1],
            [3, 2, 1],
            [3, 5, 1],
            [2, 4, 1]
        ],
        set_k=[
            [5, 4, 1],
            [1, 2, 2]
        ],
        set_m=[
            [1, 3, 1],
            [3, 2, 1],
            [3, 5, 1],
            [2, 4, 1],
            [1, 5, 1]
        ],
        answer=(4, 4),
    ),
    Case(
        name='base5',
        n=2,
        set_t=[
            [1, 2, 3],
        ],
        set_k=[
            [1, 2, 2],
        ],
        set_m=[
            [1, 2, 5],
            [1, 2, 3]
        ],
        answer=(3, 2),
    ),
    Case(
        name='base6',
        n=6,
        set_t=[
            [1, 2, 2],
            [2, 3, 6],
            [3, 6, 3],
            [3, 4, 5],
            [4, 5, 4]
        ],
        set_k=[
            [2, 5, 9],
            [3, 5, 3]
        ],
        set_m=[
            [1, 2, 2],
            [1, 6, 8],
            [2, 3, 6],
            [3, 6, 3],
            [3, 4, 5],
            [4, 5, 4],
            [6, 4, 10]
        ],
        answer=(20, 18),
    ),
    Case(
        name='base7',
        n=6,
        set_t=[
            [1, 2, 2],
            [2, 3, 6],
            [3, 6, 3],
            [3, 4, 5],
            [4, 5, 4]
        ],
        set_k=[
            [2, 5, 9],
            [3, 5, 10]
        ],
        set_m=[
            [1, 2, 2],
            [1, 6, 8],
            [2, 3, 6],
            [3, 6, 3],
            [3, 4, 5],
            [4, 5, 4],
            [6, 4, 10]
        ],
        answer=(20, 20),
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = task3(
        n=case.n,
        set_t=case.set_t,
        set_m=case.set_m,
        set_k=case.set_k,
    )
    assert answer == case.answer
