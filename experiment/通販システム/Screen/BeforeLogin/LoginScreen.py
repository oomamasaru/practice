import tkinter.messagebox as tkmessage
from ShareInfo import ShareInfo as si

def login(root) :
    """
    入力制限を満たしていることを確認し、
    ログインする画面遷移先は会員区分によって分岐する

    Args:
        root (BeforeLoginScreen): 画面の親フレーム
    """

    # 画面からの入力内容を取得する
    mem_id_txt = root.login_mem_id_txt.get().strip()
    pw_txt = root.login_pw_txt.get().strip()

    # 未入力エラー
    if not mem_id_txt or not pw_txt :
        tkmessage.showwarning("警告",si.Message.NOT_ENTERED)
        return
    
    # 会員情報をCSVから取得する
    mem_info_df = root.mem_info_csv.readCSV()
    
    # 入力された会員IDが存在するかチェック
    # 存在しない場合はエラー
    login_member_df = mem_info_df[mem_info_df[si.MemberInfoColumn.MEMBER_ID]==mem_id_txt]
    if login_member_df.empty  or list(login_member_df[si.MemberInfoColumn.PASSWORD])[0] != pw_txt :
        tkmessage.showwarning("警告",si.Message.LOGIN_FAILURE)
        return
    
    # BeforeLoginScreenの戻り値を生成
    root.member_info_dict = login_member_df.iloc[0].to_dict()
    # BeforeLoginScreenの無限ループ終了
    root.destroy()