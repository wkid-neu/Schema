from pandas._libs import json
import os
import re

pattern = ': "[\s\S]*[^\\\]"[\s\S]+",'
pattern_two = '[^\\\]"[\s\S]+",'
path = '../all_class_json'


def solve(file_path):
    print(file_path)
    filter_data = ""
    with open(file_path, 'r', encoding='utf-8') as f:
        for row in f.readlines():
            res = re.search(pattern, row)
            str = row
            if res is not None:
                print(row)
                pos = res.span()
                pos_two = pos[0]
                res2 = re.search(pattern_two, row[pos_two + 3:])
                st_pos = pos_two + 3 + res2.span()[0]
                end_pos = row.find("\",", st_pos)
                str_fro = row[0:st_pos]
                str_mid = row[st_pos:end_pos]
                str_end = row[end_pos:]
                str_list_mid = list(str_mid)
                for i in range(len(str_list_mid)):
                    if str_list_mid[i] == '"':
                        str_list_mid[i] = '\\"'
                str_mid = ''.join(str_list_mid)
                str = str_fro + str_mid + str_end
            filter_data += str
    f.close()
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(filter_data)
    f.close()


def filter_pro(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                temp_content = f.read()
                content = json.loads(temp_content)
        except:
            solve(file_path)

# if __name__ == "__main__":
#     filter_pro('../all_property_json')
