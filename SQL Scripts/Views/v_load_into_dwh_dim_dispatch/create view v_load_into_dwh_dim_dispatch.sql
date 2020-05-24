create or replace view v_load_into_dwh_dim_dispatch as
select distinct dispatch_reference,
		dispatch_date,
		sum(quantity) as quantity_dispatched,
		product_description,
		'stg_dispatch_lines' as data_source,
		CURRENT_TIMESTAMP as dwh_updated_at
from stg_dispatch_lines
group by dispatch_reference,
		 dispatch_date,
		 product_description,
		 'stg_dispatch_lines',
		CURRENT_TIMESTAMP