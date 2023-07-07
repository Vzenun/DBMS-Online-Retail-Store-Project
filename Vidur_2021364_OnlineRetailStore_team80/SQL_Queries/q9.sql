SELECT COUNT(DISTINCT pro.Brand_name)
from Online_Retail_Store.product as pro, Online_Retail_Store.tracking_details as tr,  Online_Retail_Store.orders as o
where pro.Brand_name!='Tasigna';