import requests 
import pandas as pd
import time
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
} # 
# { market data link http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx tihs link for excel 

request = requests.get( 'http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx',headers )
data = request.text
df =  pd.DataFrame((data.split('@')[2]).split(';'))
# print(len(df))
df = df[0].str.split(",",expand=True)
df = df.iloc[:,:23] # # select the first 23 columns of the dataframe
# ['Symbol id for web','Ticker Code to identify the stock','Symbol name','Full Name','Time','Open','Final price','Close','No_Tran','Volume','Value',
#                       'Low','High','yesterday Final price','EPS','Base volume hajm mabna','wtf','wtf','Sector','Day upper limit ','Day lower limit ','Share Number','market ID 300 Bourse, 303 Fara Bourse, 305 Sandoogha, 309 Payeh, 400 Hagh Bourse, 403 Hagh FaraBourse, 404 H HaghPayeh']

df.columns = ['Symbol_id','Code','Symbol','Name','Time','Open','Final','Close','No_Tran','Volume','Value',
                      'Low','High','YD_Final','EPS','Base_Vol','wtf','wtf','Groups','Day_Upper','Day_lower','Share_No','M_ID']

df = df[['Symbol_id','Symbol','Name','Time','Open','High','Low','Close','Volume','Final','No_Tran','Value',
                      'YD_Final','EPS','Base_Vol','Day_Upper','Day_lower','Share_No','M_ID']]

df = df[df['M_ID'].isin(['300','303','309'])] # i wont just 300 Bourse, 303 Fara Bourse,  309 Payeh
df['M_ID'] = df['M_ID'].map({'300':'بورس','303':'فرابورس','309':'پایه'}) # market id to market name


print(df.iloc[1])






    
# }