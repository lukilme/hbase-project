import happybase

connection = happybase.Connection('localhost', port=9090)
connection.open()

try:
    connection.create_table(
        'test_table',
        {'cf1': dict()}  
    )
    print("Tabela criada com sucesso!")
except Exception as e:
    print(f"Tabela já existe: {e}")

table = connection.table('test_table')
table.put(b'row1', {b'cf1:col1': b'value1'})

row = table.row(b'row1')
print(f"Row: {row}")

connection.close()
