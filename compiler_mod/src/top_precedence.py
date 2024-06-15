
precedence = [
    ['right', 'assign'],
    ['right', 'lambda'],
    # ['right', 'dot'],
    ['left', ','],
    ['nonassoc', 'then'],
    ['nonassoc', 'else', 'do'],
    ['left', 'or'],
    ['left', 'and', 'nand'],
    ['left', '=', 'neqs', 'eq'],
    ['left', '<', '>', 'le', 'ge'],
    ['left', '+', '-'],
    ['left', '*', '/'],
    ['right', '(','['],
    ['left', ')',']'],
    ['right', 'not', 'UMINUS'],
]
