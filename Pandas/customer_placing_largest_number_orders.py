import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_counts = {}
    for customer in orders['customer_number']:
        if customer in order_counts:
            order_counts[customer] += 1
        else:
            order_counts[customer] = 1
    
    if not order_counts:
        return pd.DataFrame({'customer_number': []})
    
    max_customer = max(order_counts, key=order_counts.get)
    return pd.DataFrame({'customer_number': [max_customer]})
    
orders = pd.DataFrame({
    'customer_number': [1, 1, 2, 2, 2, 3],
    'order_number': [1, 2, 1, 2, 3, 1]
})
print(largest_orders(orders))
