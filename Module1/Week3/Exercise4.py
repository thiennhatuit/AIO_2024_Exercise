



class myQueue:
    def __init__(self, capacity:int):
        self.__capacity = capacity
        self.__queue_list = []
    
    def is_empty(self):
        return len(self.__queue_list) == 0
    def is_full(self):
        return len(self.__queue_list) == self.__capacity
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        return self.__queue_list.pop(0)
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return
        self.__queue_list.append(value)
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return 
        return self.__queue_list[0]
    
    
queue = myQueue(capacity=5)

queue.enqueue(5)
queue.enqueue(1)
queue.front()

print(queue.is_empty())
        

