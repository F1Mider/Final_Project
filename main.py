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
            a = -1
            while a<=0:
                a = np.random.normal(0.6, 0.05)
            return a
        else:
            return np.random.normal(1.2,0.2)


class Flight:
    def __init__(self, arrival, count):
        self.arrival_time = arrival
        self.passenger_count = count
        self.citizen_count = int(self.passenger_count * get_citizen_ratio())
        self.non_citizen_count = self.passenger_count - self.citizen_count


class Booth:

    def __init__(self, processing_citizen, opening = False, next_time = 0):
        self.open = opening
        self.process_citizen = processing_citizen
        self.next = next_time

    def open_booth(self):
        self.open = True

    def close_booth(self):
        self.open = False

    def process_passenger(self, passenger, timespan):
        next_time = passenger.process(timespan) + timespan
        self.next = cleanup_float(next_time)
        return cleanup_float(passenger.time_processed - passenger.flight.arrival_time.minute)


class Queue:
    def __init__(self):
        """ create an empty queue """
        self.queue = []

    def isEmpty(self):
        '''Check if there is passengers in the current waiting queue'''
        return self.queue == []

    def enqueue(self, item):
        ''' add new passenger to the end of queue'''
        self.queue.insert(0, item)

    def enqueue_list(self, items):
        ''' add a list of items to the end of queue'''
        for item in items:
            self.queue.insert(0, item)

    def dequeue(self):
        '''remove the passenger from the beginning of the queue'''
        return self.queue.pop()

    def size(self):
        '''return the number of items in the queue'''
        return len(self.queue)


def average_time(time, pax):
    if pax == 0:
        return 0
    return sum(time)/pax


def max_time(time):
    return max(time)


def get_citizen_ratio():
    a = -1
    while a < 0 or a > 1:
        a = np.random.normal(0.5, 0.1, 1)
    return a


def cleanup_float(f):
    return round(f*10)/10


def initiate_booths(booths_list, count, process_citizen):
    for i in range(1, count+1):
        booths_list.append(Booth(process_citizen, True))
    return booths_list


if __name__ == '__main__':
    run = True
    timespan = 0
    citizen = Queue()
    non_citizen = Queue()
    flight_schedule = {}
    for hour in range(0,24):
        flight_schedule[hour] = None
    flights = []
    flights.append(Flight(datetime.time(13, 0), 150))
    flights.append(Flight(datetime.time(13, 5), 287))
    flights.append(Flight(datetime.time(13, 13), 212))
    flights.append(Flight(datetime.time(13, 20), 450))
    flights.append(Flight(datetime.time(13, 35), 98))
    flights.append(Flight(datetime.time(13, 45), 55))
    flights.append(Flight(datetime.time(13, 50), 234))
    flights.append(Flight(datetime.time(13, 57), 15))
    flight_schedule[13] = flights
    time_citizen = []
    time_non_citizen = []
    total_passenger = 0
    total_citizen = 0
    total_non_citizen = 0
    booths = []
    initiate_booths(booths, 6, True)
    initiate_booths(booths, 8, False)
    for hour in range(0,24):
        flights = Queue()
        next_flight = None
        if flight_schedule[hour] is not None:
            flights.enqueue_list(flight_schedule[hour])
            next_flight = flights.dequeue()
        timespan = 0
        while timespan < 60.0:
            if next_flight is not None:
                if timespan == 0.1:
                    print(0.1)
                if next_flight.arrival_time.minute == timespan:
                    print(timespan)
                    for i in range(1, next_flight.citizen_count):
                        citizen.enqueue(Passenger(next_flight, True))
                    for i in range(1, next_flight.non_citizen_count):
                        non_citizen.enqueue(Passenger(next_flight, False))
                    total_passenger += next_flight.passenger_count
                    total_citizen += next_flight.citizen_count
                    total_non_citizen += next_flight.non_citizen_count
                    if not flights.isEmpty():
                        next_flight = flights.dequeue()
                    else:
                        next_flight = None
            for booth in booths:
                if timespan >= booth.next:
                    if booth.process_citizen:
                        if not citizen.isEmpty():
                            processing = citizen.dequeue()
                            wait_time = booth.process_passenger(processing, timespan)
                            time_citizen.append(wait_time)
                    else:
                        if not non_citizen.isEmpty():
                            processing = non_citizen.dequeue()
                            wait_time = booth.process_passenger(processing, timespan)
                            time_non_citizen.append(wait_time)
            timespan += .1
            timespan = cleanup_float(timespan)

    print(total_passenger)
    print(time_citizen)
    print(average_time(time_citizen, total_citizen))
    print(max_time(time_citizen))
    print(time_non_citizen)
    print(average_time(time_non_citizen, total_non_citizen))
    print(max_time(time_non_citizen))
    print(average_time(time_citizen+time_non_citizen, total_passenger))
    print(max_time(time_non_citizen+time_citizen))


