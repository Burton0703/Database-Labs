import pymysql
import mvc_exceptions as mvc_exc
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='z.668872',
                       database='school')
cursor = conn.cursor()


# def __init__(self, class_id, class_name):
#     self.id = class_id
#     self.name = class_name
#     self.conn = conn.cursor()


def insert_one(class_id, class_name):
    sql = f'INSERT INTO class (class_id,class_name) VALUES (%s,%s);'
    try:
        cursor.execute(sql, (class_id, class_name))
        conn.commit()
        print('成功插入一条数据!')
    except pymysql.Error as e:
        raise mvc_exc.ItemAlreadyStored(
            f'{e}: {class_id} already stored in table class'
        )


def insert_many(items):
    sql = f'INSERT INTO class (class_id,class_name) VALUES (%s,%s)'
    entries = list()
    for x in items:
        entries.append((x[0], x[1]))
    try:
        cursor.executemany(sql, entries)
        conn.commit()
        print('成功多条数据！')
    except pymysql.Error as e:
        print('{}: at least one in {} was already stored in table class'
              .format(e, [x['class_id'] for x in items]))


def select_one(class_id):
    sql = f'SELECT * FROM class WHERE class_id = {class_id}'
    cursor.execute(sql)
    result = cursor.fetchone()
    if result is not None:
        return result
    else:
        raise mvc_exc.ItemNotStored(
            f'Can\'t read class_id = {class_id} because it\'t nor stored in table class')


def select_all(table_name):
    sql = f'SELECT * FROM {table_name}'
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def update_one(class_id, class_name):
    sql_check = 'SELECT EXISTS(SELECT 1 FROM class WHERE class_id=%s LIMIT 1)'
    sql_update = 'UPDATE class SET class_name = %s WHERE class_id= %s'
    cursor.execute(sql_check, (class_id,))  # we need the comma
    result = cursor.fetchone()
    if result[0]:
        cursor.execute(sql_update, (class_name, class_id))
        conn.commit()
        print(
            f'Successfully updated the class_name = {class_name} where class_id = {class_id}!')
    else:
        raise mvc_exc.ItemNotStored(
            f'Can\'t update class_id = "{class_id}" because it\'s not stored in table class')


def delete_one(class_id):
    sql_check = 'SELECT EXISTS(SELECT 1 FROM class WHERE class_id=%s LIMIT 1)'
    sql_delete = 'DELETE FROM class WHERE class_id = %s'
    cursor.execute(sql_check, (class_id,))  # we need the comma
    result = cursor.fetchone()
    if result[0]:
        cursor.execute(sql_delete, (class_id,))  # we need the comma
        conn.commit()
        print(f'Successfully deleted the data which class_id = {class_id}!')
    else:
        raise mvc_exc.ItemNotStored(
            f'Can\'t delete class_id = "{class_id}" because it\'s not stored in table class')


def main():
    # print('SELECT class_id = 1')
    # print(select_one('1'))
    # print('SELECT all:')
    # print(select_all('class'))

    # insert_one(8, 'ip-12')
    # items = [          # 模版字符串中的参数，是一个列表，列表中的每一个元素必须是元组！！！
    #     (6, 'ip-10'),
    #     (7, 'ip-11')
    # ]
    # insert_many(items)
    update_one(6, 'ip-01')
    # delete_one(7)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
