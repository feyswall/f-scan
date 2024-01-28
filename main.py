import socket
from windows.FrontWindows import FrontWindows
from database.QueryBuilder import QueryBuilder
from database.SQLiteTables import SQLiteTables

sql = SQLiteTables()
# slq.create_setups_table()

queryBuilder = QueryBuilder()
# queryBuilder.insert_setup('default', '25378', '192.168.28.1')

setups = queryBuilder.get_all_setups()
print( len(setups) )

print("ZEBRA CONFIGURATIONS")
print("NEXT LINE")