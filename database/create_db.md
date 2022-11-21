# Primeros Pasos
1. Abrir una terminal
2. psql -U postgres

# Eliminar usuario si existe
1. SELECT * FROM pg_roles WHERE rolname = 'admin';
2. DROP OWNED BY admin;
3. DROP USER admin;

# Crear Usuario y DB
1. CREATE USER admin WITH ENCRYPTED PASSWORD 'test1234';
2. CREATE DATABASE tadp;
3. GRANT ALL PRIVILEGES ON DATABASE tadp TO admin;

# Últimos Paso
- \q