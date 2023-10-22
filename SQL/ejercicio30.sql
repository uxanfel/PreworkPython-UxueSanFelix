/* 30. Agrega una restricción de clave primaria a la columna "id" en la tabla "Usuarios". */
ALTER TABLE public.usuarios
ADD CONSTRAINT pk_usuarios_id PRIMARY KEY (id);