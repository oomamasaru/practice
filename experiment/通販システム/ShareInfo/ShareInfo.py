import os
import numpy

class ScreenSize() :
    """
    ログイン前後のそれぞれの画面サイズを定義する
    """
    BEFORE_LOGIN_WIDTH = 500
    BEFORE_LOGIN_HEIGHT = 250
    AFTER_LOGIN_WIDTH = 500
    AFTER_LOGIN_HEIGHT = 500

class CSV_Name() :
    """
    各CSVファイルのパスを相対パスで保持する
    """
    MEMBER_INFO = os.path.abspath(os.getcwd())+"/CSV/会員情報.csv"
    ITEM_INFO = os.path.abspath(os.getcwd())+"/CSV/商品情報.csv"
    PURCHASE_HISTORY = os.path.abspath(os.getcwd())+"/CSV/購入履歴.csv"

class MemberInfoColumn() :
    """
    会員情報CSVのカラム名を定義する
    """
    MEMBER_ID = "会員ID"
    MEMBER_NAME = "会員名"
    PASSWORD = "パスワード"
    MEMBER_DIV = "会員区分"

class MemberDiv() :
    """
    会員区分の情報を定義し、日本語名称とマッピングする
    """
    NORMAL = 1
    ADMIN = 2
    MEMDIV_DICT = {
        NORMAL:"一般会員",
        ADMIN:"管理者"
    }
    REVERSE_MEMDIV_DICT = {
        MEMDIV_DICT[NORMAL]:NORMAL,
        MEMDIV_DICT[ADMIN]:ADMIN
    }

class ItemInfoColumn() :
    """
    商品情報CSVのカラム名を定義する
    """
    ITEM_ID = "商品ID"
    ITEM_NAME = "商品名"
    PRICE="単価"
    STOCK = "在庫数"

class PurchaseHistoryColumn() :
    """
    購入履歴CSVのカラム名を定義する
    """
    MEMBER_ID = "会員ID"
    ITEM_ID = "商品ID"
    PURCHASE_NUM = "購入数"
    PURCHASE_DATE = "購入日"


class InputLimit() :
    """
    会員IDとパスワードについて、入力桁数を定義する
    """
    ID_MIN_DIGIT = 5
    ID_MAX_DIGIT = 15
    PW_MIN_DIGIT = 5
    PW_MAX_DIGIT = 15

class ScreenTitle() :
    """
    各画面名称を定義する
    """
    LOGIN = "ログイン画面"
    MEMREG = "会員登録画面"
    ADMIN = "管理者画面"
    MEMEDIT = "会員情報変更画面"
    ITEMSRC = "商品検索画面"
    ITEM = "商品画面"
    HISTORY = "購入履歴照会画面"

class Message() :
    """
    ポップアップに出力する各メッセージを定義する
    """
    NOT_ENTERED = "未入力の項目があります"
    CHECK_FAILURE = "入力制限を満たしていません"
    ID_REGISTERED = "指定の会員IDは既に使用されています"
    REGIST_COMPLETE = "登録しました"
    LOGIN_FAILURE = "会員IDまたはパスワードに誤りがあります"
    ITEM_NO_ENTERED = "商品名を入力してください"
    ITEM_NOT_FOUND = "該当の商品情報が見つかりませんでした"
    MEMBER_NO_ENTERED = "会員名を入力してください"
    MEMBER_NOT_FOUND = "該当の会員情報が見つかりませんでした"
    MEM_EDIT_SUCCESS = "会員情報を更新しました"
    ITEM_NAME_REGISTERED = "入力された商品名は既に使用されています"
    PARCHASE_NUM_OVER = "購入数が在庫数を超過しています"
    PURCHASE_COMPLETE = "購入しました"

class LayoutPosition() :
    """
    画面の項目配置を行う際のGridをカスタムする
    """
    x_step = 80
    y_step = 40
    BEFORE_X_POS_LIST = numpy.arange(20,ScreenSize.BEFORE_LOGIN_WIDTH,x_step)
    BEFORE_Y_POS_LIST = numpy.arange(20,ScreenSize.BEFORE_LOGIN_HEIGHT,y_step)
    AFTER_X_POS_LIST = numpy.arange(20,ScreenSize.AFTER_LOGIN_WIDTH,x_step)
    AFTER_Y_POS_LIST = numpy.arange(20,ScreenSize.AFTER_LOGIN_HEIGHT,y_step)

