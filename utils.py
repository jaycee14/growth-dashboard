import pandas as pd

def get_data():
    return pd.read_excel('labourproductivityitls.xls',sheet_name='Productivity Hours', skiprows=4)

def prep_data(data,level):
    new_cols = [x.split('_')[1] for x in data.columns ]
    data.columns=new_cols
    data_level = data.loc[data.level==level]
    data_re_org = data_level.drop(['level','code'],axis=1).melt(id_vars='name', )
    data_re_org.rename(columns={'name':'Region','variable':'Year','value':'Hours'},inplace=True)

    return data_re_org



