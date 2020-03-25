# -*- coding: utf-8 -*-
# 元素

alist = [ '测试',2,'你好',6,'test',1,3.2 ]

# list的读取,切片
def list_sel():
    # 通过索引/下标 取元素
    # 正序取 从零开始数
    print(alist[0])
    # 倒叙取 从-1 开始数
    print(alist[-1])
   # 切片
    print(alist[1:5])
    # list 倒排
    print(alist[::-1])

def list_del():
    # list.pop() : 默认删掉最后一位元素 , 并返回删除的那个元素
    ele = alist.pop()
    print(alist)
    print(ele)
    # 填参数: 参数为 索引值 , 填哪个删哪个
    alist.pop(2)
    print(alist)

## 增加元素
def list_add():
    # list.append(元素值)
    alist.append("ysl")
    print(alist)

    # 合并两个list
    blist = [8,8.8]
    alist.extend(blist)
    print(alist)
    alist.append(blist)
    print(alist)

def list_update():
    qlist = [1,2,6,4,5]
    # 更新列表中的元素 , 根据索引进行更新,值写在= 后面 就可以了
    qlist[0] = 100
    print(qlist)

    # 更新第三位 ,改为200
    qlist[2] = 200
    print(qlist)

def list_order_by():
    qlist = [1, 2, 6, 4, 5,5]
    # 从小到大排序
    qlist.sort()
    print(qlist)
    # 从大到小排序 # 指定参数入参: reverse=True
    qlist.sort(reverse=True)
    print(qlist)


def list_distinct():
    vlist = [1,2,2,6,6,4,5]
    # set() : 去重函数s
    s = set(vlist)
    print(s)
    print( type( s ) )
    l = list(s)
    print(type(l))
    print(l)

    # len() : 查看长度
    print(len(l))
    # # set(vlist) : 使用set 方法对 list进行去重,去重后不是list类型,用list() 方法 将这个数据转换成list类型
    # print(type(set(vlist)))
    # vlist = list(set(vlist))
    # print(vlist)
    #
    # # len(): 获取列表的长度,有几个元素 就 返回几
    # print(len(vlist))

if __name__ == '__main__':
    list_distinct()