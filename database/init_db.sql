/*
    This script is intended to work only in a postgresql database
*/

-- # Delete tables

DO
$$
BEGIN
   IF EXISTS (SELECT 1 from INFORMATION_SCHEMA.Tables WHERE table_schema = 'tadp' AND  table_name = 'clave') THEN
        DROP TABLE tadp.clave;
   END IF;
END $$;

DO
$$
BEGIN
   IF EXISTS (SELECT 1 from INFORMATION_SCHEMA.Tables WHERE table_schema = 'tadp' AND  table_name = 'turno_revision') THEN
        DROP TABLE tadp.turno_revision;
   END IF;
END $$;

DO
$$
BEGIN
   IF EXISTS (SELECT 1 from INFORMATION_SCHEMA.Tables WHERE table_schema = 'tadp' AND  table_name = 'turno_examen') THEN
        DROP TABLE tadp.turno_examen;
   END IF;
END $$;

DO
$$
BEGIN
   IF EXISTS (SELECT 1 from INFORMATION_SCHEMA.Tables WHERE table_schema = 'tadp' AND  table_name = 'usuario') THEN
        DROP TABLE tadp.usuario;
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
CREATE SCHEMA tadp;

-- # Create Tables
CREATE TABLE tadp.usuario (
  id_usuario INT GENERATED ALWAYS AS IDENTITY,
  tipo TEXT NOT NULL, -- POSTULANTE o ADMINISTRADOR
  habilitado boolean NOT NULL DEFAULT true,
  anteojos boolean NOT NULL DEFAULT false,
  nombre_usuario TEXT NOT NULL,
  contrasenia TEXT NOT NULL
);

CREATE TABLE tadp.turno_examen (
  id_turno_examen INT GENERATED ALWAYS AS IDENTITY,
  id_usuario INT NOT NULL,
  fecha DATE NOT NULL
);

CREATE TABLE tadp.turno_revision (
  id_turno_revision INT GENERATED ALWAYS AS IDENTITY,
  id_usuario INT NOT NULL,
  fecha DATE NOT NULL
);

CREATE TABLE tadp.clave (
  id_clave INT GENERATED ALWAYS AS IDENTITY,
  valor TEXT NOT NULL,
  fecha_creacion DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  es_valida BOOLEAN NOT NULL DEFAULT true
);

-- # PK
ALTER TABLE tadp.usuario ADD PRIMARY KEY (id_usuario);
ALTER TABLE tadp.turno_examen ADD PRIMARY KEY (id_turno_examen);
ALTER TABLE tadp.turno_revision ADD PRIMARY KEY (id_turno_revision);
ALTER TABLE tadp.clave ADD PRIMARY KEY (id_clave);

-- # FK Constraint

ALTER TABLE tadp.turno_examen 
ADD CONSTRAINT fk_turno_examen_usuario 
FOREIGN KEY (id_usuario) 
REFERENCES tadp.usuario (id_usuario);

ALTER TABLE tadp.turno_revision
ADD CONSTRAINT fk_turno_revision_usuario 
FOREIGN KEY (id_usuario) 
REFERENCES tadp.usuario (id_usuario);

-- # Insert Test Values
INSERT INTO tadp.usuario(tipo, nombre_usuario, contrasenia) VALUES ('POSTULANTE', 'test', 'test');

INSERT INTO tadp.turno_examen(id_usuario, fecha) VALUES (1, current_timestamp);

INSERT INTO tadp.turno_revision(id_usuario, fecha) VALUES (1, current_timestamp);

INSERT INTO tadp.clave(id_usuario, fecha) VALUES (1, current_timestamp);

-- # After Changes Check 
SELECT * FROM tadp.usuario;
