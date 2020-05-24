create table stg_dispatch_lines (
dispatch_lines_key int key not null AUTO_INCREMENT,
order_id bigint,
dispatch_reference bigint,
dispatch_date timestamp,
product_code varchar(255),
product_description varchar(255),
quantity int,
data_source varchar(255),
dwh_updated_at timestamp
)