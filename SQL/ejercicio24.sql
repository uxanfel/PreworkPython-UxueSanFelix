/* 24. Realiza una consulta para obtener todos los productos y los detalles de pedido correspondientes utilizando un left join. */
SELECT * FROM public.productos
LEFT JOIN public.detallespedido
ON public.productos.id = public.detallespedido.pedido_id