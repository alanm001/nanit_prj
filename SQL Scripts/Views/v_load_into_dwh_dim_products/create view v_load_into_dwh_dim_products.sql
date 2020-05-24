create or replace view v_load_into_dwh_dim_products as
select distinct product_code,
		product_description,
		unit_cost,
		'stg_order_lines' as data_source,
		CURRENT_TIMESTAMP as dwh_updated_at
from stg_order_lines