from stack import Stack

OPEN_BRACKETS = ('(', '{', '[')
CLOSE_BRACKETS = (')', '}', ']')
SQUARE_BRACKETS = ('[', ']')
PARENTHESES = ('(', ')')
FIGURE_BRACKETS = ('{', '}')


def is_opener(value: str) -> bool:
    return value in OPEN_BRACKETS


def is_closer(value: str) -> bool:
    return value in CLOSE_BRACKETS


def is_pair_brackets(value1: str, value2: str) -> bool:
    return (
            (value1 in SQUARE_BRACKETS and value2 in SQUARE_BRACKETS) or
            (value1 in PARENTHESES and value2 in PARENTHESES) or
            (value1 in FIGURE_BRACKETS and value2 in FIGURE_BRACKETS)
    )


def first_decision(string):
    stack = Stack()

    if len(string) % 2:
        return 'Несбалансированно'

    for letter in string:
        if is_opener(letter):
            stack.push(letter)
        if is_closer(letter):
            if stack.is_empty():
                return 'Несбалансированно'
            elif is_pair_brackets(letter, stack.pop()):
                continue
            else:
                return 'Несбалансированно'

    return 'Сбалансированно'



if __name__ == '__main__':
    print(first_decision('(((([{}]))))'))
    print(first_decision('[([])((([[[]]])))]{()}'))
    print(first_decision('{{[()]}}'))
    print(first_decision('}{}'))
    print(first_decision('{{[(])]}}'))
    print(first_decision('[[{())}]'))