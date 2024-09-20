import pymysql

endpoint = 'database-1.c5eyaugg4l87.us-east-2.rds.amazonaws.com'
user = ''
passw = ''

pymysql.connect (
    host=endpoint,
    User=user,
    password=passw
)