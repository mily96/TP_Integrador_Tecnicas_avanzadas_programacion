# Primeros Pasos
1. Abrir una terminal
2. psql -U postgres

# Eliminar usuario si existe
1. SELECT * FROM pg_roles WHERE rolname = 'admin';
2. DROP USER admin;

(optional) DROP OWNED BY admin;

# Crear nuevo usuario
- CREATE USER admin WITH ENCRYPTED PASSWORD 'test1234';
(optional) GRANT ALL PRIVILEGES ON DATABASE [mydatabase] TO admin;

# Últimos Paso
- \q