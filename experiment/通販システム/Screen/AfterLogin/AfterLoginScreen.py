import tkinter as tk
from tkinter import messagebox as tkmessage
import pandas as pd
from ShareInfo import ShareInfo as si
from ShareInfo.ShareInfo import MemberInfoColumn as mic,ItemInfoColumn as iic,PurchaseHistoryColumn as phc
from CSVAccesser.CSVAccesser import CSVAccesser as dba
from Screen import CreateWidgets as cw
from ShareInfo import ValueCheck as vc
import datetime as dt
from . import AdminScreen,MemberEditScreen,ItemScreen,ItemSearchScreen,PurchaseHistoryScreen

class AfterLoginScreen(tk.Tk) :
    """
    ログイン前の画面フレームを生成する
    ・管理者画面
    ・会員情報変更画面
    ・商品検索画面
    ・商品画面
    ・購入履歴画面

    Args:
        tk (tkinter): デスクトップアプリ生成用のライブラリ
    """
    def __init__(self,member_info_dict:dict):
        """
        イニシャライザ

        Args:
            member_info_dict (dict): ログイン中の会員情報
        """
        super().__init__()

        # ログイン中のユーザ情報を保持する
        self.member_info_dict = member_info_dict
        # 管理者かどうかのフラグ（後続処理で多用するため先に定義）
        self.admin_flg = self.member_info_dict[mic.MEMBER_DIV] == si.MemberDiv.ADMIN
        # 商品検索画面のテーブルにて選択された商品情報
        self.selected_item_values = None
        # 管理者画面でテーブルに出力されていた会員情報
        # 会員情報を更新した後で管理者画面に戻ってきた際、同じ会員情報を最新の情報にして出力するために保持する
        self.member_tree_list = list()
        # 商品検索画面でテーブルに出力されていた商品情報
        # 商品情報を更新した後で商品検索画面に戻ってきた際、同じ商品情報を最新の情報にして出力するために保持する
        self.item_tree_list = list()
        # 各CSVのアクセサの定義
        self.mem_info_csv = dba(si.CSV_Name.MEMBER_INFO)
        self.item_info_csv = dba(si.CSV_Name.ITEM_INFO)
        self.history_csv = dba(si.CSV_Name.PURCHASE_HISTORY)

        # 画面サイズの定義
        self.geometry(f"{si.ScreenSize.AFTER_LOGIN_WIDTH}x{si.ScreenSize.AFTER_LOGIN_HEIGHT}")
        
        # 会員情報変更画面の定義
        self.mem_edit_frame = tk.Frame(self,width=si.ScreenSize.AFTER_LOGIN_WIDTH,height=si.ScreenSize.AFTER_LOGIN_HEIGHT)
        self.mem_edit_frame.pack()
        cw.createMemEditWidgets(self)

        # 管理者画面の定義
        self.admin_frame = tk.Frame(self,width=si.ScreenSize.AFTER_LOGIN_WIDTH,height=si.ScreenSize.AFTER_LOGIN_HEIGHT)
        self.admin_frame.pack()
        cw.createAdminWidget(self)

        # 商品検索画面の定義
        self.item_search_frame = tk.Frame(self,width=si.ScreenSize.AFTER_LOGIN_WIDTH,height=si.ScreenSize.AFTER_LOGIN_HEIGHT)
        self.item_search_frame.pack()
        cw.createItemSrcWidget(self)

        # 商品画面の定義
        self.item_frame = tk.Frame(self,width=si.ScreenSize.AFTER_LOGIN_WIDTH,height=si.ScreenSize.AFTER_LOGIN_HEIGHT)
        self.item_frame.pack()
        cw.createItemWidgets(self)

        # 購入履歴画面の定義
        self.history_frame = tk.Frame(self,width=si.ScreenSize.AFTER_LOGIN_WIDTH,height=si.ScreenSize.AFTER_LOGIN_HEIGHT)
        self.history_frame.pack()
        cw.createHistoryWidgets(self)

        # 初回遷移先画面を指定
        # 管理者の場合:管理者画面　、　一般会員の場合:商品検索画面
        if self.admin_flg :
            self.showAdminFrame()
        else :
            self.showItemSearchFrame()

    def bootScreen(self) :
        """
        ログイン後の画面を起動する
        """
        self.mainloop()
    
    def showMemEditFrame(self) :
        """
        会員情報変更画面を表示する
        """
        MemberEditScreen.displayPreparation(self)

        self.title(si.ScreenTitle.MEMEDIT)
        self.mem_edit_frame.pack()
        self.admin_frame.pack_forget()
        self.item_search_frame.pack_forget()
        self.item_frame.pack_forget()
        self.history_frame.pack_forget()
    
    def showAdminFrame(self) :
        """
        管理者画面を表示する
        """
        AdminScreen.displayPreparation(self)

        self.title(si.ScreenTitle.ADMIN)
        self.mem_edit_frame.pack_forget()
        self.admin_frame.pack()
        self.item_search_frame.pack_forget()
        self.item_frame.pack_forget()
        self.history_frame.pack_forget()
    
    def showItemSearchFrame(self) :
        """
        商品検索画面を表示する
        """
        ItemSearchScreen.displayPreparation(self)

        self.title(si.ScreenTitle.ITEMSRC)
        self.mem_edit_frame.pack_forget()
        self.admin_frame.pack_forget()
        self.item_search_frame.pack()
        self.item_frame.pack_forget()
        self.history_frame.pack_forget()

    def showItemFrame(self) :
        """
        商品画面を表示する
        """
        ItemScreen.displayPreparation(self)

        # 商品画面のみ表示する
        self.title(si.ScreenTitle.ITEM)
        self.mem_edit_frame.pack_forget()
        self.admin_frame.pack_forget()
        self.item_search_frame.pack_forget()
        self.item_frame.pack()
        self.history_frame.pack_forget()

    def showHistoryFrame(self) :
        """
        購入履歴画面を表示する
        """
        PurchaseHistoryScreen.displayPreparation(self)

        self.title(si.ScreenTitle.HISTORY)
        self.mem_edit_frame.pack_forget()
        self.admin_frame.pack_forget()
        self.item_search_frame.pack_forget()
        self.item_frame.pack_forget()
        self.history_frame.pack()
    
    def itemArrival(self) :
        """
        新規商品入荷ボタンが押下された場合の処理
        """

        # 商品検索画面の表の選択情報を抹消し、商品画面に遷移する。
        # ItemScreenの表示準備処理にて、表の選択情報がNoneであることによって
        # 新規商品入荷ボタンから遷移したものと認識させる
        self.selected_item_values = None
        self.showItemFrame()

    def searchItem(self) :
        """
        商品検索画面の検索ボタンが押下されたことを契機に商品検索処理を呼び出す
        """
        ItemSearchScreen.searchItem(self)

    def searchMember(self) :
        """
        管理者画面の検索ボタンが押下されたことを契機に会員検索処理を呼び出す
        """
        AdminScreen.searchMember(self)

    def selectMemRecord(self,event) :
        """
        管理者画面の表の特定行が選択されたことを契機に会員情報変更画面への遷移準備を行う

        Args:
            event (TreeviewSelect): 管理者画面のテーブルについて、行が選択されたことを通知する
        """

        # 選択された行の会員情報を取得する
        self.edit_mem_values = self.admin_mem_tree.item(self.admin_mem_tree.focus(),"values")
        # 取得した会員情報が空でない場合、会員情報変更画面に遷移する
        if self.edit_mem_values:
            self.showMemEditFrame()

    def selectItemRecord(self,event) :
        """
        商品検索画面の表の特定行が選択されたことを契機に商品画面への遷移準備を行う

        Args:
            event (TreeviewSelect): 商品検索画面のテーブルについて、行が選択されたことを通知する
        """

        # 選択された行の商品情報を取得する
        self.selected_item_values = self.itemsrc_item_tree.item(self.itemsrc_item_tree.focus(),"values")
        # 取得した商品情報が空でない場合、商品画面に遷移する
        if self.selected_item_values :
            self.showItemFrame()

    def sortingMemEditReturn(self) :
        """
        会員情報変更画面からの戻り先画面を管理者フラグによって仕分ける
        """
        if self.admin_flg :
            self.showAdminFrame()
        else :
            self.showItemSearchFrame()

    def registMemEdit(self) :
        """
        会員情報編集の登録処理を呼び出す
        """
        MemberEditScreen.registMemEdit(self)
    
    def registItem(self) :
        """
        商品情報の登録処理を呼び出す
        """
        ItemScreen.registItem(self)
    
    

        

        

        






