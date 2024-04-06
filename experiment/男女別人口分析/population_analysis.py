import pandas as pd
import glob

# 調査結果格納フォルダ
INPUT_FOLDER_NAME = "解析対象データ"
OUTPUT_FILE_NAME = "都道府県別_前回集計時との差分.csv"
# 西暦カラム名
YEAR_COLUMN_NAME = "西暦（年）"
# 分析対象区分(1:総数、2:男性、3:女性)
ANALYSIS_DIV = 1
# 分析対象区分ごと対応カラム名
ANALYSIS_DIV_DICT = {1:"人口（総数）",2:"人口（男）",3:"人口（女）"}
# ソート条件カラム
SORT_COLUMN = "都道府県コード"
# 前回集計時との差分カラム
DIFF_COLUMN = "前回集計時との差分"
# 増減割合カラム
RATIO_COLUMN = "増減割合"


def execute() :
    """総務省が集計した人口統計から、人口の推移を計算する。    """
    csv_files = glob.glob(f"{INPUT_FOLDER_NAME}/*.csv")
    target_colmn = ANALYSIS_DIV_DICT[ANALYSIS_DIV]

    # 調査結果格納フォルダ内の全CSVファイルを順次読み出し、マージする
    df = pd.DataFrame()
    for csv_file in csv_files :
        # floatの項目は含まれていないため、小数点付きで読み込まないようにintにキャスト（数値変換できない情報はそのまま）
        df2 = pd.read_csv(csv_file,encoding="shift-jis").astype(int,errors="ignore")
        df = pd.merge(df,df2,"outer") if not df.empty else df2
    
    # データフレームをソートする（第一条件：都道府県コード、第二条件：西暦）
    df = df.sort_values([SORT_COLUMN,YEAR_COLUMN_NAME])

    # 人口が集計されていないレコードを削除する
    df = df.drop(index=df[df[target_colmn]=="-"].index)
    df = df.drop(index=df[pd.isna(df[target_colmn])].index)

    # 分析対象カラムを数値型に変換する。(読み込み時にintにしているはずだが、適用されない…)
    df[target_colmn] = df[target_colmn].astype(int)

    # 各都道府県ごとに、前回集計時の人口との差分を導出する。
    df[DIFF_COLUMN] = df[target_colmn].diff()
    df.loc[df.index<47,[DIFF_COLUMN]]=0
    df[DIFF_COLUMN] = df[DIFF_COLUMN].astype(int)

    # 前回集計時との差分の増減割合を導出する。
    df[RATIO_COLUMN] = df[DIFF_COLUMN] / df[target_colmn]

    # 分析対象外の人口列を削除する。
    df = df.drop([ANALYSIS_DIV_DICT[exclude_div] for exclude_div in ANALYSIS_DIV_DICT if exclude_div != ANALYSIS_DIV],axis=1)

    # 出力フォーマットを整える。
    df[RATIO_COLUMN] = df[RATIO_COLUMN].astype(float).apply(lambda value : "{:.2%}".format(value))
    df[target_colmn] = df[target_colmn].apply(format_with_commas)
    df[DIFF_COLUMN] = df[DIFF_COLUMN].apply(format_with_commas)

    df.to_csv(OUTPUT_FILE_NAME)

def format_with_commas(value) :
    return "{:,d}".format(value)

if __name__ == "__main__" :
    execute()