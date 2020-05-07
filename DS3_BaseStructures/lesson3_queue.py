'''
队列:是一系列有顺序的元素的集合，新元素加入在队列的一端，这一端叫做'队尾(rear)'
    以有元素的移除发生在队列的另一端，叫做'队首(front)',当以元素被加入到队列之后，
    他就从队尾向队首前进，直到他成为下一个即将被移除队列的元素
先进先出(FIFO):最新被加入的元素处于对尾，在队列中停留最长时间的元素处于队首

-----------------------------------
rear                         front
-----------------------------------

抽象数据类型(ADT):
    Queue() 创建一个空队列对象，无需参数，返回空的队列
    enqueue(item)  将数据项添加到队尾，无返回值
    dequeue()  从队首移出数据项，无需参数，返回值为队首数据项
    isEmpty()   是否队列为空，无需参数，返回值为布尔值
    size()    返回队列中的数据项的个数，无需参数

用python list实现队列
队尾在列表0的位置
enqueue   insert()
dequeue   pop()
'''


# class Queue():
#     def __init__(self):
#         self.items = []
#     def enqueue(self,item):
#         self.items.insert(0,item)
#     def dequeue(self):
#         return self.items.pop()
#     def isEmoty(self):
#         return self.items == []
#     def size(self):
#         return len(self.items)
# q = Queue()
# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)
# print(q.size())
# print(q.isEmoty())
# print(q.dequeue())


# q = Queue()
# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(3)
# q.dequeue()


'''
马铃薯游戏，20s中结束，物品在谁手里，谁将被淘汰
选定一个人作为开始的人经过num个人后，将此人淘汰
'''
from pythonds.basic.queue import Queue

name_list = ['红','明','强','丽','马','王','赵','三','四','五','啦']
num = 7
def send_flower(name_list,num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        n = q.dequeue()
        print(n)
    return q.dequeue()

send_flower(name_list,num)

'''
模拟打印机
'''