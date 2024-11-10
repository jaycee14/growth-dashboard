import pandas as pd
from langchain_core.prompts import PromptTemplate


def get_data():
    return pd.read_excel('labourproductivityitls.xls',sheet_name='Productivity Hours', skiprows=4)

def prep_data(data,level):
    new_cols = [x.split('_')[1] for x in data.columns ]
    data.columns=new_cols
    data_level = data.loc[data.level==level]
    data_re_org = data_level.drop(['level','code'],axis=1).melt(id_vars='name', )
    data_re_org.rename(columns={'name':'Region','variable':'Year','value':'Hours'},inplace=True)

    return data_re_org

def create_prompt():    
    template = """
    <|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>
    {system}
    <|eot_id|>
    <|start_header_id|>user<|end_header_id|>
    {user}
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """

    # Added prompt template
    prompt = PromptTemplate(
        input_variables=["system", "user"],
        template=template
    )

    return prompt


