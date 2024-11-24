from pyhive import hive

conn = hive.Connection(host="localhost", port=10000, username="hive")
cursor = conn.cursor()

table_name = 'sua_tabela'

cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
tables = cursor.fetchall()

if not tables:
    print(f"Tabela {table_name} não existe. Criando a tabela...")
    cursor.execute(f"""
    CREATE TABLE {table_name} (
        id INT,
        nome STRING
    )
    """)
    print(f"Tabela {table_name} criada.")

for i in range(1, 6):
    cursor.execute(f"INSERT INTO {table_name} (id, nome) VALUES ({i}, 'Item {i}')")

cursor.execute(f"SELECT * FROM {table_name}")
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
conn.close()
