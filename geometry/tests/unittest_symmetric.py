import pytest
import os
import sys

sys.path.append(os.path.dirname(__file__) + '/../')

from symmetric_points import check_line


@pytest.fixture(scope="function", params=[
    ([(2.0, 2.0), (3.0, 7.0), (4.0, 7.0), (5.0, 2.0)], 1,
     True
     ),
    ([(2.0, 2.0), (3.0, 2.0), (4.0, 7.0), (5.0, 7.0)], 1,
     False),
    ([(12.0, 10.0), (13.0, 20.0), (15.0, 7.0), (3.0, 2.0)], 1,
     False
     ),
    ([(12.0, 10.0), (13.0, 20.0), (15.0, 7.0), (3.0, 2.0)], 0,
     False
     ),
    ([(2.0, 10.0), (3.0, 5.0), (2.0, 7.0), (3.0, 2.0)], 0,
     False
     ),
    ([(2.0, 10.0), (3.0, 7.0), (2.0, 6.0), (3.0, 9.0)], 0,
     True
     )
])
def param_test(request):
    return request.param


def test_check_line(param_test):
    data, index, expected_output = param_test
    result = check_line(data, index)
    print("\n ось {0}, input: {0}, output: {1}, expected: {2}".format(index, data, result,
                                                                      expected_output))
    assert result == expected_output



