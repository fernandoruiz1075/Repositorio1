import pymysql

endpoint = 'database-1.c5eyaugg4l87.us-east-2.rds.amazonaws.com'
user = 'admin'
passw = 'NATAdani65'

def connectionSQL():
    try:
        obj_connect = pymysql.connect(
            host=endpoint,
            user=user,
            password=passw
        )
        print("Succesfull connection to a database")
        return obj_connect 
    except Exception as err:
        print("Error:",err)
        obj_connect = None

def add_user (id, name, lastname, birthday):
    try:
        instruction_sql = "INSERT INTO db_users.users (id, name, lastname, birthday) VALUES (" + str(id) + ", '" + name + "', '" + lastname + "', '" + birthday + "')"
        obj_connect = connectionSQL()
        obj_connect.cursor().execute(instruction_sql).commit()
        print("The user was added")
        #return True
    except Exception as err:
        print("Error:",err)
        #return False