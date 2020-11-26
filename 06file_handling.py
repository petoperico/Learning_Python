"""File Handling."""

# my_file = open('data.txt', 'r')

"""
with open('data.txt', 'r') as data:
    print(f'File name: {data.name}')
    # for text_line in data.readlines():
    #     print(text_line, end='')
    for line in data:
        print(line, end='')
"""
"""
lines = ["This is line 1", "This is line 2", "This is line 3", "This is line 4"]
with open('data.txt', 'w') as data:
    for line in lines:
        data.write(line)
        data.write('\n')
"""
lines = ["This is line 5", "This is line 6", "This is line 3", "This is line 7"]
with open('data.txt', 'r') as data:
    data_as_list = data.readlines()

data_as_list.insert(1, "This is between line 1 and 2\n")

with open('data.txt', 'w') as data:
    data_as_str = "".join(data_as_list)
    data.write(data_as_str)

with open('data.txt', 'a') as data:
    for line in lines:
        data.write(line)
        data.write('\n')

"""
Text file's modes:
w - Write
r - Read
a - Append
r+ - Read  Write
x - Creation Mode

Binary file's modes:
wb - Write
rb - Read
ab - Append
rb+ - Read  Write
"""
