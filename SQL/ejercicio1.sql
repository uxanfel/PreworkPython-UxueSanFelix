/* 1. Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria),nombre (texto) y email (texto). */
CREATE TABLE IF NOT EXISTS clientes(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	email VARCHAR(255)
)