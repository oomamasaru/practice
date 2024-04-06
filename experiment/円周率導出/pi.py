"""
3平方の定理を使用して円周率を求める。\n
XYグラフの原点に半径がRADIUSの円の中心があるイメージ\n
円の内側に多角形を作り、各辺の長さを足し合わせることで円周に近づける。\n
計算量を考慮して、円周の1/4を求め、その値を4倍することで円周として扱う。\n
求めた円周をもとに円周率を導出する。\n

Returns:
    None
"""

import math
import numpy

# 半径
RADIUS = 10
# 精度(細かすぎると処理落ちする)
ACCURACY = 10**(-6)

def execute() :
    print("開始")
    # 正のX軸と円周の交点が初期値
    before_x = RADIUS
    before_y = 0
    # 円周
    circumference = 0
    # 「正のX軸と円周の交点」から「正のY軸と円周の交点」を目指すように加算（円周の1/4）
    for i in numpy.arange(ACCURACY,RADIUS,ACCURACY) :
        # RADIUSからループカウンタを引いた値をX（徐々にX軸の負の方向に向かう）
        x_point = RADIUS - i
        # X座標がxの時のY座標
        # （X軸のxから円周に対し直角に線を引き、交点から原点まで線を引いた場合の三角形）
        y_point = demandHeight(x_point,RADIUS)
        # 特定した座標をもとに斜辺の長さを求める。
        hypotenuse = demandHypotenuse(before_x - x_point, y_point - before_y)
        before_x = x_point
        before_y = y_point
        # 斜辺の長さを足し合わせる。
        circumference = circumference + hypotenuse
    
    # 求めた円周から円周率を導出する。
    # (求めたのは円周の1/4なので、求めた数値を4倍したものを円周として扱う)
    pi = (circumference * 4) / 2 * RADIUS / 100
    print(f"円周率\t: {pi}")

    print("終了")

def demandHeight(bottom:float,hypotenuse:float)->float :
    """
    底辺と斜辺から、高さを求める

    Args:
        bottom (float): 底辺
        hypotenuse (float): 斜辺

    Returns:
        float: 高さ
    """
    bottomSquare = bottom ** 2
    hypotenuseSquare = hypotenuse ** 2
    return math.sqrt(hypotenuseSquare - bottomSquare)

def demandHypotenuse(bottom:float,height:float)->float :
    """
    底辺と高さから、斜辺を求める

    Args:
        bottom (float): 底辺
        height (float): 高さ

    Returns:
        float: 斜辺
    """
    bottomSquare = bottom ** 2
    heightSquare = height ** 2
    return math.sqrt(bottomSquare + heightSquare)


if __name__ == "__main__" :
    execute()