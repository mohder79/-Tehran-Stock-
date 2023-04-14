import requests 
import pandas as pd
import time
import config as con
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
} # 


# { market data link http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx Data structure : some number i dont now @ time , Overall Index , Overall value , ... @ market data @ order book data @ some number data i dont now

while True :
    try :
        request = requests.get( 'http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx',headers )   
        data = request.text
        
        # symbols data
        df =  pd.DataFrame((data.split('@')[2]).split(';'))
        df = df[0].str.split(",",expand=True)
        df = df.iloc[:,:23] # # select the first 23 columns of the dataframe
        
        # order books data
        ob_df =  pd.DataFrame((data.split('@')[3]).split(';'))
        ob_df = ob_df[0].str.split(",",expand=True)
    except :
        print('Request failed: "Encountered network error"  Retrying in 1 seconds')
        time.sleep(1)


    # print(df.iloc[2])
    # print(len(df))
    
    
    # ['Symbol id for web','Ticker Code to identify the stock','Symbol name','Full Name','Time','Open','Final price','Close','No_Tran','Volume','Value',
    #                       'Low','High','yesterday Final price','EPS','Base volume hajm mabna','wtf','wtf','Groups','Day upper limit ','Day lower limit ','Share Number','market ID 300 Bourse, 303 Fara Bourse, 305 Sandoogha, 309 Payeh, 400 Hagh Bourse, 403 Hagh FaraBourse, 404 H HaghPayeh']




    df.columns = ['Symbol_id','Code','Symbol','Name','Time','Open','Final','Close','No_Tran','Volume','Value',
                        'Low','High','YD_Final','EPS','Base_Vol','wtf','wtf','Groups','Day_Upper','Day_lower','Share_No','M_ID']

    # df = df[['Symbol_id','Symbol','Name','Time','Open','High','Low','Close','Volume','Final','No_Tran','Value',
    #                       'YD_Final','EPS','Base_Vol','Day_Upper','Day_lower','Share_No','M_ID']]

    df = df[df['M_ID'].isin(['300','303','309'])] # i wont just 300 Bourse, 303 Fara Bourse,  309 Payeh
    df['Time'] = df['Time'].apply(lambda f: f[:2]+':'+f[2:4]+':'+f[4:6])   #Time : 122950  to 12:29:50
    # {calculate percentage
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce') # Close price is str to int
    df['YD_Final'] = pd.to_numeric(df['YD_Final'], errors='coerce') # yasterday final price price is str to int
    df['Final'] = pd.to_numeric(df['Final'], errors='coerce') #  final price price is str to int
    df['Close %'] = round((df['Close'] - df['YD_Final'])/df['YD_Final']*100,2)  # percentage change in the closing price 
    df['Final(%)'] = round((df['Final']-df['YD_Final'])/df['YD_Final']*100,2)
    # }
    df['M_ID'] = df['M_ID'].map({'300':'بورس','303':'فرابورس','309':'پایه'}) # market id to market name
    df['Groups'] = df['Groups'].map(con.Groups) # groups id to groups name
    df.reset_index(drop = True)
    print(df.iloc[1])


    #  ['Symbol_id','Order Book Depth','Seller Number','Buyer Number','Buy Price','Sell Price','Buy Volume','Sell Volume']
    ob_df.columns = ['Symbol_id','OB_Depth','Sell_No','Buy_No','Buy_Price','Sell_Price','Buy_Vol','Sell_Vol'] # order book Depth 5
    or1_df = (ob_df[ob_df['OB_Depth']=='1']).copy() 
    or2_df = (ob_df[ob_df['OB_Depth']=='2']).copy() 
    or3_df = (ob_df[ob_df['OB_Depth']=='3']).copy() 
    or4_df = (ob_df[ob_df['OB_Depth']=='4']).copy() 
    or5_df = (ob_df[ob_df['OB_Depth']=='5']).copy() 

    or1_df = or1_df[or1_df['Symbol_id'].isin(df['Symbol_id'])].reset_index(drop = True)
    or2_df = or2_df[or2_df['Symbol_id'].isin(df['Symbol_id'])].reset_index(drop = True)
    or3_df = or3_df[or3_df['Symbol_id'].isin(df['Symbol_id'])].reset_index(drop = True)
    or4_df = or4_df[or4_df['Symbol_id'].isin(df['Symbol_id'])].reset_index(drop = True)
    or5_df = or5_df[or5_df['Symbol_id'].isin(df['Symbol_id'])].reset_index(drop = True)



# ob_df['Name'] = df.apply(lambda row: row['Name'] if row['Symbol_id'] == ob_df['Symbol_id'] else '', axis=1)
# print(len(df))

print((df))


# def symbol_info(name):
#     filtered_rows = df[df['Symbol'] == name]

#     if not filtered_rows.empty:
#         row = filtered_rows.iloc[0]
#         print(row)
#     else:
#         print(f"No rows found with name = {name}")

# symbol_info('فنورد')



    
# }