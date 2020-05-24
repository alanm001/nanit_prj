import json
import requests
import MySQLdb
from datetime import datetime


url='https://nanit-bi-assginment.s3.amazonaws.com/shippingdata.json'
try:
    file = requests.get(url)
except Exception:
    "fail to retrive data"
# check request success & there is data
try:
    obj = json.loads(file.text)
except Exception:
    "fail to parse json"
    #return default value
stg_order = []
stg_ol = []
stg_dl = []
count_disp = 0
#Iterat over the json
for order in obj.get("Order", []):
    order_row = [order["OrderId"], order["OrderDate"], order["OrderSource"], url, datetime.now()]
    stg_order.append(order_row)
    for ol in order.get("OrderLines", []):
        ol_row = [order["OrderId"], ol["ProductCode"], ol["ProductDescription"], ol["Quantity"], ol["UnitCost"], url, datetime.now()]
        stg_ol.append(ol_row)
    dispatches = order.get("Dispatches", [])
    if dispatches is not None:
        count_disp = 0
        for d in order.get("Dispatches", []):
             if order["OrderId"]=='101180131661':
                 print(1)
             for dl in d.get("DispatchedLines", []):
                 skip_adding_dl = 0
                 # for first run
                 if len(stg_dl) > 0:
                     # for accumolate quantity of dl
                     for exsits_product in stg_dl:
                         if exsits_product[1] == d["DispatchReference"] and exsits_product[4] == dl["ProductDescription"]:
                            exsits_product[5] += dl["Quantity"]
                            skip_adding_dl = 1
                            break
                         else:
                             continue
                 if skip_adding_dl == 0:
                    dl_row = [order["OrderId"], d["DispatchReference"], d["DispatchDate"], dl["ProductCode"],
                              dl["ProductDescription"], dl["Quantity"], url, datetime.now()]
                    stg_dl.append(dl_row)
try:
    db = MySQLdb.connect("localhost", "root", "pL2017eo(", "nanit")
except Exception:
    "fail to connect to mysql"
c = db.cursor()
try:
    c.execute("TRUNCATE TABLE stg_orders")
    c.executemany("""INSERT INTO stg_orders (order_id, order_date, order_source, data_source, dwh_updated_at) 
            VALUES (%s, %s, %s ,%s ,%s) """, stg_order)
    c.execute("TRUNCATE TABLE stg_order_lines")
    c.executemany("""INSERT INTO stg_order_lines (order_id, product_code, product_description, quantity, unit_cost, 
            data_source, dwh_updated_at) 
                VALUES (%s, %s, %s ,%s ,%s, %s ,%s) """, stg_ol)
    c.execute("TRUNCATE TABLE stg_dispatch_lines")
    c.executemany("""INSERT INTO stg_dispatch_lines (order_id, dispatch_reference, dispatch_date, product_code, 
            product_description, quantity, data_source, dwh_updated_at) 
                VALUES (%s, %s, %s ,%s ,%s ,%s ,%s, %s) """, stg_dl)
    db.commit()
    print(c.rowcount, "All data was inserted successfully into stg tables")
except Exception:
    "fail to execute query"
c.close()
db.close()

