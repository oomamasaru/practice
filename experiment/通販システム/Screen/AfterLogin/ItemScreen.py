import tkinter as tk
from ShareInfo.ShareInfo import MemberInfoColumn as mic,ItemInfoColumn as iic,PurchaseHistoryColumn as phc
from ShareInfo import ShareInfo as si
from tkinter import messagebox as tkmessage
import pandas as pd
import datetime as dt

ARRIVAL_NUM = "受注数"

def displayPreparation(root) :
    """
    商品画面の各項目の初期値の設定と、活性・非活性制御を行う

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """
    # 非活性状態の項目は値を上書きできないため、全項目を活性状態に変更する
    root.item_item_id_txt["state"] = tk.NORMAL
    root.item_item_name_txt["state"] = tk.NORMAL
    root.item_price_txt["state"] = tk.NORMAL
    root.item_stock_txt["state"] = tk.NORMAL

    # 新規商品登録の場合は商品情報がNoneに設定される。
    # 商品検索画面の表の選択により画面遷移された場合
    if root.selected_item_values != None :
        # 商品情報をCSVから取得する
        item_info_df =  root.item_info_csv.readCSV()
        item_id = root.selected_item_values[0]
        # 商品情報データフレームから対象商品の情報を検索する
        select_mem_info_dict =item_info_df[item_info_df[iic.ITEM_ID]==item_id].iloc[0].to_dict()

        # 項目に値を設定し、必要に応じて非活性状態に変更する
        root.item_item_id_txt.delete(0,tk.END)
        root.item_item_id_txt.insert(0,select_mem_info_dict[iic.ITEM_ID])
        root.item_item_id_txt["state"] = tk.DISABLED

        root.item_item_name_txt.delete(0,tk.END)
        root.item_item_name_txt.insert(0,select_mem_info_dict[iic.ITEM_NAME])
        
        root.item_stock_txt.delete(0,tk.END)
        root.item_stock_txt.insert(0,select_mem_info_dict[iic.STOCK])
        
        root.item_price_txt.delete(0,tk.END)
        root.item_price_txt.insert(0,select_mem_info_dict[iic.PRICE])

        if root.admin_flg :
            root.item_arrival_txt["state"] = tk.NORMAL
            root.item_arrival_txt.delete(0,tk.END)
        else :
            root.item_purchase_txt["state"] = tk.NORMAL
            root.item_purchase_txt.delete(0,tk.END)

            root.item_item_name_txt["state"] = tk.DISABLED
            root.item_price_txt["state"] = tk.DISABLED
    # 新規商品追加ボタンを契機に遷移する場合
    else :
        # 入力可能にするために活性化
        root.item_arrival_txt["state"] = tk.NORMAL

        # 既に入力されている情報を削除する
        root.item_item_id_txt.delete(0,tk.END)
        root.item_item_name_txt.delete(0,tk.END)
        root.item_price_txt.delete(0,tk.END)
        root.item_stock_txt.delete(0,tk.END)
        root.item_arrival_txt.delete(0,tk.END)

    # 項目IDと在庫数は参照用項目のため、必ず非活性にする
    root.item_item_id_txt["state"] = tk.DISABLED
    root.item_stock_txt["state"] = tk.DISABLED

def registItem(root) :
    """
    入力された情報の入力制限を確認し、問題ない場合はCSVに登録する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """

    # 各項目の入力値を取得する
    item_id = root.item_item_id_txt.get()
    item_name = root.item_item_name_txt.get()
    price = root.item_price_txt.get()
    stock = root.item_stock_txt.get()
    input_num = root.item_arrival_txt.get() if root.admin_flg else root.item_purchase_txt.get()

    # 入力チェックを行う
    if not item_name or not price or not input_num :
        tkmessage.showwarning("警告",si.Message.NOT_ENTERED)
        return
    if not price.isnumeric() or not input_num.isnumeric():
        tkmessage.showwarning("警告",si.Message.CHECK_FAILURE)
        return

    # 入力情報を辞書に変換する
    input_item_dict = {
        iic.ITEM_ID : item_id,
        iic.ITEM_NAME : item_name,
        iic.PRICE : int(price),
        iic.STOCK : int(stock) if stock else 0
    }

    # 商品情報をCSVから取得する
    item_info_df = root.item_info_csv.readCSV()

    # 管理者フラグの値に応じて辞書に情報を追加してから、各登録処理に移行する
    if root.admin_flg:
        input_item_dict[ARRIVAL_NUM] = int(input_num)
        updateItem(root,input_item_dict,item_info_df)
    else :
        input_item_dict[phc.PURCHASE_NUM] = int(input_num)
        registItemPurchase(root,input_item_dict,item_info_df)
    
