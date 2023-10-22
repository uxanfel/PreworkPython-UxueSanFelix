/* 29. Cambia el nombre de la columna "nombre" en la tabla "Usuarios" a "nombre_completo". */
ALTER TABLE public.usuarios
RENAME COLUMN nombre TO nombre_completo;
