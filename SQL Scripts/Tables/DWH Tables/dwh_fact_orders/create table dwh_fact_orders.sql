create table dwh_fact_orders (
order_id bigint,
dispatch_reference bigint,
product_description varchar(255),
orders_quantity int,
dispatches_quantity int,
order_total_price int,
products_ordered_together varchar(255),
data_source varchar(255),
dwh_updated_at timestamp
)