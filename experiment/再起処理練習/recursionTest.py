route_list = list()
pattern_list = list()

def execute():
    """
    Keyに親、Valueに子供を持つ辞書をInputに
    再帰処理を使って孫、ひ孫の代までの流れをまとめる。
    """
    test_dict = {
        "aaaa" : ["bbbb","cccc","dddd"],
        "bbbb" : ["cccc","eeee"],
        "eeee" : ["bbbb"]
    }
    recursion(test_dict,"aaaa")
    print("\n".join(pattern_list))
    

def recursion(test_dict,target) :
    # 終点フラグ（子供なし）
    terminal_flg = True
    # 既出の場合は無限ループになるため、末端に(既出)の文字を結合して、無理やり終点とする。
    if target in route_list :
        target += "(既出)"
    # 親子関係のリストにtargetを追加する。（要素番号が若い方が親）
    route_list.append(target)
    # inputの辞書からtargetの子供情報を取得する。（存在しない場合は空のリスト）
    next_list = test_dict[target] if target in test_dict else list()
    # リストが空になるまでループ（処理済みの要素は消す）
    while next_list :
        # input辞書に子供の情報を持っている場合、終点ではないためパターンに含めない。
        terminal_flg = False
        # 子供情報をtargetに指定し、再帰処理実行。
        recursion(test_dict,next_list.pop(0))
    
    if terminal_flg :
        # 終点の場合のみ、そこまでの経路情報を保持する
        pattern_list.append("\t".join(route_list))
    # 当該target情報は処理済みのため、経路情報から削除する。
    route_list.pop(-1)


if __name__ == "__main__" :
    execute()