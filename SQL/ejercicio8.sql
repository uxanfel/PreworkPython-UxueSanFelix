/* 8. Actualiza el cliente_id del pedido con id=1 a 2 en la tabla "Pedidos". */
UPDATE public.pedidos
SET cliente_id = 2
WHERE cliente_id = 1;