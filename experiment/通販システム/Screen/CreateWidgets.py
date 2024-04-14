import tkinter as tk
from tkinter import ttk
from ShareInfo import ShareInfo as si
from ShareInfo.ShareInfo import LayoutPosition as lp,InputLimit as il,MemberInfoColumn as mic,ItemInfoColumn as iic,PurchaseHistoryColumn as phc

def createLoginWidgets(root) :
    """
    ログイン画面の設定項目を配置する

    Args:
        root (BeforeLoginScreen): ログイン前の親フレーム
    """
    root.login_lomen_id_lbl = tk.Label(root.login_frame,text="会員ID")
    root.login_lomen_id_lbl.place(x=lp.BEFORE_X_POS_LIST[0],y=lp.BEFORE_Y_POS_LIST[0])
    root.login_pw_lbl = tk.Label(root.login_frame,text="パスワード")
    root.login_pw_lbl.place(x=lp.BEFORE_X_POS_LIST[0],y=lp.BEFORE_Y_POS_LIST[1])
    root.login_mem_id_txt = tk.Entry(root.login_frame,width=15)
    root.login_mem_id_txt.place(x=lp.BEFORE_X_POS_LIST[1],y=lp.BEFORE_Y_POS_LIST[0])
    root.login_pw_txt = tk.Entry(root.login_frame,show="*",width=15)
    root.login_pw_txt.place(x=lp.BEFORE_X_POS_LIST[1],y=lp.BEFORE_Y_POS_LIST[1])
    root.login_login_btn = tk.Button(root.login_frame,text="ログイン",command=root.login)
    root.login_login_btn.place(x=lp.BEFORE_X_POS_LIST[-3],y=lp.BEFORE_Y_POS_LIST[1])
    root.login_mem_regist_btn = tk.Button(root.login_frame,text="会員登録",command=root.showMemRegFrame)
    root.login_mem_regist_btn.place(x=lp.BEFORE_X_POS_LIST[-2],y=lp.BEFORE_Y_POS_LIST[-2])
    root.login_quit_btn = tk.Button(root.login_frame,text="終了",command=root.destroy)
    root.login_quit_btn.place(x=lp.BEFORE_X_POS_LIST[-1],y=lp.BEFORE_Y_POS_LIST[-2])


def createMemRegWidgets(root) :
    """
    会員登録画面の設定項目を配置する

    Args:
        root (BeforeLoginScreen): ログイン前の親フレーム
    """
    root.memreg_men_id_lbl = tk.Label(root.memreg_frame,text="会員ID")
    root.memreg_men_id_lbl.place(x=lp.BEFORE_X_POS_LIST[0],y=lp.BEFORE_Y_POS_LIST[0])
    root.memreg_mem_name_lbl = tk.Label(root.memreg_frame,text="会員名")
    root.memreg_mem_name_lbl.place(x=lp.BEFORE_X_POS_LIST[0],y=lp.BEFORE_Y_POS_LIST[1])
    root.memreg_pw_lbl = tk.Label(root.memreg_frame,text="パスワード")
    root.memreg_pw_lbl.place(x=lp.BEFORE_X_POS_LIST[0],y=lp.BEFORE_Y_POS_LIST[2])
    root.memreg_mem_id_txt = tk.Entry(root.memreg_frame,width=15)
    root.memreg_mem_id_txt.place(x=lp.BEFORE_X_POS_LIST[1],y=lp.BEFORE_Y_POS_LIST[0])
    root.memreg_mem_name_txt = tk.Entry(root.memreg_frame,width=15)
    root.memreg_mem_name_txt.place(x=lp.BEFORE_X_POS_LIST[1],y=lp.BEFORE_Y_POS_LIST[1])
    root.memreg_pw_txt = tk.Entry(root.memreg_frame,show="*",width=15)
    root.memreg_pw_txt.place(x=lp.BEFORE_X_POS_LIST[1],y=lp.BEFORE_Y_POS_LIST[2])
    root.guide_lbl1 = tk.Label(root.memreg_frame,text=f"※{il.ID_MIN_DIGIT}〜{il.ID_MAX_DIGIT}字の英数字")
    root.guide_lbl1.place(x=lp.BEFORE_X_POS_LIST[3],y=lp.BEFORE_Y_POS_LIST[0])
    root.guide_lbl2 = tk.Label(root.memreg_frame,text=f"※{il.PW_MIN_DIGIT}〜{il.PW_MAX_DIGIT}字の英数字")
    root.guide_lbl2.place(x=lp.BEFORE_X_POS_LIST[3],y=lp.BEFORE_Y_POS_LIST[2])
    root.memreg_regist_btn = tk.Button(root.memreg_frame,text="登録",command=root.registMember)
    root.memreg_regist_btn.place(x=lp.BEFORE_X_POS_LIST[-2],y=lp.BEFORE_Y_POS_LIST[-2])
    root.memreg_return_btn = tk.Button(root.memreg_frame,text="戻る",command=root.showLoginFrame)
    root.memreg_return_btn.place(x=lp.BEFORE_X_POS_LIST[-1],y=lp.BEFORE_Y_POS_LIST[-2])

