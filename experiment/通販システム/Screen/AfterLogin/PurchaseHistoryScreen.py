from ShareInfo.ShareInfo import ItemInfoColumn as iic,PurchaseHistoryColumn as phc,MemberInfoColumn as mic

def displayPreparation(root) :
    """
    購入履歴画面を表示するための準備処理

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """

    # 購入履歴をCSVから取得
    history_df = root.history_csv.readCSV()
    # ログイン中の会員の購入履歴だけを抽出
    mem_history_list = history_df[history_df[phc.MEMBER_ID]==root.member_info_dict[mic.MEMBER_ID]].to_dict("records")
    # 購入履歴がある場合
    if mem_history_list :
        # 商品情報をCSVから取得
        item_info_df = root.item_info_csv.readCSV()

        # 既存のテーブル行をすべて削除
        for item in root.history_tree.get_children() :
            root.history_tree.delete(item)

        # 購入履歴の件数分ループ
        for i,mem_history_info in enumerate(mem_history_list) :
            # 商品情報データフレームから購入履歴の商品IDに紐づく商品情報を取得する
            target_item_info = item_info_df[item_info_df[iic.ITEM_ID]==mem_history_info[phc.ITEM_ID]].to_dict("records")[0]
            # テーブルに購入履歴情報を追加する
            root.history_tree.insert(parent="",index="end",iid=i,
                                        values=(target_item_info[iic.ITEM_NAME],
                                                target_item_info[iic.PRICE],
                                                mem_history_info[phc.PURCHASE_NUM],
                                                mem_history_info[phc.PURCHASE_DATE]))