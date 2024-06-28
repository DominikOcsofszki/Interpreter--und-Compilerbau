
precedence = [
    ['right', 'ASSIGN'],
    # ['right', 'extend'],
    ['right', 'LAMBDA'],
    ['right', 'LOCAL'],
    ['nonassoc', 'THEN',  'DO'],
    ['nonassoc' ,'ELSE'],
    ['left', 'OR'],
    ['left', 'AND', 'NAND'],
    ['left', '=', 'NEQS', 'EQ'],
    ['left', '<', '>', 'LE', 'GE'],
    ['left', '+', '-'],
    ['left', '*', '/'],
    ['right', 'NOT', 'UMINUS'],
]
