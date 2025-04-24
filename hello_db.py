import psycopg2

# Do not expose your Neon credentials to the browser

PGHOST='ep-little-base-a4uo5yhk-pooler.us-east-1.aws.neon.tech'
PGDATABASE='neondb'
PGUSER='neondb_owner'
PGPASSWORD='npg_FtrX9BkMKuH8'

conexion = psycopg2.connect(host = PGHOST, database = PGDATABASE, user = PGUSER, password = PGPASSWORD)

cursor = conexion.cursor()
cursor.execute('SELECT nombre_departamento, codigo_departamento from departamentos')
resultado = cursor.fetchall()

print(resultado)