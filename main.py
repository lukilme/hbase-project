import happybase

connection = happybase.Connection('localhost', port=9090)
connection.open()
print(connection.tables())
