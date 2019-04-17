import os

def countvalues():
    with open('test.txt', 'r') as f:
        content = f.read()
    content_list = content.split('\n')
    keystack = {}
    for i in range(0,len(content_list)):
        dict_temp = content_list[i].split(' ')
        dict_key = dict_temp[0]
        dict_value = dict_temp[1]
        if dict_key not in keystack.keys():
            keystack.setdefault(dict_key, [dict_value,1])
        else:
            if dict_value not in keystack[dict_key]:
                keystack.setdefault(dict_key, [dict_value, 1])
            # for i in keystack:
            #     print('s' + i)
            #     if i[0] == dict_value:
            #         i[1] += 1
            pass
        print(keystack)









countvalues()