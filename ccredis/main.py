import re

def define_input(input):
    in_split = input.split('\r\n')
    print(in_split)
    analyse = in_split[0]
    print(analyse)
    result = ''
    if re.match(r'[\$*]-\d', analyse): 
        #raise Exception('Null string received', analyse)
        print("Null string received")
    elif re.match(r'[\+\-].*', analyse):
        if analyse[0] == "+":
            print("Simple String detected in " + analyse)
        elif analyse[0] == ":":
            print("Integer detected in ", analyse)
        else:
            print("Error detected in " + analyse)
        result = get_simple_string(analyse)
    elif re.match(r'\$\d*', analyse):
        print("Bulk String detected in " + input)
        result = get_bulk_string(input)
    elif re.match(r'\*\d*', analyse):
        print("Array detected in " + input)
        result = get_array_parse(input)
    print("Result: ")
    print(result)

def get_simple_string(input):
    return input[1:]

def get_bulk_string(input):
    list_of_str = input.split('\r\n')
    length = list_of_str[0][1:]
    try:
        int_length = int(length)
    except ValueError:
        print("the string is in the incorrect format. Expected int after $, found " + length)
    if int_length > 0:
        return list_of_str[1]
    else: 
        return ''

def get_array_parse(input):
    list_of_str = input.split('\r\n')
    length = list_of_str[0][1:]
    res = []
    try:
        int_length = int(length)
    except ValueError:
        print("the array is in the incorrect format. Expected int after *, found " + length)
    if int_length > 0:
        for i in range(1,int_length+1):
            res.append(list_of_str[i * 2])
        return res
    else: 
        return ''
    
if __name__ == "__main__":
    arr = ["$-1\r\n",'*1\r\n$4\r\nping\r\n','*2\r\n$4\r\necho\r\n$11\r\nhello world\r\n', '*2\r\n$3\r\nget\r\n$3\r\nkey\r\n',"+OK\r\n","-Error message\r\n","$0\r\n\r\n",'+hello world\r\n']
    for i in range(len(arr)):
        define_input(arr[i])