import pandas as pd
import tkinter.messagebox as tkmessage

class CSVAccesser() :
    def __init__(self,db_path) :
        self.db_path = db_path
    
    def readCSV(self) :
        try :
            return pd.read_csv(self.db_path,encoding="shift-jis")
        except(FileNotFoundError) :
            tkmessage.showerror("エラー","CSVファイルが存在しません")
            return
    
    def writeCSV(self,df:pd.DataFrame) :
        try :
            df.to_csv(self.db_path,encoding="shift-jis",index=False)
        except(FileExistsError) :
            tkmessage.showerror("エラー","CSVファイルが存在しません")
            return
