create table dwh_dim_dispatches (
dispatch_reference bigint,
dispatch_date timestamp,
quantity_dispatched int,
product_description varchar(255),
data_source varchar(255),
dwh_updated_at timestamp
)