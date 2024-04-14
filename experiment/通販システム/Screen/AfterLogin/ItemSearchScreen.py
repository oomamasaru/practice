from ShareInfo.ShareInfo import ItemInfoColumn as iic
from ShareInfo import ShareInfo as si
import tkinter.messagebox as tkmessage

def displayPreparation(root) :
    """
    商品検索画面の表を更新して出力する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """
    
    # テーブルに行が存在しない場合（初期表示時など）
    if not len(root.itemsrc_item_tree.get_children()) :
        # CSVから取得した商品情報からランダムに15件取得し、テーブルへの出力対象とする
        randam_items_df = root.item_info_csv.readCSV()
        randam_items_df = randam_items_df.sample(15 if randam_items_df.shape[0]>=15 else randam_items_df.shape[0])
        # テーブルを更新する
        itemTreeRefresh(root,randam_items_df.to_dict("records"))
    else :
        # 直前に表示されていたテーブル情報の商品IDを取得し、
        # 各商品の情報をCSVから取得した最新情報に更新する。
        item_info_df = root.item_info_csv.readCSV()
        item_id_list = [item_info[iic.ITEM_ID] for item_info in root.item_tree_list]

        display_data_list = list()
        for item_id in item_id_list :
            target_item_info_list = item_info_df[item_info_df[iic.ITEM_ID]== item_id].to_dict("records")
            display_data_list.append(target_item_info_list[0])
        # テーブルを更新する
        itemTreeRefresh(root,display_data_list)

def searchItem(root) :
    """
    商品検索画面の検索ボタンの押下を契機に、商品情報を検索する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """

    # 入力された検索項目を取得
    item_txt = root.itemsrc_itemsrc_txt.get().strip()
    # 空の場合、CSVからランダムな商品情報を15件を出力する
    if not item_txt :
        # テーブル内の既存データを削除する
        for item in root.itemsrc_item_tree.get_children() :
            root.itemsrc_item_tree.delete(item)
        root.showItemSearchFrame()
        return
    
    # 商品情報をCSVから取得する
    item_info_df = root.item_info_csv.readCSV()
    # 検索欄に入力された文字列で商品名に対してあいまい検索を行う
    search_result_df = item_info_df[item_info_df[iic.ITEM_NAME].str.contains(item_txt)]
    # 該当結果が存在しない場合、エラー
    if search_result_df.empty :
        tkmessage.showwarning("警告",si.Message.ITEM_NOT_FOUND)
        return
    # テーブルを更新する
    itemTreeRefresh(root,search_result_df.to_dict("records"))

def itemTreeRefresh(root,display_data_list:list) :
    """
    パラメータで受け取った表示データをもとに、テーブルを更新する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
        display_data_list (list): テーブルへの表示データ
    """

    # テーブル内の既存データを削除する
    for item in root.itemsrc_item_tree.get_children() :
        root.itemsrc_item_tree.delete(item)

    # パラメータで受け取った表示内容をテーブルに出力する
    for i,display_data_dict in enumerate(display_data_list) :
        root.itemsrc_item_tree.insert(parent="",index="end",iid=i,
                                        values=(display_data_dict[iic.ITEM_ID],
                                                display_data_dict[iic.ITEM_NAME],
                                                display_data_dict[iic.PRICE],
                                                display_data_dict[iic.STOCK]
                                                ))
    # 最新の出力内容を更新して保持する
    root.item_tree_list = display_data_list