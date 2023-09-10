import pandas as pd

'''
This function takes in the customers dataset and an orders data set and returns a dataset where it lists customers who NEVER ordered
'''
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    '''
    have pandas compare ids of the id column in the name table and the customer id in the orders table
    check to see if those ids of these tables are Not equal to each other. If so, make a table with those ids which are not in the order table
    '''
    dontOrder = customers['id'].isin(orders['customerId'])
    dontOrder = dontOrder[['name']].rename(columns={'name': 'Customers'})
    return dontOrder