# -*- coding: utf-8 -*-

# 单行注释 行首加 #
# 多行注释 上下加三个单引号  ''' '''
# print('hollo word')
# print('你好')

'''
jsdkfjsa
是利空打击发散开来
速度快积分卡
'''


# python 是以 缩进来控制代码层级的
# 基本数据类型 int 整数
def int_demo1():
    aint = 4
    bint = 5
    cint = -1
    print(type(aint))


def int_demo2():
    aint = 4
    bint = 5
    cint = -1
    print(type(aint))


def float_demo1():
    afloat = 0.1
    print(type(afloat))

# int 转换成 float  : float()
def int2float():
    # 2 => to
    aint = 10
    print(aint)
    print(type(aint))
    afloat = float(aint)
    print(afloat)
    print(type(afloat))

# float 转换成 int  : int()
def float2int():
    # 2 => to
    afloat = 10.6
    print(afloat)
    print(type(afloat))
    aint = int(afloat)
    print(aint)
    print(type(aint))

# str 基本操作
def str_demo():
    astr = '这是一句话,你说什么'
    bstr = "这又是一句话"
    print(astr)
    print(type(astr))
    # 索引/下标 , 从0开始数  正序 ,  从-1 开始数 倒叙
    print(astr[0])
    print(astr[-1])

    # 切片  : 从 第一个 索引位置 取到 第二个 索引的前一位
    print(astr[2:5])
    # 后面不填  取到 结束
    print(astr[3:])
    # 前面不填  从头开始取
    print(astr[:3])

    # 倒排
    print(astr[::-1])
    print(astr[::3])
    # str 类型是 有序的

if __name__ == '__main__':
    # int_demo1()
    # int_demo2()
    # float_demo1()
    # int2float()
    # float2int()
    str_demo()