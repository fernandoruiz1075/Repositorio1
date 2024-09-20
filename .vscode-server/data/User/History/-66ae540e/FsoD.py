import pymysql

endpoint = 'database-1.c5eyaugg4l87.us-east-2.rds.amazonaws.com'
user = 'admin'
passw = 'NATAdani65'

def connectionSQL():
    try:
        pymysql.connect (
            host=endpoint,
            User=user,
            password=passw
        )

     except Exception as err:
        print("Error:",err)       

connectionSQL()

