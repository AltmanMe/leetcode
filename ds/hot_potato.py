from basic.queue import Queue

def hot_potato(name_list, num):
    que = Queue()
    out_list = list()

    for name in name_list:
        que.enqueue(name)

    while que.size() > 1:
        for i in range(num):
            que.enqueue(que.dequeue())
        out_list.append(que.dequeue())   

    out_list.append(que.dequeue())
    
    return out_list

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))
