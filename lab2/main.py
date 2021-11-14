import pymysql
import mvc_exceptions as mvc_exc


connection = pymysql.connect(
    host='localhost', user='root', password='z.668872', database='school')

cursor = connection.cursor()

# Create table


def create_table(table_name):
    sql = f'''CREATE TABLE {table_name}(
                class_id INT(10) PRIMARY KEY NOT NULL,
                class_name VARCHAR(30) NOT NULL)'''
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)

# Create function


def insert_one(class_id, class_name, table_name):
    sql = f'INSERT INTO {table_name} (class_id,class_name) VALUES (%s,%s,%s)'
    try:
        cursor.execute(sql, (class_id, class_name))
        connection.commit()
    except Exception as e:
        raise mvc_exc.ItemAlreadyStored(
            f'{e}:{class_name} already stored in table {table_name}')


def insert_many(items, table_name):
    sql = f'INSERT INTO {table_name} (class_id,class_name) VALUES (%s,%s,%s)'


cursor.close()
connection.close()
# here
