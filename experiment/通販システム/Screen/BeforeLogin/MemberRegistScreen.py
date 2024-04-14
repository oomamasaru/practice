import tkinter.messagebox as tkmessage
from ShareInfo import ValueCheck as vc, ShareInfo as si
import pandas as pd

def registMember(root) :
    """
    入力制限を満たしていることを確認し、会員登録処理を実行する

    Args:
        root (BeforeLoginScreen): 画面の親フレーム
    """
    # 画面からの入力内容を取得する
    mem_id_txt = root.memreg_mem_id_txt.get().strip()
    mem_name_txt = root.memreg_mem_name_txt.get() .strip()
    pw_txt = root.memreg_pw_txt.get().strip()

    # 会員IDとパスワードが入力制限を満たしているかチェックする
    if error_msg := vc.memIDCheck(mem_id_txt) :
        tkmessage.showwarning("警告",error_msg)
    if error_msg := vc.passwordCheck(pw_txt) :
        vc.passwordCheck(pw_txt)

    # 会員情報をCSVから取得する
    mem_info_df = root.mem_info_csv.readCSV()

    # 入力された会員IDが既に存在しないかチェック
    # 会員IDが既に使用されている場合はエラー
    if not mem_info_df[mem_info_df[si.MemberInfoColumn.MEMBER_ID]==mem_id_txt].empty :
        tkmessage.showwarning("警告",si.Message.ID_REGISTERED)
        return
    
    # 登録する会員情報を作成
    # 会員区分は一般会員とする
    append_member_df = pd.DataFrame(
        {
            si.MemberInfoColumn.MEMBER_ID : [mem_id_txt],
            si.MemberInfoColumn.MEMBER_NAME : [mem_name_txt],
            si.MemberInfoColumn.PASSWORD : [pw_txt],
            si.MemberInfoColumn.MEMBER_DIV : [si.MemberDiv.NORMAL]
        }
    )
    # 会員情報を更新する
    root.mem_info_csv.writeCSV(pd.concat([mem_info_df,append_member_df]))
    tkmessage.showinfo("会員登録完了",si.Message.REGIST_COMPLETE)

    # ログイン画面に遷移する
    root.showLoginFrame()