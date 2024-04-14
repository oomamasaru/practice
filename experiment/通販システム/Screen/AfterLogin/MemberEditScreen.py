import tkinter as tk
from ShareInfo.ShareInfo import MemberInfoColumn as mic
from ShareInfo import ShareInfo as si
from tkinter import messagebox as tkmessage
from ShareInfo import ValueCheck as vc

def displayPreparation(root) :
    """
    管理者フラグに応じて表示項目、活性・非活性の制御を行う

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """

    # 入力内容の編集を可能にするために、一旦活性化する
    root.memedit_mem_id_txt["state"] = tk.NORMAL
    root.memedit_edit_mem_name_txt["state"] = tk.NORMAL

    # 既存の入力内容を削除
    root.memedit_mem_id_txt.delete(0,tk.END)
    root.memedit_edit_mem_name_txt.delete(0,tk.END)

    # 管理者フラグによって表示項目、活性・非活性を制御する
    if root.admin_flg :
        # 管理者の場合、管理者画面で選択された会員情報を会員情報変更画面に表示する
        root.memedit_mem_div_cb["state"] = tk.NORMAL
        root.memedit_mem_div_cb.delete(0,tk.END)
        mem_id = root.edit_mem_values[0]
        mem_info_df =  root.mem_info_csv.readCSV()
        select_mem_info_dict =mem_info_df[mem_info_df[mic.MEMBER_ID]==mem_id].iloc[0].to_dict()
        
        root.memedit_mem_id_txt.insert(0,select_mem_info_dict[mic.MEMBER_ID])
        root.memedit_edit_mem_name_txt.insert(0,select_mem_info_dict[mic.MEMBER_NAME])
        root.memedit_mem_div_cb.set(si.MemberDiv.MEMDIV_DICT[select_mem_info_dict[mic.MEMBER_DIV]])
    else :
        # 一般会員の場合、会員自身の情報を会員情報変更画面に表示する
        root.memedit_password_txt["state"] = tk.NORMAL
        root.memedit_password_txt.delete(0,tk.END)
        root.memedit_mem_id_txt.insert(0,root.member_info_dict[mic.MEMBER_ID])
        root.memedit_edit_mem_name_txt.insert(0,root.member_info_dict[mic.MEMBER_NAME])

    # 会員IDは参照用の項目のため、必ず非活性とする 
    root.memedit_mem_id_txt["state"] = tk.DISABLED

def registMemEdit(root) :
    """
    入力内容の入力制限をチェックし、問題なければ会員情報を更新する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """
    member_id = root.memedit_mem_id_txt.get()
    # 会員情報を取得する
    mem_info_df = root.mem_info_csv.readCSV()
    # 更新対象の会員情報INDEXを取得する
    mem_id_list = mem_info_df[mic.MEMBER_ID].to_list()
    target_index = mem_id_list.index(member_id)

    # 更新対象の会員名を更新する
    mem_info_df.loc[target_index,mic.MEMBER_NAME] = root.memedit_edit_mem_name_txt.get()

    if root.admin_flg :
        mem_div_cb = root.memedit_mem_div_cb.get()
        # 会員区分が未入力の場合エラー
        if not mem_div_cb :
            tkmessage.showwarning("警告",si.Message.CHECK_FAILURE)
            return
        # 更新対象の会員区分を更新する
        mem_info_df.loc[target_index,mic.MEMBER_DIV] = si.MemberDiv.REVERSE_MEMDIV_DICT[mem_div_cb]
    else :
        pw_txt = root.memedit_password_txt.get()
        # パスワードの入力制限をチェックする
        if error_msg := vc.passwordCheck(pw_txt) :
            tkmessage.showwarning("警告",error_msg)
            return
        # 更新対象のパスワードを更新する
        mem_info_df.loc[target_index,mic.PASSWORD] = pw_txt
    # 更新結果をCSVに書き込む
    root.mem_info_csv.writeCSV(mem_info_df)
    tkmessage.showinfo("更新完了",si.Message.MEM_EDIT_SUCCESS)
    # 管理者フラグに応じて戻り先を振り分ける
    root.sortingMemEditReturn()