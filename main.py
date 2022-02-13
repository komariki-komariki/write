import os
def union_file():
    temp_list =[]
    final_list = []
    directory = os.getcwd()
    files = os.listdir(directory)
    for name in files:
        if 'txt' in name:
            with open(name, encoding='utf-8') as file:
                temp_list = []
                file_text = file.readlines()
                file_name = str(name) + '\n'
                file_len = str(len(file_text)) + '\n'
                temp_list += file_name, file_len
                temp_list += file_text
                temp_list += '\n'
                final_list.append(temp_list)
    sorted_list = sorted(final_list, key=len)
    for one_list in sorted_list:
        string = "".join(one_list)
        my_file = open("rezult.txt", "a", encoding='utf8')
        my_file.write(string)
        my_file.close()
union_file()
