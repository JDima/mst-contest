import pytest

from .task import task4


class Case:
    def __init__(self, name: str, n: int, qualifications: list,
                 statements: list, answer: int):
        self._name = name
        self.n = n
        self.qualifications = qualifications
        self.statements = statements
        self.answer = answer

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=4,
        qualifications=[7, 2, 3, 1],
        statements=[
            [1, 2, 5],
            [2, 4, 1],
            [3, 4, 1],
            [1, 3, 5],
        ],
        answer=11,
    ),
    Case(
        name='base2',
        n=3,
        qualifications=[1, 2, 3],
        statements=[
            [3, 1, 2],
            [3, 1, 3],
        ],
        answer=-1,
    ),
    Case(
        name='base3',
        n=2,
        qualifications=[5, 1],
        statements=[
            [1, 2, 5]
        ],
        answer=5,
    ),
    Case(
        name='base4',
        n=8,
        qualifications=[10, 9, 8, 7, 8, 8, 8, 8],
        statements=[
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5],
            [5, 4, 10],
            [6, 4, 20],
            [7, 4, 3000],
            [8, 4, 400],
        ],
        answer=-1,
    ),
    Case(
        name='base5',
        n=7,
        qualifications=[2, 1, 1, 2, 1, 1, 3],
        statements=[
            [1, 2, 3],
            [1, 3, 3],
            [4, 5, 2],
            [4, 6, 2],
            [7, 4, 2],
            [7, 1, 3]
        ],
        answer=15,
    ),
    Case(
        name='base6',
        n=1,
        qualifications=[1],
        statements=[],
        answer=0
    ),
    Case(
        name='base7',
        n=6,
        qualifications=[5, 4, 1, 10, 7, 3],
        statements=[
            [2, 3, 3],
            [2, 3, 10],
            [1, 2, 4],
            [1, 3, 2],
            [4, 1, 6],
            [4, 2, 7],
            [4, 5, 1],
            [5, 2, 10],
            [5, 6, 5],
            [6, 3, 3],
            [5, 2, 0]
        ],
        answer=14,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    answer = task4(
        n=case.n,
        qualifications=case.qualifications,
        statements=case.statements,
    )
    assert answer == case.answer
