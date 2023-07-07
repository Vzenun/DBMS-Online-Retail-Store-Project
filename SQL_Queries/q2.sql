SELECT dealer_id
FROM Online_Retail_Store.dealer as dp
WHERE NOT EXISTS ( SELECT p.product_id
					FROM Online_Retail_Store.product as p
                    WHERE NOT EXISTS ( SELECT dp1.deal_id
										FROM Online_Retail_Store.deal_prod as dp1
                                        WHERE dp1.deal_id=dp.dealer_id and p.product_id=dp1.prod_id));