create table dwh_dim_orders (
order_id bigint,
order_date timestamp,
order_source varchar(255),
products_quantity int,
order_total_price float,
data_source varchar(255),
dwh_updated_at timestamp
)