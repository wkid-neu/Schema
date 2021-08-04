import os

from PreprocessData.database_op import datasql


def load():
    path = r'..\all_class_files'
    result = {}
    for class_name in os.listdir(path):
        with open(os.path.join(path, class_name), 'r', encoding='utf-8') as f:
            read_data = f.read()
            read_data = read_data[read_data.find('class '):]
            result[class_name[:class_name.find('.')]] = read_data
    return result


def run(preprocess_data):
    all_class_content = load()
    content = 'import global_data\n\n'
    vis = ['object']
    while len(vis) < len(all_class_content):
        for class_name in all_class_content:
            if class_name in vis:
                continue
            super_names = preprocess_data[class_name]
            for father in super_names.split(','):
                if father not in vis:
                    flag = True
                    continue
            if flag is True:
                flag = False
                continue
            vis.append(class_name)
            content += all_class_content[class_name]+'\n\n'
    with open(r'..\all_class_files\all_class.py', 'w', encoding='utf-8') as f:
        f.write(content)
        f.close()


if __name__ == '__main__':
    msql = datasql()
    entities = msql.query('entity_tab')
    preprocess_data = dict(zip([obj[0] for obj in entities], [obj[2] for obj in entities]))  # 实体名，实体父类们，实体自己的属性
    run(preprocess_data)
