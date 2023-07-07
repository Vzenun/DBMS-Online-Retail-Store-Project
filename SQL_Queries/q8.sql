select del.contact_number,tr.location,del.delivery_boy_name
from Online_Retail_Store.delivery_boy as del, Online_Retail_Store.tracking_details as tr,  Online_Retail_Store.orders as o
where o.delivery_boy_id=del.delivery_boy_id and o.order_id=tr.track_id;