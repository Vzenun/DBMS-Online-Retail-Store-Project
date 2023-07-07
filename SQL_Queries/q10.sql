SELECT pro.product_id,pro.product_name,SUM(pro.product_cost*pro.Quantity)
froM Online_Retail_Store.product as pro, Online_Retail_Store.tracking_details as tr,  Online_Retail_Store.orders as o
group by pro.product_id;