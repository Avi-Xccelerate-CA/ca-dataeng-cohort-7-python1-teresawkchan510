from week0 import dose
import pytest

testdata =[
    ([500, 1, 0, 0, 0], "No medicine given"),
    ([499, 1, 0, 0, 0], "No medicine given"),
    ([251, 10, 20, 30, 40], "No medicine given"),
	([100,200,100,100,1,0], "No medicine given")
]

@pytest.mark.parametrize("case, expected", testdata)
def test_ex3(case, expected):
	assert dose(case) == expected
