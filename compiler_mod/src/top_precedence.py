
precedence = [
    ['right', 'assign'],
    ['right', 'lambda'],
    ['left', ','],
    ['nonassoc', 'then'],
    ['nonassoc', 'else', 'do'],
    ['left', 'or'],
    ['left', 'and', 'nand'],
    ['left', '=', 'neqs', 'eq'],
    ['left', '<', '>', 'le', 'ge'],
    ['left', '+', '-'],
    ['left', '*', '/'],
    ['right', 'not', 'UMINUS'],
    # ['right', '[',']'],
    ['right', '('],
    ['left', ')'],
]
