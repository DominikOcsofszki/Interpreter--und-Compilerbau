import re
file_path = 'code/symbol_table.tx'

with open(file_path, 'r') as file:
    text = file.read()

# print(file_contents[40:50])
# print(file_contents[92])
pattern = r'[a-zA-Z_][a-zA-Z_0-9]*'
print(text)
x = re.findall(pattern,text)
print(x)


lines = text.splitlines()

matches_with_positions = []

for line_num, line in enumerate(lines, start=1):
    for match in re.finditer(pattern, line):
        word = match.group()
        start_column = match.start() + 1 
        matches_with_positions.append(f"{word} (Line {line_num}, Column {start_column})")

column_output = "\n".join(matches_with_positions)

print(column_output)
