import tkinter as tk
from ShareInfo import ShareInfo as si
from CSVAccesser.CSVAccesser import CSVAccesser
from Screen import CreateWidgets as cw
from . import LoginScreen,MemberRegistScreen


class BeforeLoginScreen(tk.Tk):
    """
    ログイン前の画面フレームを生成する
    ・ログイン画面
    ・会員登録画面

    Args:
        tk (tkinter): デスクトップアプリ生成用のライブラリ

    Returns:
        辞書: ログインした会員情報
    """

    # 戻り値に設定する会員情報
    member_info_dict = dict()

    def __init__(self):
        """
        イニシャライザ
        """
        super().__init__()
        # ルート情報の設定
        self.title(si.ScreenTitle.LOGIN)
        self.geometry(f"{si.ScreenSize.BEFORE_LOGIN_WIDTH}x{si.ScreenSize.BEFORE_LOGIN_HEIGHT}")

        # 顧客情報にアクセスするためのアクセサの生成
        self.mem_info_csv = CSVAccesser(si.CSV_Name.MEMBER_INFO)

        # ログイン画面のフレーム
        self.login_frame = tk.Frame(self,width=si.ScreenSize.BEFORE_LOGIN_WIDTH,height=si.ScreenSize.BEFORE_LOGIN_HEIGHT)
        self.login_frame.pack()
        cw.createLoginWidgets(self)

        # 会員登録画面のフレーム
        self.memreg_frame = tk.Frame(self,width=si.ScreenSize.BEFORE_LOGIN_WIDTH,height=si.ScreenSize.BEFORE_LOGIN_HEIGHT)
        self.memreg_frame.pack()
        cw.createMemRegWidgets(self)

        # 最初はログイン画面を表示
        self.showLoginFrame()
    
    def bootScreen(self)->dict :
        """
        ログイン画面を表示する\n
        ログイン前の会員情報の判定、作成を行う

        Returns:
            str: 会員区分
        """
        self.mainloop()
        return self.member_info_dict

    def showLoginFrame(self):
        """
        ログイン画面に遷移する
        """
        self.memreg_frame.pack_forget()
        self.title(si.ScreenTitle.LOGIN)
        self.login_frame.pack()

    def showMemRegFrame(self):
        """
        会員登録画面に遷移する
        """
        self.memreg_frame.pack()
        self.title(si.ScreenTitle.MEMREG)
        self.login_frame.pack_forget()

    def login(self) :
        """
        ログイン処理
        """
        LoginScreen.login(self)


    def registMember(self) :
        """
        会員登録処理
        """
        MemberRegistScreen.registMember(self)
