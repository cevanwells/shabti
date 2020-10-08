# shabti/tests/test_querystring.py
import json
from pytest import fixture

from shabti import QueryString


@fixture
def single_operand():
    return ['patron', 'b', 'equals', '1234567890']


@fixture
def double_operand():
    return ['patron', 'b', 'between', ['1234567890', '1234567899']]


def test__repr__(single_operand):
    query = QueryString(*single_operand)
    response = query.__repr__()

    assert response == '<QueryString [{}]>'.format(query.type)


def test__str__(single_operand):
    query = QueryString(*single_operand)
    response = query.__str__()

    assert isinstance(response, str)


def test_querystring_single_operand(single_operand):
    query = QueryString(*single_operand)

    assert query.type == 'patron'
    assert query.tag == 'b'
    assert query.operation == 'equals'
    assert query.operands == ['1234567890', '']


def test_querystring_double_operand(double_operand):
    query = QueryString(*double_operand)

    assert query.type == 'patron'
    assert query.tag == 'b'
    assert query.operation == 'between'
    assert query.operands == ['1234567890', '1234567899']


def test_querystring_single_operand_to_json(single_operand):
    query = QueryString(*single_operand)
    response = json.loads(query.to_json())

    assert isinstance(response, dict)
    assert response['target']['record']['type'] == 'patron'
    assert response['target']['field']['tag'] == 'b'
    assert response['expr']['op'] == 'equals'
    assert response['expr']['operands'] == ["1234567890", ""]


def test_querystring_double_operand_to_json(double_operand):
    query = QueryString(*double_operand)
    response = json.loads(query.to_json())

    assert isinstance(response, dict)
    assert response['target']['record']['type'] == 'patron'
    assert response['target']['field']['tag'] == 'b'
    assert response['expr']['op'] == 'between'
    assert response['expr']['operands'] == ["1234567890", "1234567899"]
