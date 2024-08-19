
from icecream import ic
from collections import defaultdict

# my_dict = defaultdict(list)
#
# my_dict["s"].append(1)
# my_dict["s"].append(2)
# my_dict["s"].append(3)
#
# print(my_dict["s"])

class TableDict:

    def __init__(self,tables=[{}]):
        self.tables = tables
        self.local_index = 0

    def get_global_table(self):
        return self.tables[0]

    def get_local(self):
        return self.tables[self.local_index]

    def set_local_var(self, var_name, var_info,index_from_env):
        self.tables[index_from_env][var_name] = var_info

    # def set_local_var(self, var_name, var_info):
    #     self.tables[self.local_index][var_name] = var_info

    def set_global_var(self, var_name, var_info):
        self.tables[0][var_name] = var_info

    def push_local(self):
        self.local_index = self.local_index + 1

    def pop_local(self):
        if self.local_index == 0:
            raise RuntimeError("self.local_index == 0, pop_local should not happen!")
        self.local_index = self.local_index - 1

    def get_global_var(self, var_name):
        return self.tables[0][var_name]

    def _try_index_var(self,index,var_name):
        ic(self,index,var_name)
        return self.tables[index].get(var_name, None)

    def get_local_var(self, var_name, index):
        # ic("def get_local_var(self, var_name, index):")
        # ic(self, var_name, index)
        
        # index = self.local_index
        while index >= 0:
            entry = self._try_index_var(index,var_name)
            # ic(entry)
            if entry:
                return entry
            else:
                index = index - 1

    def __repr__(self):
        return f"TableDict(tables={self.tables}, local_index={self.local_index})"

SYMBOL_TABLE = TableDict()


