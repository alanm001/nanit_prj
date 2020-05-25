create or replace view v_load_into_dwh_fact_orders as
select o.order_id,
		dispatch_reference,
		ol.product_description,
		sum(ol.quantity) as orders_quantity,
		sum(dl.quantity) as dispatches_quantity,
		sum(ol.quantity * unit_cost) as order_total_price,
		products_ordered_together,
		'stg tables' as data_source,
		CURRENT_TIMESTAMP as dwh_updated_at
from stg_orders o
join (select order_id,product_description,unit_cost,sum(quantity) quantity
		from stg_order_lines
		group by order_id,product_description,unit_cost) ol on o.order_id = ol.order_id 
left join stg_dispatch_lines dl on ol.order_id = dl.order_id and ol.product_description = dl.product_description
left join (select order_id,GROUP_CONCAT(distinct product_description order by product_description SEPARATOR', ') as products_ordered_together
		   from nanit.stg_order_lines
		   group by order_id
		   ) f1 on o.order_id = f1.order_id 
group by o.order_id,
		dispatch_reference,
		ol.product_description,
		products_ordered_together,
		'stg tables',
		CURRENT_TIMESTAMP
# for inserting all dispatch items that not appears in the order
UNION 
select dl.order_id,
		dispatch_reference,
		dl.product_description,
		null as orders_quantity,
		sum(dl.quantity) as dispatches_quantity,
		null as order_total_price,
		null as products_ordered_together,
		'stg tables' as data_source,
		CURRENT_TIMESTAMP as dwh_updated_at
from stg_dispatch_lines dl
left join (select order_id,product_description
			from stg_order_lines
			group by order_id,product_description,unit_cost) ol on ol.order_id = dl.order_id and ol.product_description = dl.product_description
where ol.product_description is null
group by dl.order_id,
		dispatch_reference,
		dl.product_description,
		products_ordered_together,
		'stg tables',
		CURRENT_TIMESTAMP