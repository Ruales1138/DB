import psycopg2

# Do not expose your Neon credentials to the browser

PGHOST='ep-little-base-a4uo5yhk-pooler.us-east-1.aws.neon.tech'
PGDATABASE='neondb'
PGUSER='neondb_owner'
PGPASSWORD='npg_FtrX9BkMKuH8'

conexion = psycopg2.connect(host = PGHOST, database = PGDATABASE, user = PGUSER, password = PGPASSWORD)

respuesta = input('Nombre de departamento: ')

cursor = conexion.cursor()
cursor.execute(f"select codigo_municipio, nombre_municipio, codigo_departamento from municipios where codigo_municipio LIKE '%001'")
resultado = cursor.fetchall()

print(resultado)