def createAdminWidget(root) :
    """
    管理者画面の設定項目を配置する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """
    root.admin_mem_name_lbl = tk.Label(root.admin_frame,text=f"{root.member_info_dict[mic.MEMBER_NAME]} 様")
    root.admin_mem_name_lbl.place(x=lp.AFTER_X_POS_LIST[-2],y=10)
    root.admin_mem_src_lbl = tk.Label(root.admin_frame,text="会員検索")
    root.admin_mem_src_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[1])
    root.admin_mem_src_txt = tk.Entry(root.admin_frame)
    root.admin_mem_src_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[1])
    root.admin_mem_src_btn = tk.Button(root.admin_frame,text="検索",command=root.searchMember)
    root.admin_mem_src_btn.place(x=lp.AFTER_X_POS_LIST[4],y=lp.AFTER_Y_POS_LIST[1])
    root.admin_mem_tree = ttk.Treeview(root.admin_frame,columns=(mic.MEMBER_ID,mic.MEMBER_NAME,mic.MEMBER_DIV))
    root.admin_mem_tree.bind("<<TreeviewSelect>>",root.selectMemRecord)
    root.admin_mem_tree.column("#0",width=0,stretch="no")
    root.admin_mem_tree.column(mic.MEMBER_ID,anchor=tk.CENTER,width=100)
    root.admin_mem_tree.column(mic.MEMBER_NAME,anchor=tk.CENTER,width=150)
    root.admin_mem_tree.column(mic.MEMBER_DIV,anchor=tk.CENTER,width=100)
    root.admin_mem_tree.heading("#0",text="")
    root.admin_mem_tree.heading(mic.MEMBER_ID,text=mic.MEMBER_ID,anchor=tk.CENTER)
    root.admin_mem_tree.heading(mic.MEMBER_NAME,text=mic.MEMBER_NAME,anchor=tk.CENTER)
    root.admin_mem_tree.heading(mic.MEMBER_DIV,text=mic.MEMBER_DIV,anchor=tk.CENTER)
    root.admin_mem_tree.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[2])
    root.admin_arrival_reg_btn = tk.Button(root.admin_frame,text="入荷登録",command=root.showItemSearchFrame)
    root.admin_arrival_reg_btn.place(x=lp.AFTER_X_POS_LIST[-4],y=lp.AFTER_Y_POS_LIST[-2])
    root.admin_quit_btn = tk.Button(root.admin_frame,text="終了",command=root.destroy)
    root.admin_quit_btn.place(x=lp.AFTER_X_POS_LIST[-2],y=lp.AFTER_Y_POS_LIST[-2])

