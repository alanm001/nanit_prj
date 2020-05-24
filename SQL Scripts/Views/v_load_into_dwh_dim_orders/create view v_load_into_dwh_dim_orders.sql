create or replace view v_load_into_dwh_dim_orders as
select o.order_id,
		o.order_date,
		o.order_source,
		sum(quantity) as products_quantity,
		sum(quantity * unit_cost) as order_total_price,
		'stg tables' as data_source,
		CURRENT_TIMESTAMP as dwh_updated_at
from stg_orders o
join stg_order_lines ol on o.order_id =ol.order_id
group by o.order_id,
		o.order_date,
		o.order_source,
		'stg tables',
		CURRENT_TIMESTAMP