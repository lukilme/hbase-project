import happybase


HBASE_HOST = 'localhost'  
HBASE_PORT = 9090        

connection = happybase.Connection(host=HBASE_HOST, port=HBASE_PORT)

table_name = 'cliente32s'

def create_table():
    if table_name.encode() not in connection.tables():
        connection.create_table(
            table_name,
            {
                'info': dict(),  
                'endereco': dict()  
            }
        )
        print(f"Tabela '{table_name}' criada com sucesso!")
    else:
        print(f"Tabela '{table_name}' já existe.")

def insert_data():
    table = connection.table(table_name)

    table.put('1', {
        b'info:nome': b'Joao Silva',
        b'info:idade': b'30',
        b'endereco:rua': b'Rua das Flores',
        b'endereco:cidade': b'Sao Paulo'
    })

    table.put('2', {
        b'info:nome': b'Maria Oliveira',
        b'info:idade': b'25',
        b'endereco:rua': b'Av. Central',
        b'endereco:cidade': b'Rio de Janeiro'
    })
    print("Dados inseridos com sucesso!")

def get_data(row_key):
    table = connection.table(table_name)
    row = table.row(row_key.encode())
    if row:
        print(f"Dados da linha {row_key}:")
        for key, value in row.items():
            print(f"  {key.decode()}: {value.decode()}")
    else:
        print(f"Não foram encontrados dados para a linha '{row_key}'.")

def scan_table():
    table = connection.table(table_name)
    print("Todos os dados da tabela:")
    for key, data in table.scan():
        print(f"Chave: {key.decode()}")
        for col, val in data.items():
            print(f"  {col.decode()}: {val.decode()}")

def delete_row(row_key):
    table = connection.table(table_name)
    table.delete(row_key.encode())
    print(f"Linha '{row_key}' excluída com sucesso!")

def main():
    print("Interagindo com o HBase...")
    create_table()
    insert_data()
    print("\n--- Consultando dados de uma linha específica ---")
    get_data('1')
    print("\n--- Escaneando a tabela completa ---")
    scan_table()
    print("\n--- Excluindo uma linha ---")
    delete_row('1')
    print("\n--- Escaneando a tabela após exclusão ---")
    scan_table()
    connection.close()

if __name__ == '__main__':
    main()
