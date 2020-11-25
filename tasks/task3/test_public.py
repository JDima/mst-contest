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
        name='base',
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
