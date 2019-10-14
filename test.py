# raise案例-2
# 自己定义异常
# 需要注意：　自定义异常必须是系统异常的子类

class DanaValueError(ValueError):
    print("这个是自己定义的error")


