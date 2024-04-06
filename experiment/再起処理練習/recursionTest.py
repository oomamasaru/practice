route_list = list()
pattern_list = list()

def execute():
    test_dict = {
        "aaaa" : ["bbbb","cccc","dddd"],
        "bbbb" : ["cccc","eeee"],
        "eeee" : ["bbbb"]
    }
    recursion(test_dict,"aaaa")
    print("\n".join(pattern_list))
    

def recursion(test_dict,target) :
    exist_next_flg = False
    if target in route_list :
        target += "(既出)"
    route_list.append(target)
    next_list = test_dict[target] if target in test_dict else list()
    while next_list :
        exist_next_flg = True
        recursion(test_dict,next_list[0])
        next_list.pop(0)
    
    if not exist_next_flg :
        pattern_list.append("¥t".join(route_list))
    route_list.pop(-1)


if __name__ == "__main__" :
    execute()