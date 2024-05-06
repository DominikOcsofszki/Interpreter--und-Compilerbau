
# loop expr do expr
# for assign;bool_expr;assign do expr
# for assign;bool_expr;assign do lock var expr << optional
# ===================================================
# if bool_expr then expr
# if bool_expr then expr else expr

reserved_control ={
        "loop":"loop",
        "do":"do",
        "for":"for",
        "if":"if",
        "then":"then",
        "else":"else",
        # "lock":"lock",
        "while":"while",
        }
tokens_control = [] +\
        list(reserved_control.values())
