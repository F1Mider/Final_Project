import datetime
import numpy as np


class Passenger:
    def __init__(self, arrived_flight, is_citizen):
        self.is_processed = False
        self.is_citizen = is_citizen
        self.flight = arrived_flight
        self.time_processed = None

    def process(self, time):
        if not self.is_processed:
            self.is_processed = True
            self.time_processed = time
            p = self.process_time()
            return int(p*10)/10
        return None


    def process_time(self):
        if self.is_citizen:
            return np.random.normal(0.6,0.05)
        else:
            return np.random.normal(1.2,0.2)


class Flight:
    def __init__(self, arrival):
        self.arrival_time = arrival


class Booth:

    def __init__(self, processing_citizen, open = False, next = 0):
        self.open = open
        self.process_citizen = processing_citizen
        self.next = next

    def open_booth(self):
        self.open = True

    def close_booth(self):
        self.open = False


class Queue:
    def __init__(self):
        """ create an empty queue """
        self.items = []

    def isEmpty(self):
        '''Check if there is passengers in the current waiting queue'''
        return self.items == []

    def enqueue(self, item):
        ''' add new passenger to the end of queue'''
        self.items.insert(0, item)

    def dequeue(self):
        '''remove the passenger from the beginning of the queue'''
        return self.items.pop()

    def size(self):
        '''return the number of items in the queue'''
        return len(self.items)


def average_time(time, pax):
    return sum(time)/pax


def max_time(time):
    return max(time)


def get_citizen_ratio():
    a=-1
    while a<0 or a>1:
        a = np.random.normal(0.5,0.1,1)
    return a


def cleanup_float(float):
    return round(float*10)/10


if __name__ == '__main__':
    run = True
    timespan = 0
    citizen = Queue()
    non_citizen = Queue()
    current_flight = Flight(datetime.time(0,0))
    time_citizen = []
    time_non_citizen = []
    total_arriving = 150
    ratio = get_citizen_ratio()
    citizen_count = int(total_arriving * ratio)
    non_citizen_count = total_arriving - citizen_count
    for i in range(1, citizen_count):
        citizen.enqueue(Passenger(current_flight, True))
    for i in range(1, non_citizen_count):
        non_citizen.enqueue(Passenger(current_flight, False))
    citizen_next = 0
    non_citizen_next_1 = 0
    non_citizen_next_2 = 0
    while run:
        if not citizen.isEmpty():
            if timespan == citizen_next:
                processing = citizen.dequeue()
                citizen_next = processing.process(timespan) + timespan
                citizen_next = cleanup_float(citizen_next)
                time_citizen.append(processing.time_processed - processing.flight.arrival_time.minute)
                print("yes")
        if not non_citizen.isEmpty():
            if timespan == non_citizen_next_1:
                processing = non_citizen.dequeue()
                non_citizen_next_1 = processing.process(timespan) + timespan
                non_citizen_next_1 = cleanup_float(non_citizen_next_1)
                time_non_citizen.append(processing.time_processed - processing.flight.arrival_time.minute)
                print("non")
            if timespan == non_citizen_next_2:
                processing = non_citizen.dequeue()
                non_citizen_next_2 = processing.process(timespan) + timespan
                non_citizen_next_2 = cleanup_float(non_citizen_next_2)
                time_non_citizen.append(processing.time_processed - processing.flight.arrival_time.minute)
                print("non")
        timespan += .1
        timespan = cleanup_float(timespan)
        if timespan == 120:
            run = False

    print(time_citizen)
    print(average_time(time_citizen, total_arriving))
    print(time_non_citizen)
    print(max_time(time_non_citizen))
    #


