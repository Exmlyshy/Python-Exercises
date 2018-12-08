import os


# with open('test.txt', 'r', encoding='utf-8') as f:
#     print(f.readlines())
l = []
code_lines = comment_lines = empty_lines = 0
with open('test.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        l.append(line)
        if line.startswith('#'):
            comment_lines += 1
        elif line.startswith("'''"):
            comment_lines += 1
            line = f.readline()
            while(line and not line.endswith("'''\n")):
                comment_lines += 1
                line = f.readline()
            comment_lines += 1
        elif line == '\n':
            empty_lines += 1
        else:
            code_lines += 1
        line = f.readline()

print(l)
print(code_lines, comment_lines, empty_lines)