def createItemSrcWidget(root) :
    """
    商品検索画面の設定項目を配置する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """
    root.itemsrc_mem_name_lbl = tk.Label(root.item_search_frame,text=f"{root.member_info_dict[mic.MEMBER_NAME]} 様")
    root.itemsrc_mem_name_lbl.place(x=lp.AFTER_X_POS_LIST[-2],y=10)
    root.itemsrc_itemsrc_lbl = tk.Label(root.item_search_frame,text="商品検索")
    root.itemsrc_itemsrc_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[1])
    root.itemsrc_itemsrc_txt = tk.Entry(root.item_search_frame)
    root.itemsrc_itemsrc_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[1])
    root.itemsrc_itemsrc_btn = tk.Button(root.item_search_frame,text="検索",command=root.searchItem)
    root.itemsrc_itemsrc_btn.place(x=lp.AFTER_X_POS_LIST[4],y=lp.AFTER_Y_POS_LIST[1])
    root.itemsrc_item_tree = ttk.Treeview(root.item_search_frame, height=15,columns=(iic.ITEM_ID,iic.ITEM_NAME,iic.PRICE,iic.STOCK))
    root.itemsrc_item_tree.column("#0",width=0,stretch="no")
    root.itemsrc_item_tree.bind("<<TreeviewSelect>>",root.selectItemRecord)
    root.itemsrc_item_tree.column(iic.ITEM_ID,anchor=tk.CENTER,width=80)
    root.itemsrc_item_tree.column(iic.ITEM_NAME,anchor=tk.CENTER,width=180)
    root.itemsrc_item_tree.column(iic.PRICE,anchor=tk.CENTER,width=100)
    root.itemsrc_item_tree.column(iic.STOCK,anchor=tk.CENTER,width=100)
    root.itemsrc_item_tree.heading("#0",text="")
    root.itemsrc_item_tree.heading(iic.ITEM_ID,text=iic.ITEM_ID,anchor=tk.CENTER)
    root.itemsrc_item_tree.heading(iic.ITEM_NAME,text=iic.ITEM_NAME,anchor=tk.CENTER)
    root.itemsrc_item_tree.heading(iic.PRICE,text=iic.PRICE,anchor=tk.CENTER)
    root.itemsrc_item_tree.heading(iic.STOCK,text=iic.STOCK,anchor=tk.CENTER)
    root.itemsrc_item_tree.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[2])
    if root.admin_flg :
        root.itemsrc_item_reg_btn = tk.Button(root.item_search_frame,text="新規商品入荷",command=root.showItemFrame)
        root.itemsrc_item_reg_btn.place(x=lp.AFTER_X_POS_LIST[-4],y=lp.AFTER_Y_POS_LIST[-2])
        root.itemsrc_return_btn = tk.Button(root.item_search_frame,text="戻る",command=root.showAdminFrame)
        root.itemsrc_return_btn.place(x=lp.AFTER_X_POS_LIST[-2],y=lp.AFTER_Y_POS_LIST[-2])
    else :
        root.itemsrc_mem_edit_btn = tk.Button(root.item_search_frame,text="会員情報変更",command=root.showMemEditFrame)
        root.itemsrc_mem_edit_btn.place(x=lp.AFTER_X_POS_LIST[-6],y=lp.AFTER_Y_POS_LIST[-2])
        root.itemsrc_history_btn = tk.Button(root.item_search_frame,text="購入履歴",command=root.showHistoryFrame)
        root.itemsrc_history_btn.place(x=lp.AFTER_X_POS_LIST[-4],y=lp.AFTER_Y_POS_LIST[-2])
        root.itemsrc_quit_btn = tk.Button(root.item_search_frame,text="終了",command=root.destroy)
        root.itemsrc_quit_btn.place(x=lp.AFTER_X_POS_LIST[-2],y=lp.AFTER_Y_POS_LIST[-2])

def createHistoryWidgets(root) :
    """
    購入履歴画面の設定項目を配置する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """
    root.history_mem_name_lbl = tk.Label(root.history_frame,text=f"{root.member_info_dict[mic.MEMBER_NAME]} 様")
    root.history_mem_name_lbl.place(x=lp.AFTER_X_POS_LIST[-2],y=10)
    root.history_tree = ttk.Treeview(root.history_frame,height=17,columns=(iic.ITEM_NAME,iic.PRICE,phc.PURCHASE_NUM,phc.PURCHASE_DATE))
    root.history_tree.column("#0",width=0,stretch="no")
    root.history_tree.column(iic.ITEM_NAME,anchor=tk.CENTER,width=150)
    root.history_tree.column(iic.PRICE,anchor=tk.CENTER,width=70)
    root.history_tree.column(phc.PURCHASE_NUM,anchor=tk.CENTER,width=50)
    root.history_tree.column(phc.PURCHASE_DATE,anchor=tk.CENTER,width=100)
    root.history_tree.heading("#0",text="")
    root.history_tree.heading(iic.ITEM_NAME,text=iic.ITEM_NAME,anchor=tk.CENTER)
    root.history_tree.heading(iic.PRICE,text=iic.PRICE,anchor=tk.CENTER)
    root.history_tree.heading(phc.PURCHASE_NUM,text=phc.PURCHASE_NUM,anchor=tk.CENTER)
    root.history_tree.heading(phc.PURCHASE_DATE,text=phc.PURCHASE_DATE,anchor=tk.CENTER)
    root.history_tree.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[1])
    root.history_return_btn = tk.Button(root.history_frame,text="戻る",command=root.showItemSearchFrame)
    root.history_return_btn.place(x=lp.AFTER_X_POS_LIST[-2],y=lp.AFTER_Y_POS_LIST[-2])

