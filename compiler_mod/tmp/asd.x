src/pack/ast/lambda_ast.py.bak:18:            return self.body_lambda.eval(lambda_env)[0]
src/pack/ast/lambda_ast.py.bak:30:            if len(self.id)==0:
src/pack/ast/lambda_ast.py.bak:31:                env_tmp[self.id], env_delme = val[0].eval(env)
src/pack/ast/lambda_ast.py.bak:43:        if len(self.x) != 0:
src/pack/ast/lambda_ast.py.bak:79:                env_closure[self.ids[i].eval(env_closure)[0]] = vals[i]
src/pack/ast/lambda_ast.py.bak:87:        #         env_tmp[id], env_delme = val[0].eval(env)
src/pack/ast/lambda_ast.py.bak:88:        #     env_tmp[self.id], env_delme = val[0].eval(env)
src/pack/ast/lambda_ast.py.bak:99:        #     return env_tmp[vals[1].eval(env_tmp)[0]]
src/pack/ast/types_ast.py:38:        array_list =[self.array_list[i].eval(env)[0] for i in range(len(self.array_list))]
src/pack/ast/types_ast.py:48:        # array_list =[self.array_name[i].eval(env)[0] for i in range(len(self.array_name))]
src/pack/ast/types_ast.py:58:    return l[0]
src/pack/ast/types_ast.py:65:    return None if a==None or len(a)==0 else (a[0], ListExpression(a[1:]))
src/pack/ast/types_ast.py:73:            return (self.lst[0].eval(env)[0],
src/pack/ast/types_ast.py:74:                    self.lst[1].eval(env)[0]),env
src/pack/ast/arith_ast.py:9:        # env["asd"] = 0
src/pack/ast/arith_ast.py:72:        case "+"   : p[0] = PlusExpression(p[1],p[3]) 
src/pack/ast/arith_ast.py:73:        case "-"   : p[0] = MinusExpression(p[1],p[3]) 
src/pack/ast/arith_ast.py:74:        case "*"   : p[0] = TimesExpression(p[1],p[3]) 
src/pack/ast/arith_ast.py:75:        case "/"   : p[0] = DivideExpression(p[1],p[3]) 
src/pack/ast/arith_ast.py:77:    return p[0]
src/pack/ast/lambda_ast.py:15:            return self.body_lambda.eval(lambda_env)[0]
src/pack/ast/lambda_ast.py:27:            if len(self.id)!=0:
src/pack/ast/lambda_ast.py:28:                lambda_env[self.id], env_delme = val[0].eval(env)
src/pack/ast/lambda_ast.py:30:            return self.body_lambda.eval(lambda_env)[0]
src/pack/ast/lambda_ast.py:41:        if len(self.x) != 0:
src/pack/ast/lambda_ast.py:75:#                 env_closure[self.ids[i].eval(env_closure)[0]] = vals[i]
src/pack/ast/lambda_ast.py:83:#         #         env_tmp[id], env_delme = val[0].eval(env)
src/pack/ast/lambda_ast.py:84:#         #     env_tmp[self.id], env_delme = val[0].eval(env)
src/pack/ast/lambda_ast.py:95:#         #     return env_tmp[vals[1].eval(env_tmp)[0]]
src/pack/ast/var_ast.py:5:#     p[0] = generator_var.ReadIdExpression(p[1])
src/pack/ast/var_ast.py:9:#     p[0] = generator_var.WriteIdExpression(p[1],p[3])
src/pack/ast/bool_ast.py:145:        case "and"      : p[0] = AndExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:146:        case "eqcomp"   : p[0] = EqCompExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:147:        case "="       : p[0] = EqExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:148:        case ">="       : p[0] = GeExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:149:        case ">"       : p[0] = GtExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:150:        case "<="       : p[0] = LeExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:151:        case "!="       : p[0] = NotEqCompExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:152:        case "<"       : p[0] = LtExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:153:        case "not"      : p[0] = NotEqCompExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:154:        case "or"       : p[0] = OrExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:155:        case "nand"     : p[0] = NandExpression(p[1],p[3]) 
src/pack/ast/bool_ast.py:157:    return p[0]
src/pack/ast/bool_ast.py:162:        case "not" : p[0] = NotBoolExpression(p[2])
src/pack/ast/bool_ast.py:164:    return p[0]
src/pack/ast/bool_ast.py:169:        case "true" | "false"   : p[0] = BoolValueExpression(p[1])
src/pack/ast/bool_ast.py:170:    return p[0]
