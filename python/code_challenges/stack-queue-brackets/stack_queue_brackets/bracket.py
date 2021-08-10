open_list = ['(','[','{']
close_list = [')',']','}']

def validate_brackets(input):
    char_list=[]
    for i in input:
        if i in open_list:
            char_list.append(i)
        elif i in close_list:
            x = close_list.index(i)
            if ((len(char_list) > 0) and (open_list[x] == char_list[len(char_list) - 1])):
                    char_list.pop()
            else:
                return False
    if len(char_list) == 0:
            return True
    else:
            return False


result=validate_brackets('(){[]}')
print(result)
result1=validate_brackets('[{})')
print(result1)
