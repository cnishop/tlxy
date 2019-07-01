import multiprocessing
from time import ctime

def consumer(name,input_q):
    def __init__(self, name):
        self.name = name
    print ("Into consumer:", ctime(), '-----' ,name)
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q",'-----' ,name)
    print ("Out of consumer:", ctime(),'-----' ,name)

def producer(sequence, output_q):
    for item in sequence:
        print ("Into procuder:", ctime())
        output_q.put(item)
        print("put", item, "into q")
        print ("Out of procuder:", ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p1 = multiprocessing.Process (target = consumer, args = ("p1",q))
    cons_p1.start()

    cons_p2 = multiprocessing.Process (target = consumer, args = ("p2",q))
    cons_p2.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()
