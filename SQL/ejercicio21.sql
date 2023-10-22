/* 21. Realiza una consulta para obtener todos los clientes y sus pedidos correspondientes utilizando un inner join. */
SELECT * FROM public.clientes
INNER JOIN public.pedidos
ON public.clientes.id = public.pedidos.cliente_id
