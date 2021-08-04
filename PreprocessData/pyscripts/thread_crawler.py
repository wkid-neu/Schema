import threading
import time
from queue import Queue
import requests
import os
from bs4 import BeautifulSoup
from PreprocessData.database_op import datasql


def run(que, json_load_path):
    headers = {
        'Cookie': 'OCSSID=4df0bjva6j7ejussu8al3eqo03',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    cnt = 0
    while que.empty() is not True:
        try:
            url = que.get()
            filename = url[url.rfind('/') + 1:-5]
            path = '{}/{}.json'.format(json_load_path, filename)
            if os.path.exists(path) is True:
                print("%s 已经存在。" % (filename))
                continue
            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.content, "html.parser", from_encoding='gb18030')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(soup.text)
                f.close()
            time.sleep(1)
            cnt = cnt + 1
            print("完成第 %s 个" % (cnt))
        except Exception as e:
            print(e)


def prepare(dest, result):
    queue = Queue()
    json_load_path = r'../all_{}_json'.format(dest)
    for obj in result:
        # print('http://cnschema.org/data/' + obj[0] + '.json')
        queue.put('http://cnschema.org/data/' + obj[0] + '.json')
    for i in range(1, 6):
        t = threading.Thread(target=run, args=(queue, json_load_path))
        t.start()
        t.join()


if __name__ == '__main__':
    dest = 'property'  # 爬取实体还是属性
    msql = datasql()
    result = msql.query('{}_tab'.format(dest))
    prepare(dest, result)

    # filter_pro(json_load_path)  ##爬取的某些json中格式有错误，需要纠正
