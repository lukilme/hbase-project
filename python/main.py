import happybase

# Configurar a conexão com o HBase
HBASE_HOST = 'localhost'  # Substitua pelo IP ou hostname do servidor HBase
HBASE_PORT = 9090         # Porta do servidor Thrift

# Criar conexão com o HBase
connection = happybase.Connection(host=HBASE_HOST, port=HBASE_PORT)

# Nome da tabela
table_name = 'clientes'

# Função para criar uma tabela
def create_table():
    if table_name.encode() not in connection.tables():
        connection.create_table(
            table_name,
            {
                'info': dict(),  # Família de colunas "info"
                'endereco': dict()  # Família de colunas "endereco"
            }
        )
        print(f"Tabela '{table_name}' criada com sucesso!")
    else:
        print(f"Tabela '{table_name}' já existe.")

# Função para inserir dados
def insert_data():
    table = connection.table(table_name)
    # Inserir dados na linha com row key '1'
    table.put('1', {
        b'info:nome': b'Joao Silva',
        b'info:idade': b'30',
        b'endereco:rua': b'Rua das Flores',
        b'endereco:cidade': b'Sao Paulo'
    })
    # Inserir dados na linha com row key '2'
    table.put('2', {
        b'info:nome': b'Maria Oliveira',
        b'info:idade': b'25',
        b'endereco:rua': b'Av. Central',
        b'endereco:cidade': b'Rio de Janeiro'
    })
    print("Dados inseridos com sucesso!")

# Função para consultar dados de uma linha específica
def get_data(row_key):
    table = connection.table(table_name)
    row = table.row(row_key.encode())
    if row:
        print(f"Dados da linha {row_key}:")
        for key, value in row.items():
            print(f"  {key.decode()}: {value.decode()}")
    else:
        print(f"Não foram encontrados dados para a linha '{row_key}'.")

# Função para consultar todos os dados da tabela
def scan_table():
    table = connection.table(table_name)
    print("Todos os dados da tabela:")
    for key, data in table.scan():
        print(f"Chave: {key.decode()}")
        for col, val in data.items():
            print(f"  {col.decode()}: {val.decode()}")

# Função para excluir uma linha
def delete_row(row_key):
    table = connection.table(table_name)
    table.delete(row_key.encode())
    print(f"Linha '{row_key}' excluída com sucesso!")

# Função principal
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
    # Fechar a conexão
    connection.close()

# Executar o programa
if __name__ == '__main__':
    main()
