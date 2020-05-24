import MySQLdb


try:
    db = MySQLdb.connect("localhost", "root", "pL2017eo(", "nanit")
except Exception:
    "fail to connect to mysql"
c = db.cursor()
try:
    c.execute("""truncate dwh_fact_orders""")
    c.execute("""insert into dwh_fact_orders (
                        order_id,
                        dispatch_reference,
                        product_description,
                        orders_quantity,
                        dispatches_quantity,
                        order_total_price,
                        products_ordered_together,
                        data_source,
                        dwh_updated_at)
                select *
                from v_load_into_dwh_fact_orders """)
    c.execute("""truncate dwh_dim_products""")
    c.execute("""insert into dwh_dim_products (
                        product_code,
                        product_description,
                        unit_cost,
                        data_source,
                        dwh_updated_at)
                select *
                from v_load_into_dwh_dim_products""")
    c.execute("""truncate dwh_dim_dispatches""")
    c.execute("""insert into dwh_dim_dispatches (
                        dispatch_reference,
                        dispatch_date,
                        quantity_dispatched,
                        product_description,
                        data_source,
                        dwh_updated_at)
                select *
                from v_load_into_dwh_dim_dispatch""")
    c.execute("""truncate dwh_dim_orders""")
    c.execute("""insert into dwh_dim_orders (
                        order_id,
                        order_date,
                        order_source,
                        products_quantity,
                        order_total_price,
                        data_source,
                        dwh_updated_at)
                select *
                from v_load_into_dwh_dim_orders""")
    db.commit()
except Exception:
    "fail to execute query"
print(c.rowcount, "Record inserted successfully into dwh fact table")
c.close()
db.close()