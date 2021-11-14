import pymysql


class Mysql():
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost', user='root', password='z.668872', database='school')

# operation CUD
    def update(self, sql):
        print(f'Received sql:{sql}')
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                self.connection.commit()
        except Exception as e:
            self.conn.rollback()
            return "非空"
        finally:
            if self.connection:
                self.connection.close()

    def get_all(self, sql):
        try:
            # 使用with建立/关闭游标对象 ：cursor
            with self.conn.cursor() as cursor:
                # 执行sql语句
                cursor.execute(sql)
                # 查询sql语句
                result = cursor.fetchall()
                return result
        # try中的代码块若出现异常则处理并打印异常信息
        except Exception as e:
            print(e)
        # 以上代码块执行结束后最后断开mysql数据库连接
        finally:
            # 如果mysql连接对象存在，则关闭连接对象：conn.close()
            if self.conn:
                self.conn.close()
