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
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    answer = task4(
        n=case.n,
        qualifications=case.qualifications,
        statements=case.statements,
    )
    assert answer == case.answer
