/* 22. Realiza una consulta para obtener todos los clientes y sus pedidos correspondientes utilizando un left join. */
SELECT * FROM public.clientes
LEFT JOIN public.pedidos
ON public.clientes.id = public.pedidos.cliente_id

