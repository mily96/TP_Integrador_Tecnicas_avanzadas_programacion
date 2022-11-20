/*
    This script is intended to work only in a postgresql database
*/

-- # Delete tables
DO
$$
BEGIN
   IF EXISTS (SELECT 1 from INFORMATION_SCHEMA.Tables WHERE table_schema = 'tadp' AND  table_name = 'usuario') THEN
        DROP TABLE tadp.Usuario;
   END IF;
END $$;

-- # Delete schema
DO
$$
BEGIN
    IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.Schemata WHERE schema_name = 'tadp') THEN
        DROP SCHEMA tadp;
    end if;
END $$;

-- # Create Schema
CREATE SCHEMA IF NOT EXISTS tadp;

-- # Create Tables
CREATE TABLE tadp.Usuario (
  idUsuario INT GENERATED ALWAYS AS IDENTITY,
  tipo TEXT NOT NULL, -- POSTULANTE o ADMINISTRADOR
  habilitado boolean NOT NULL DEFAULT true,
  anteojos boolean NOT NULL DEFAULT false,
  nombreUsuario TEXT NOT NULL,
  contrasenia TEXT NOT NULL
);


-- # PK
ALTER TABLE tadp.Usuario ADD PRIMARY KEY (idUsuario);

-- # FK Constraint

-- # Constraint


-- ALTER TABLE child_table 
-- ADD CONSTRAINT constraint_name 
-- FOREIGN KEY (fk_columns) 
-- REFERENCES parent_table (parent_key_columns);

-- # Insert Test Values
INSERT INTO tadp.Usuario(tipo, nombreUsuario, contrasenia) VALUES ('POSTULANTE', 'test', 'test');

-- fetch 
SELECT * FROM tadp.Usuario;
