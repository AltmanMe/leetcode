import random
from basic.queue import Queue

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None
    
    def busy(self):
        if self.current_task:
            return True
        else:
            return False

    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate # unit second

class Task:
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1,21)

    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp

def simulation(num_seconds, pages_per_minute):
    printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for cur_sec in range(num_seconds):
        
        if new_task():
            task = Task(cur_sec)
            print_queue.enqueue(task)
        
        if (not printer.busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            wait_time = next_task.wait_time(cur_sec)
            waiting_times.append(wait_time)
            printer.start_next(next_task)

        printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print('Average Wait {:6.2f} secs {:3} tasks remaining.'.format(average_wait, print_queue.size()))

def new_task():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,20)
