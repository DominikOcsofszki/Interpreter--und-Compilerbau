class GeneratorHelper:
    def __init__(self, used_procedures_and_classes,gen):
        self.used_procedures_and_classes = used_procedures_and_classes
        self.gen = gen

    def set_generator_module_and_check(self,module):
        self.gen = module
        self.__check_generator_module()
        self.__generator_module_implements()
        return self.gen

    def __generator_module_implements(self): # check availability of module and all referenced items
        return all(hasattr(self.gen, x) for x in self.used_procedures_and_classes)

    def __check_generator_module(self):
        if not self.gen:
            raise Exception("No code generator provided please use 'set_generator_module()' in parser module")
        if not self.__generator_module_implements() :
            raise Exception("code generator doesn't implement all expected functions")

# class GeneratorHelper2:
#     def __init__(self, used_procedures_and_classes,gen) -> None:
#         self.used_procedures_and_classes = used_procedures_and_classes
#         self.gen = gen
#
#     def set_generator_module_and_check(self,m):
#         self.__set_generator_module(m)
#         # self.gen = m
#         self.__check_generator_module()
#         self.__generator_module_implements()
#         return self.gen
#
#     def __set_generator_module(self,m):
#         self.gen = m
#
#     def __generator_module_implements(self): # check availability of module and all referenced items
#         return all(hasattr(self.gen, x) for x in self.used_procedures_and_classes)
#
#     def __check_generator_module(self):
#         if not self.gen:
#             raise Exception("No code generator provided please use 'set_generator_module()' in parser module")
#         if not self.__generator_module_implements() :
#             raise Exception("code generator doesn't implement all expected functions")
#
#
#     # def generator_module_implements(self,used_procedures_and_classes): # check availability of module and all referenced items
#     #     return all(hasattr(self.gen, x) for x in used_procedures_and_classes)
#
#     # def check_generator_module(self,used_procedures_and_classes):
#     #     if not self.gen:
#     #         raise Exception("No code generator provided please use 'set_generator_module()' in parser module")
#     #     if not self.generator_module_implements(used_procedures_and_classes) :
#     #         raise Exception("code generator doesn't implement all expected functions")
#
