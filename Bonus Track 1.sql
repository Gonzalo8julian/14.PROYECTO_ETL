select * from public.ciudad;
select * from public.eventos;
select * from public.hoteles;
select * from public.clientes;
select * from public.reservas;

select 
	h.nombre_hotel,
	COUNT(r.id_reserva) AS num_reservas
from
	public.hoteles as h 
	join public.reservas as r on h.id_hotel = r.id_hotel
where
	h.competencia = true
group by
	h.nombre_hotel
order by
	num_reservas desc;

#BONUS TRACK

#1. Cuántos hoteles tiene la BBDD:

select 
	count(id_hotel) as total_hoteles
from
	public.hoteles;

#2 Cuántas reservas se han hecho

select
	count(id_reserva) as total_reservas
from
	public.reservas;

#3 Identifica los 10 clientes que más se han gastado:

select
	CONCAT(c.nombre , ' ', c.apellido) as nombre_cliente,
	r.precio_noche
from 
	public.clientes c
	join public.reservas r on c.id_cliente = r.id_cliente
order by
	r.precio_noche desc limit 10;

#4. Identifica el hotel de la competencia y el hotel de nuestra marca que más han recaudado para esas fechas:

select
	h.nombre_hotel,
	h.competencia,
	sum(r.precio_noche) as total_recaudado_competencia
from
	public.hoteles h
	join public.reservas r on h.id_hotel = r.id_hotel
where 
	h.competencia = True
group by
	h.nombre_hotel,
	h.competencia
order by
	total_recaudado_competencia desc
limit 1;

select
	h.nombre_hotel,
	h.competencia,
	sum(r.precio_noche) as total_recaudado_propios
from
	public.hoteles h
	join public.reservas r on h.id_hotel = r.id_hotel
where 
	h.competencia = False
group by
	h.nombre_hotel,
	h.competencia 
order by
	total_recaudado_propios desc
limit 1;

#5. Identifica cuantos eventos hay.

select 
	count(id_evento) as Total_eventos
from
	public.eventos;

#6. Identifica el día que más reservas se han hecho para nuestro hoteles
select
	r.fecha_reserva,
	count(r.id_reserva) as total_reservas
from
	public.reservas r
	join public.hoteles h on r.id_hotel = h.id_hotel
where
	h.competencia = False
group by
	r.fecha_reserva
order by total_reservas desc
limit 1;
	



