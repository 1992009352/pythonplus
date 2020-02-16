import sys

def argv_check_error():
    print("parameter error")
    return 0

def check_int(argv):
    try:
        argv=int(argv)
        return True
    except ValueError:
        return False

#函数：参数是否为指定范围内的整型
def argv_check_int_range(low,high,tg):
#检查是否为范围内的整型数据,边界值为真,边界值传入false时为正负无限
#注：argv传入的时候永远都是str类型数据
    if check_int(tg)==False:
        argv_check_error()
        return 0
    else:
        tg=int(tg)
    if low=='-' and high!='-':
        if tg>high:
            argv_check_error()
    elif low!='-' and high=='-':
        if tg<low:
            argv_check_error()
    elif low!='-' and high!='-':
        if tg<low or tg>high:
            argv_check_error()
    else:
        return 1

if __name__=='__main__':
    #计算税费，并带有错误判断
    test_num=sys.argv[1]
    argv_check_int_range(0,'-',test_num)