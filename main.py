from stack import Stack

OPEN_BRACKETS = '({['
CLOSE_BRACKETS = ')}]'
PAIRS = {o: c for o, c in zip(CLOSE_BRACKETS, OPEN_BRACKETS)}


def is_opening(value: str) -> bool:
    return value in OPEN_BRACKETS


def is_closing(value: str) -> bool:
    return value in CLOSE_BRACKETS


def is_pair_brackets(value1: str, value2: str) -> bool:
    return value2 != PAIRS[value1]


def first_decision(string):
    stack = Stack()

    if len(string) % 2:
        return 'Несбалансированно'

    for letter in string:
        if is_opening(letter):
            stack.push(letter)
        elif is_closing(letter):
            if stack.is_empty() or is_pair_brackets(letter, stack.pop()):
                return 'Несбалансированно'

    return 'Сбалансированно'


if __name__ == '__main__':
    print(first_decision('(((([{}]))))'))
    print(first_decision('[([])((([[[]]])))]{()}'))
    print(first_decision('{{[()]}}'))
    print(first_decision('}{}'))
    print(first_decision('{{[(])]}}'))
    print(first_decision('[[{())}]'))
