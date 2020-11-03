# shabti/tests/test_result_set.py
import pytest
from collections.abc import Iterable

from shabti import ResultSet
from shabti import ResourceObject


def test_new_result_set(query_results_string):
    res = ResultSet('patrons', query_results_string)

    assert isinstance(res, ResultSet)
    assert res.total == 3
    assert res.start == 0
    assert isinstance(res.entries, list)

    assert len(res) == 3
    assert isinstance(res, Iterable)
    assert isinstance(res[0], ResourceObject)


@pytest.mark.vcr()
def test_result_set_info(query_results_string, patron_keys):
    res = ResultSet('patrons', query_results_string)

    assert res._list() == ['1401559', '1401560', '1401561']

    info_results = res.info()

    assert set(patron_keys).issubset(info_results[0])
    assert info_results[0]['id'] == 1401559
    assert info_results[0]['birthDate'] == "1963-07-02"


@pytest.mark.vcr()
def test_result_set_info_with_fields(query_results_string, custom_patron_keys):
    res = ResultSet('patrons', query_results_string)

    info_results = res.info(fields=",".join(custom_patron_keys))

    assert set(custom_patron_keys).issubset(info_results[0])
    assert info_results[0]['names'] == ["Worthington III, Warren Kenneth"]
