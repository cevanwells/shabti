# shabti/querystring.py
import json


class QueryString(object):
    query_types = ['bib', 'order', 'item', 'volume',
                   'holding', 'patron', 'resource',
                   'license', 'vendor', 'contact',
                   'invoice', 'authority', 'course',
                   'program', 'section']
    operation_types = ['equals', 'not_equal', 'greater_than',
                       'less_than', 'greater_than_or_equal',
                       'less_than_or_equal', 'has', 'all_fields_not_have',
                       'at_least_one_field_not_have', 'between',
                       'not_within', 'in', 'starts_with', 'ends_with',
                       'exists', 'not_exists', 'today', 'yesterday',
                       'last_week', 'last_month', 'days_ago', 'weeks_ago',
                       'months_ago', 'regex']

    def __init__(self, qtype, tag, operation, ops):
        if qtype not in QueryString.query_types:
            raise QueryStringTypeUnknownError(qtype)

        if operation not in QueryString.operation_types:
            raise QueryStringOperationUnknownError(operation)

        if isinstance(ops, list):
            operands = ops
        elif isinstance(ops, str):
            operands = [ops, '']
        else:
            raise QueryStringOperandsInvalidError(ops)

        self._data = {
            'target': {
                'record': {
                    'type': qtype
                },
                'field': {
                    'tag': tag
                }
            },
            'expr': {
                'op': operation,
                'operands': operands
            }
        }

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return '<QueryString [{}]>'.format(self.type)

    def to_json(self):
        return json.dumps(self._data)

    @property
    def type(self):
        return self._data['target']['record']['type']

    @property
    def tag(self):
        return self._data['target']['field']['tag']

    @property
    def operation(self):
        return self._data['expr']['op']

    @property
    def operands(self):
        return self._data['expr']['operands']


class QueryStringTypeUnknownError(Exception):
    """Exception raised for errors in the input Type.

    Attributes:
        qtype -- input qtype which caused the error
        message -- provided error message
    """
    def __init__(self, qtype, message="Query type is not recognized"):
        self.qtype = qtype
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{} -> {}".format(self.qtype, self.message)


class QueryStringOperationUnknownError(Exception):
    """Exception raised for errors in the input Operation.

    Attributes:
        operation -- input operation which caused the error
        message -- provided error message
    """

    def __init__(self, operation, message="Query operation is not recognized"):
        self.operation = operation
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{} -> {}".format(self.operation, self.message)


class QueryStringOperandsInvalidError(Exception):
    """Exception raised for errors in the input Operands.

    Attributes:
        operands -- input operands which caused the error
        message -- provided error message
    """

    def __init__(self, operands,
                 message="Query operands must be of type list or str"):
        self.operands = operands
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return "{} -> {}".format(self.operands, self.message)
