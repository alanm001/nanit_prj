create table stg_orders (
order_key int key not null AUTO_INCREMENT,
order_id bigint,
order_source varchar(255),
order_date timestamp,
data_source varchar(255),
dwh_updated_at timestamp
)