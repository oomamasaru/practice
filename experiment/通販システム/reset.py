import pandas as pd
import ShareInfo.ShareInfo as si
from ShareInfo.ShareInfo import MemberInfoColumn as member_column,ItemInfoColumn as item_column,PurchaseHistoryColumn as purchase_column 
from CSVAccesser.CSVAccesser import CSVAccesser as dba

def execute() :
    member_info_df = pd.DataFrame(
        {
            member_column.MEMBER_ID:["admin"],
            member_column.MEMBER_NAME:["日本 太郎"],
            member_column.PASSWORD:["admin"],
            member_column.MEMBER_DIV:[2]
        }
    )

    item_info_df = pd.DataFrame(
        {
            item_column.ITEM_ID:["I0000001","I0000002","I0000003"],
            item_column.ITEM_NAME:["机","椅子","パソコン"],
            item_column.PRICE:[10000,5000,100000],
            item_column.STOCK:[5,5,5]
        }
    )

    purchase_history_df = pd.DataFrame(
        {
            purchase_column.MEMBER_ID:[],
            purchase_column.ITEM_ID:[],
            purchase_column.PURCHASE_NUM:[],
            purchase_column.PURCHASE_DATE:[]
        }
    )
    mem_info_csv = dba(si.CSV_Name.MEMBER_INFO)
    mem_info_csv.writeCSV(member_info_df)
    item_info_csv = dba(si.CSV_Name.ITEM_INFO)
    item_info_csv.writeCSV(item_info_df)
    purchase_history_csv = dba(si.CSV_Name.PURCHASE_HISTORY)
    purchase_history_csv.writeCSV(purchase_history_df)

if __name__ == "__main__" :
    execute()