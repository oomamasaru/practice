from ShareInfo.ShareInfo import MemberInfoColumn as mic
from ShareInfo import ShareInfo as si
from tkinter import messagebox as tkmessage

def displayPreparation(root) :
    """
    テーブル情報を最新に更新する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """

    # 初期表示以外の場合
    if root.member_tree_list :
        # 会員情報をCSVから取得する
        mem_info_df = root.mem_info_csv.readCSV()
        # 直前に表示されていた会員情報の会員IDを取得する
        member_id_list = [member_info[mic.MEMBER_ID] for member_info in root.member_tree_list]

        display_data_list = list()
        # 各会員毎の会員情報を最新情報に更新する
        for member_id in member_id_list :
            target_mem_info_list = mem_info_df[mem_info_df[mic.MEMBER_ID]==member_id].to_dict("records")
            display_data_list.append(target_mem_info_list[0])
        # テーブルを更新する
        adminTreeRefresh(root,display_data_list)

def adminTreeRefresh(root,display_data_list:list) :
    """
    管理者画面のテーブルを更新する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
        display_data_list (list): テーブルに表示するデータ
    """
    # もともと表示されていたデータを削除
    for item in root.admin_mem_tree.get_children() :
        root.admin_mem_tree.delete(item)
    
    # 新しいデータを追加
    for i,display_data_dict in enumerate(display_data_list) :
        root.admin_mem_tree.insert(parent="",index="end",iid=i,
                                    values=(display_data_dict[mic.MEMBER_ID],
                                            display_data_dict[mic.MEMBER_NAME],
                                            si.MemberDiv.MEMDIV_DICT[display_data_dict[mic.MEMBER_DIV]]
                                            ))
    # テーブルの最新情報を更新する
    root.member_tree_list = display_data_list

def searchMember(root) :
    """
    検索ボタンを契機に、会員情報から対象会員を検索する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """
    member_txt = root.admin_mem_src_txt.get().strip()
    # 検索欄が空の場合エラー
    if not member_txt :
        tkmessage.showwarning("警告",si.Message.MEMBER_NO_ENTERED)
        return
    # 会員情報をCSVから取得する
    member_info_df = root.mem_info_csv.readCSV()
    # 入力内容を会員名からあいまい検索する
    search_result_df = member_info_df[member_info_df[mic.MEMBER_NAME].str.contains(member_txt)]
    # 結果が存在しない場合エラー
    if search_result_df.empty :
        tkmessage.showwarning("警告",si.Message.MEMBER_NOT_FOUND)
        return
    # 検索結果をテーブルに設定する
    adminTreeRefresh(root,search_result_df.to_dict("records"))