def createItemWidgets(root) :
    """
    商品画面の設定項目を配置する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """
    root.item_mem_name_lbl = tk.Label(root.item_frame,text=f"{root.member_info_dict[mic.MEMBER_NAME]} 様")
    root.item_mem_name_lbl.place(x=lp.AFTER_X_POS_LIST[-2],y=10)
    root.item_item_id_lbl = tk.Label(root.item_frame,text="商品ID")
    root.item_item_id_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[1])
    root.item_item_id_txt = tk.Entry(root.item_frame)
    root.item_item_id_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[1])
    root.item_item_name_lbl = tk.Label(root.item_frame,text="商品名")
    root.item_item_name_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[2])
    root.item_item_name_txt = tk.Entry(root.item_frame)
    root.item_item_name_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[2])
    root.item_price_lbl = tk.Label(root.item_frame,text="単価")
    root.item_price_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[3])
    root.item_price_txt = tk.Entry(root.item_frame)
    root.item_price_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[3])
    root.item_stock_lbl = tk.Label(root.item_frame,text="在庫数")
    root.item_stock_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[4])
    root.item_stock_txt = tk.Entry(root.item_frame)
    root.item_stock_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[4])
    if root.admin_flg :
        root.item_arrival_lbl = tk.Label(root.item_frame,text="入荷数")
        root.item_arrival_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[5])
        root.item_arrival_txt = tk.Entry(root.item_frame)
        root.item_arrival_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[5])
    else :
        root.item_purchase_lbl = tk.Label(root.item_frame,text="購入数")
        root.item_purchase_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[5])
        root.item_purchase_txt = tk.Entry(root.item_frame)
        root.item_purchase_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[5])
    root.history_return_btn = tk.Button(root.item_frame,text="登録",command=root.registItem)
    root.history_return_btn.place(x=lp.AFTER_X_POS_LIST[-4],y=lp.AFTER_Y_POS_LIST[-2])
    root.history_return_btn = tk.Button(root.item_frame,text="戻る",command=root.showItemSearchFrame)
    root.history_return_btn.place(x=lp.AFTER_X_POS_LIST[-2],y=lp.AFTER_Y_POS_LIST[-2])

def createMemEditWidgets(root) :
    """
    会員情報変更画面の設定項目を配置する

    Args:
        root (AfterLoginScreen): ログイン後の親フレーム
    """
    root.memedit_mem_name_lbl = tk.Label(root.mem_edit_frame,text=f"{root.member_info_dict[mic.MEMBER_NAME]} 様")
    root.memedit_mem_name_lbl.place(x=lp.AFTER_X_POS_LIST[-2],y=10)
    root.memedit_mem_id_lbl = tk.Label(root.mem_edit_frame,text="会員ID")
    root.memedit_mem_id_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[1])
    root.memedit_mem_id_txt = tk.Entry(root.mem_edit_frame)
    root.memedit_mem_id_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[1])
    root.memedit_edit_mem_name_lbl = tk.Label(root.mem_edit_frame,text="会員名")
    root.memedit_edit_mem_name_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[2])
    root.memedit_edit_mem_name_txt = tk.Entry(root.mem_edit_frame)
    root.memedit_edit_mem_name_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[2])
    root.memedit_regist_btn = tk.Button(root.mem_edit_frame,text="登録",command=root.registMemEdit)
    root.memedit_regist_btn.place(x=lp.AFTER_X_POS_LIST[-4],y=lp.AFTER_Y_POS_LIST[-2])
    root.memedit_return_btn = tk.Button(root.mem_edit_frame,text="戻る",command=root.sortingMemEditReturn)
    root.memedit_return_btn.place(x=lp.AFTER_X_POS_LIST[-2],y=lp.AFTER_Y_POS_LIST[-2])

    if root.admin_flg :
        root.memedit_return_btn["command"] = root.showAdminFrame
        root.memedit_mem_div_lbl = tk.Label(root.mem_edit_frame,text="会員区分")
        root.memedit_mem_div_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[3])
        root.memedit_mem_div_cb = ttk.Combobox(root.mem_edit_frame,
                                               state="readonly",
                                               values=(si.MemberDiv.MEMDIV_DICT[si.MemberDiv.NORMAL],
                                                       si.MemberDiv.MEMDIV_DICT[si.MemberDiv.ADMIN]))
        root.memedit_mem_div_cb.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[3])
    else :
        root.memedit_return_btn["command"] = root.showItemSearchFrame
        root.memedit_password_lbl = tk.Label(root.mem_edit_frame,text="パスワード")
        root.memedit_password_lbl.place(x=lp.AFTER_X_POS_LIST[0],y=lp.AFTER_Y_POS_LIST[3])
        root.guide_lbl1 = tk.Label(root.mem_edit_frame,text=f"※{il.PW_MIN_DIGIT}〜{il.PW_MAX_DIGIT}字の英数字")
        root.guide_lbl1.place(x=lp.BEFORE_X_POS_LIST[-2],y=lp.BEFORE_Y_POS_LIST[3])
        root.memedit_password_txt = tk.Entry(root.mem_edit_frame,show="*")
        root.memedit_password_txt.place(x=lp.AFTER_X_POS_LIST[1],y=lp.AFTER_Y_POS_LIST[3])

    