create table stg_order_lines (
order_lines_key int key not null AUTO_INCREMENT,
order_id bigint,
product_code varchar(255),
product_description varchar(255),
quantity int,
unit_cost float,
data_source varchar(255),
dwh_updated_at timestamp
)