def updateItem(root,input_item_dict:dict,item_info_df:pd.DataFrame) :
    """
    商品の情報を更新する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
        input_item_dict (dict): 画面入力された項目内容
        item_info_df (pd.DataFrame): 項目情報のCSV情報
    """
    item_id = input_item_dict[iic.ITEM_ID]
    write_df = None

    # 項目IDが存在する場合は既存の商品の更新と見なし、
    # 空の場合は新規商品入荷と見なす
    if item_id :
        # 対象の商品レコードだけ更新したいため、対象レコードのINDEXを取得する
        item_id_list = item_info_df[iic.ITEM_ID].to_list()     
        target_index = item_id_list.index(input_item_dict[iic.ITEM_ID])
        # 在庫数から購入数を減算代入する
        item_info_df.loc[target_index,iic.STOCK] = input_item_dict[iic.STOCK] + input_item_dict[ARRIVAL_NUM]
        item_info_df.loc[target_index,iic.ITEM_NAME] = input_item_dict[iic.ITEM_NAME]
        item_info_df.loc[target_index,iic.PRICE] = input_item_dict[iic.PRICE]
        # 書き込み対象のデータフレームに格納する
        write_df = item_info_df

    else :
        # 商品名が既に存在する場合はエラーとする
        if not item_info_df[item_info_df[iic.ITEM_NAME]==input_item_dict[iic.ITEM_NAME]].empty :
            tkmessage.showwarning("警告",si.Message.ITEM_NAME_REGISTERED)
            return
        
        # CSVに登録されている商品IDの最大値を取得し、最大値＋1した値を新規の項目IDとする
        max_item_id = str(item_info_df[iic.ITEM_ID].max())
        item_id_seq_no = int(max_item_id[1:]) + 1
        item_id = "I" + str(item_id_seq_no).zfill(7)

        # 登録する商品情報を作成
        append_item_df = pd.DataFrame(
            {
                iic.ITEM_ID : [item_id],
                iic.ITEM_NAME : [input_item_dict[iic.ITEM_NAME]],
                iic.PRICE : [input_item_dict[iic.PRICE]],
                iic.STOCK : [input_item_dict[ARRIVAL_NUM]]
            }
        )
        # 既存の商品情報と結合したデータフレームを書き込み対象として格納する
        write_df = pd.concat([item_info_df,append_item_df])
    # 商品情報を更新する
    root.item_info_csv.writeCSV(write_df)
    tkmessage.showinfo("登録完了",si.Message.REGIST_COMPLETE)

    # 商品検索画面の表をリフレッシュするために表の要素を削除する
    for item in root.itemsrc_item_tree.get_children() :
        root.itemsrc_item_tree.delete(item)
    # 商品検索画面に遷移する
    root.showItemSearchFrame()

def registItemPurchase(root,input_item_dict:dict,item_info_df:pd.DataFrame) :
    """
    購入した商品を登録する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
        input_item_dict (dict): 画面入力された項目内容
        item_info_df (pd.DataFrame): 項目情報のCSV情報
    """
    # 対象の商品レコードだけ更新したいため、対象レコードのINDEXを取得する
    item_id_list = item_info_df[iic.ITEM_ID].to_list()     
    target_index = item_id_list.index(input_item_dict[iic.ITEM_ID])

    # 在庫数＜購入数の場合エラー
    if input_item_dict[iic.STOCK] < input_item_dict[phc.PURCHASE_NUM] :
        tkmessage.showwarning("警告",si.Message.PARCHASE_NUM_OVER)
        return
    # 在庫数から購入数を減算代入する
    item_info_df.loc[target_index,iic.STOCK] = input_item_dict[iic.STOCK] - input_item_dict[phc.PURCHASE_NUM]
    # 商品情報をCSVに書き込む
    root.item_info_csv.writeCSV(item_info_df)

    # 購入履歴情報を生成する
    append_history_df = pd.DataFrame(
        {
            phc.MEMBER_ID : [root.member_info_dict[mic.MEMBER_ID]],
            phc.ITEM_ID : [input_item_dict[iic.ITEM_ID]],
            phc.PURCHASE_NUM : [input_item_dict[phc.PURCHASE_NUM]],
            phc.PURCHASE_DATE : [getToday()]
        }
    )
    # 購入履歴をCSVから取得する
    history_df = root.history_csv.readCSV()
    # 購入履歴をCSVに書き込む
    root.history_csv.writeCSV(pd.concat([history_df,append_history_df]))
    tkmessage.showinfo("購入完了",si.Message.PURCHASE_COMPLETE)
    root.showItemSearchFrame()

def getToday()->dt :
    """
    登録時のシステム日付をYYYY/MM/DD形式で変換する

    Returns:
        datetime: 登録時のシステム日付
    """
    timedelta = dt.timedelta(hours=9)
    JST = dt.timezone(timedelta,"JST")
    now = dt.datetime.now(JST)
    return now.strftime("%Y/%m/%d")