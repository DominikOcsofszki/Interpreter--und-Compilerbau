code/lambda.tx:11:fn:= x -> x + y;
code/lambda.tx:12:# fn2:= (x,y) -> x*y;
code/lambda.tx:25:# f:= asd -> asd * 11;
code/lambda.tx:26:# f2:= asd -> asd * 11;
code/lambda.tx:31:# fac := x->x*2;
code/lambda.tx:6:lam:= x -> 5*x;
code/lambda_args.tx:3:f:= -> 100;
code/lambda_args.tx:6:fn:= x -> x ;
code/lambda_args.tx:9:fn2:= (x,y,z) -> x + y * z;
code/lambda_args2.tx:3:fnprint:=(x,y) -> {
code/lambda_args2.tx:8:# asd -> {} c
code/lambda_no_args.tx:5:fn:=  -> 2111*x;
code/local_letrec.tx:10:fun_from_local:=local fac := x -> if x=0 then 1 else x*fac(x-1) in fac;
code/local_letrec.tx:11:# local fac := x -> if x=0 then 1 else x*fac(x-1) in fac(3)
code/local_letrec.tx:4:# local fac:= x -> if x=0 then 1 else x * fac(x-1) in fac;
code/local_letrec.tx:6:# local sqrt:= x->x*x in sqrt(5);
code/local_letrec.tx:8:# local ok:= x->x*x in ok(1000);
code/local_works.tx:4:# local fac:= x -> if x=0 then 1 else x * fac(x-1) in fac;
code/local_works.tx:6:s:=local sqrt:= x->x*x in sqrt;
code/new_lambda.tx:3:l0:= /->99;
code/new_lambda.tx:4:l1:= /x->x;
code/new_lambda.tx:5:l2:= /x,y->x+y;
code/structs_fn.tx:5:    f:= -> 11;
code/structs_fn.tx:6:    f1:= x -> x*1;
code/structs_fn.tx:7:    f2:= (x,y) -> x*1*y;
code/structs_test_class.tx:14:f:= x -> x*3;
code/structs_test_class.tx:15:# f2:= y -> ..a*y
code/structs_test_class.tx:16:f2:= y -> 99
code/structs_test_class.tx:4:f:= x -> x*1
code/structs_test_class.tx:9:f:= x -> x*2
code/types.tx:15:head:= /l -> l[0];
code/types.tx:16:tail:= /l -> l[1];
code/types.tx:17:getIndexItem:= /l -> print(tail);
