#Analytics
# 1 : which payment method have more transactions

def analytics_1():
    query = '''select PaymentMethod,count(*)as No_of_transaction from 
    online_sales group by PaymentMethod order by No_of_transaction desc'''

    return query

def analytics_2():
    query = '''select WarehouseLocation,count(*)as No_of_orders from 
    online_sales group by WarehouseLocation order by No_of_orders desc'''

    return query

import matplotlib.pyplot as plt
import numpy as np

def plot_bar_graph(x,y,title,Xaxis,Yaxis):
    plt.bar(x,y,color='green',width=0.4)
    plt.title(title)
    plt.xlabel(Xaxis)
    plt.ylabel(Yaxis)
    plt.savefig(f'{title}.png')

def analytics_3():
    query = '''select Country,avg(ShippingCost) as Average_shipping_cost from 
    online_sales group by Country order by Average_shipping_cost desc'''

    return query

def plot_bar_graph1(x,y,title,Xaxis,Yaxis):
    plt.bar(x,y,color='red',width=.1)
    plt.title(title)
    plt.xlabel(Xaxis)
    plt.ylabel(Yaxis)
    # plt.savefig(f'{title}.png')
    # plt.show()


def analytics_4():
    query = '''create table if not exists c_transaction as select Country,PaymentMethod,count(*)as 
    count from online_sales group by Country,PaymentMethod'''

    return query
def graph_2(x_values,x_names,y1,y2,y3):
    bar_width = 0.25
    plt.bar(x_values-bar_width,y1,bar_width,color='blue',label='Bank Transfer')
    plt.bar(x_values,y2,bar_width,color='red',label='Credit Card')
    plt.bar(x_values+bar_width,y3,bar_width,color='green',label='Paypall')
    plt.xticks(x_values,x_names)
    # plt.show()
    plt.savefig('graph_2.png')

