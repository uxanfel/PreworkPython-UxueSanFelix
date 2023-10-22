/* 23. Realiza una consulta para obtener todos los productos y los detalles de pedido correspondientes utilizando un inner join. */
SELECT * FROM public.productos
INNER JOIN public.detallespedido
ON public.productos.id = public.detallespedido.pedido_id
