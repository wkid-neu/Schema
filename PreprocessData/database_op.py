import pymysql


class datasql(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root", password="123",
            database="django_mysql",
            charset="utf8"  # 没有-
        )
        self.cursor = self.conn.cursor()

    def query(self, dest):
        sql = "select * from {}".format(dest)  # %s需要去掉引号，pymysql会自动加上
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def insert_class_info(self, val):
        sql = "INSERT INTO entity_tab(entity_name, name_zh, super_name, entity_url, description, self_properties, all_properties) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        try:
            # 执行sql语句
            self.cursor.executemany(sql, val)
            # 提交到数据库执行
            self.conn.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            self.conn.rollback()

    def insert_property_info(self, content):
        sql = "INSERT INTO property_tab(property_name, name_zh, property_url, description) VALUES (%s,%s,%s,%s)"
        try:
            # 执行sql语句
            self.cursor.executemany(sql, content)
            # 提交到数据库执行
            self.conn.commit()
        except Exception as e:
            # 如果发生错误则回滚
            print(e)
            self.conn.rollback()

    def insert_range_tab(self, content):
        sql = "INSERT INTO range_tab(property_name, range_str) VALUES (%s,%s)"
        try:
            # 执行sql语句
            self.cursor.executemany(sql, content)
            # 提交到数据库执行
            self.conn.commit()
        except Exception as e:
            # 如果发生错误则回滚
            print(e)
            self.conn.rollback()

    def close(self):
        self.conn.close()
