class Select():
    def __init__(self, table, *fields):
        fields_str = ', '.join(fields)
        self._condition = None
        self._select_string = f'SELECT {fields_str} FROM {table}'

    def where(self, condition):
        if not isinstance(condition, BaseCondition):
            raise ValueError('Must provide BaseCondition instance')
        self._condition = condition

    def __str__(self):
        return f'{self._select_string} {self._condition}'

class BaseCondition():
    def __init__(self):
        self._string = None

    def __str__(self):
        return self._string


class BaseFieldCondition(BaseCondition):
    operations = []

    def __init__(self, operation, value):
        field_str = type(self).__name__.lower()
        if operation not in self.operations:
            raise ValueError('Provided operation must be in list of valid'
                             'operations of the class')
        self._string = f'{field_str} {operation} {value}'


class Id(BaseFieldCondition):
    operations = ['<', '>', '=', 'IN', 'NOTIN']

class Url(BaseFieldCondition):
    operations = ['=']

class Date(BaseFieldCondition):
    operations = ['<', '>', '=']

class Rating(BaseFieldCondition):
    operations = ['<', '>', '=']

class BaseConditionOperator(BaseCondition):
    def __init__(self, *conditions):
        if not len(conditions):
            raise ValueError('At least one BaseCondition must be provided')

        if not all(isinstance(c, BaseCondition) for c in conditions):
            raise ValueError('Arguments must be instances of BaseCondition')


class And(BaseConditionOperator):
    def __init__(self, *conditions):
        self._string = ' AND '.join(map(str, conditions))

class Or(BaseConditionOperator):
    def __init__(self, *conditions):
        cond_str = ' OR '.join(map(str, conditions))
        self._string = f'({cond_str})'

