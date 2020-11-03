# shabti/tests/test_result_set.py
import pytest
from collections.abc import Iterable

from shabti import ResultSet
from shabti import ResourceObject


def test_new_result_set(query_results_string):
    res = ResultSet('patron', query_results_string)

    assert isinstance(res, ResultSet)
    assert res.total == 3
    assert res.start == 0
    assert isinstance(res.entries, list)

    assert len(res) == 3
    assert isinstance(res, Iterable)
    assert isinstance(res[0], ResourceObject)
