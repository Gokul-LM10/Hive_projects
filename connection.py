import numpy as np
from pyhive import hive
import hive_functions
import analytics
import numpy as np
try:
    c=hive.connect(host='localhost',
                   database="batch88").cursor()
    print('Connectiom established...')
    data_path='/home/gokul/Desktop/data/hive/online_sales_dataset.csv'
    try:
        c.execute(hive_functions.create_table('online_sales',hive_functions.online_sales_columns,','))
        c.execute(hive_functions.insert_data(data_path,'online_sales'))
        print('Table created successfully...')
    except Exception as e:
        print(f'Error in creating table: {e}')

        #Analytics
        # 1 : which payment method have more transactions
    try:
        c.execute(analytics.analytics_1())
        print(f' No of transaction in each payment method: {c.fetchall()}')
    except Exception as e:
        print(f'Error in analytics_1: {e}')

        #2 :No of orders in each warehouses with visualisation
    c.execute(analytics.analytics_2())
    result = c.fetchall()
    # print(f'No of orders in each warehouses: {result}')
    x_values =[]
    y_values =[]
    for i in result:
        if i[0]!='':
            x_values.append(i[0])
            y_values.append(i[1])
    # analytics.plot_bar_graph(x_values,y_values,'No of orders in each warehouses','WarehouseLocation','Count')

    # print(x_values)
    # print(y_values)

       #3 : find the average shipping cost in each country
    c.execute(analytics.analytics_3())
    results = c.fetchall()
    print(f'Average shipping cost in each country: {results}')
    x_values1 =[]
    y_values2 =[]
    for i in results:
        if i[0]!='':
            x_values1.append(i[0])
            y_values2.append(i[1])

    # print(x_values1)
    # print(y_values2)
    # analytics.plot_bar_graph1(x_values1,y_values2,'Average shipping cost in each country','Country','Average shipping cost')

    # 4 find the no of different mode of transaction in each country
    print('No of different mode of transaction in each country:')
    c.execute(analytics.analytics_4())
    # print(c.fetchall())
    c.execute('select distinct Country from c_transaction')
    x_names = c.fetchall()


    c.execute('select * from c_transaction')
    x_values= np.arange(1,len(x_names)+1)
    y_values = c.fetchall()
    print(x_names)
    # print(y_values)
    bt = []
    cc = []
    pp = []
    for i in y_values:
        if i[1]=='Bank Transfer':
            bt.append(i[2])
        elif i[1]=='Credit Card':
            cc.append(i[2])
        elif i[1]=='paypall':
            pp.append(i[2])

    print(bt)
    print(cc)
    print(pp)

    analytics.graph_2(x_values,x_names,bt,cc,pp)


except Exception as e:
    print(f'Error in connection: {e}')

