import datetime
import numpy as np


def load_flight_data() -> dict:
    '''
    This function loads the flight schedule into the program with number of passengers on each flight. By changing the
    schedule, it is possible to simulate different situations of different airports.

    :return: A dictionary with hour as key and a list of flights in that hour.
    '''
    all_flights = initiate_dict_by_hour()
    flights01 = []
    flights01.append(Flight(datetime.time(1,13), 168))
    flights01.append(Flight(datetime.time(1,26), 168))
    all_flights[1] = flights01
    flights03 = []
    flights03.append(Flight(datetime.time(3,46), 146))
    all_flights[3] = flights03
    flights13 = []
    flights13.append(Flight(datetime.time(13, 0), 300))
    flights13.append(Flight(datetime.time(13, 5), 300))
    flights13.append(Flight(datetime.time(13, 13), 300))
    flights13.append(Flight(datetime.time(13, 20), 400))
    flights13.append(Flight(datetime.time(13, 35), 300))
    flights13.append(Flight(datetime.time(13, 45), 350))
    flights13.append(Flight(datetime.time(13, 50), 250))
    flights13.append(Flight(datetime.time(13, 57), 150))
    all_flights[13] = flights13
    flights14 = []
    flights14.append(Flight(datetime.time(14, 3), 300))
    flights14.append(Flight(datetime.time(14, 8), 300))
    flights14.append(Flight(datetime.time(14, 20), 300))
    flights14.append(Flight(datetime.time(14, 25), 400))
    flights14.append(Flight(datetime.time(14, 33), 300))
    flights14.append(Flight(datetime.time(14, 45), 350))
    flights14.append(Flight(datetime.time(14, 50), 250))
    flights14.append(Flight(datetime.time(14, 55), 150))
    all_flights[14] = flights14
    return all_flights


def load_booths_data():
    all_booths = initiate_dict_by_hour()
    all_booths[1] = [5,6]
    all_booths[3] = [2,2]
    all_booths[13] = [13, 11]
    all_booths[14] = [13, 10]
    return all_booths


def initiate_dict_by_hour(param_type=None) -> dict:
    dictionary = {}
    for hour in range(0,24):
        if param_type == list:
            dictionary[hour] = []
        elif param_type == int:
            dictionary[hour] = 0
        else:
            dictionary[hour] = None
    return dictionary


class Passenger:
    '''
    The Passenger class is used to store information about an arriving passenger.
    '''
    def __init__(self, arrived_flight: bool, is_citizen: bool):
        '''
        Parameters:
        is_processed: Boolean value of whether the passenger has cleared immigration
        is_citizen: Boolean value of whether the passenger is a US Citizen
        flight: Flight class object of the flight info the passenger is arriving in
        time_processed: timestamp when the passenger is called by the officer

        :param arrived_flight: The Flight on which passenger is arriving on
        :param is_citizen: Whether the citizen is a US Citizen or not
        '''
        self.is_processed = False
        self.is_citizen = is_citizen
        self.flight = arrived_flight
        self.time_processed = None

    def process(self, time: float) -> float:
        '''

        :param time: The timestamp in 0.1 minutes of when the passenger is called by the officer.
        :return: The time in 0.1 minutes of passenger processed
        '''
        if not self.is_processed:
            self.is_processed = True
            self.time_processed = time
            p = self.process_time()
            return cleanup_float(p)

    def process_time(self):
        if self.is_citizen:
            a = -1
            while a<=0:
                a = np.random.normal(1.0, 0.5)
            return a
        else:
            a = -1
            while a <= 0:
                a = np.random.normal(2.5, 0.4)
            return a


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

    def open_booth(self, time):
        if not self.open:
            self.next = time
            self.open = True

    def close_booth(self):
        if self.open:
            self.open = False

    def change_to_citizen(self):
        self.process_citizen = True

    def change_to_non_citizen(self):
        self.process_citizen = False

    def process_passenger(self, passenger, time, current_hour):
        next_time = passenger.process(time) + time
        if next_time >= 60:
            self.next = cleanup_float(next_time - 60)
        else:
            self.next = cleanup_float(next_time)
        process_min = passenger.time_processed - passenger.flight.arrival_time.minute
        process_hr = (current_hour - passenger.flight.arrival_time.hour) * 60
        return cleanup_float(process_hr + process_min)


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
        a = np.random.normal(0.6, 0.1, 1)
    return a


def cleanup_float(f):
    return round(f*10)/10


def initiate_booths(booths_list, count):
    for i in range(1, count+1):
        booths_list.append(Booth(True, False))
    return booths_list


def renew_booths(booths_list, booth_schedule, timespan):
    cit = 0
    non_cit = 0
    for each_booth in booths_list:
        if cit < booth_schedule[0]:
            each_booth.open_booth(timespan)
            each_booth.change_to_citizen()
            cit += 1
        elif non_cit < booth_schedule[1]:
            each_booth.open_booth(timespan)
            each_booth.change_to_non_citizen()
            non_cit += 1
        else:
            each_booth.close_booth()
    return booths_list


if __name__ == '__main__':
    run = True
    timespan = 0
    citizen = Queue()
    non_citizen = Queue()
    flight_schedule = load_flight_data()
    flight_count = initiate_dict_by_hour(int)
    time_citizen = initiate_dict_by_hour(list)
    time_non_citizen = initiate_dict_by_hour(list)
    total_passenger = initiate_dict_by_hour(int)
    total_citizen = initiate_dict_by_hour(int)
    total_non_citizen = initiate_dict_by_hour(int)
    booths = []
    booths_schedule = load_booths_data()
    initiate_booths(booths, 30)
    for hour in range(0,24):
        flights = Queue()
        next_flight = None
        if flight_schedule[hour] is not None:
            flights.enqueue_list(flight_schedule[hour])
            flight_count[hour] = flights.size()
            next_flight = flights.dequeue()
        timespan = 0
        if booths_schedule[hour] is not None:
            booths = renew_booths(booths, booths_schedule[hour], timespan)
        while timespan < 60.0:
            if next_flight is not None:
                if next_flight.arrival_time.minute == timespan:
                    for i in range(1, next_flight.citizen_count):
                        citizen.enqueue(Passenger(next_flight, True))
                    for i in range(1, next_flight.non_citizen_count):
                        non_citizen.enqueue(Passenger(next_flight, False))
                    total_passenger[hour] += next_flight.passenger_count
                    total_citizen[hour] += next_flight.citizen_count
                    total_non_citizen[hour] += next_flight.non_citizen_count
                    if not flights.isEmpty():
                        next_flight = flights.dequeue()
                    else:
                        next_flight = None
            for booth in booths:
                if timespan >= booth.next:
                    if booth.open:
                        if booth.process_citizen:
                            if not citizen.isEmpty():
                                processing = citizen.dequeue()
                                wait_time = booth.process_passenger(processing, timespan, hour)
                                time_citizen[processing.flight.arrival_time.hour].append(wait_time)
                        else:
                            if not non_citizen.isEmpty():
                                processing = non_citizen.dequeue()
                                wait_time = booth.process_passenger(processing, timespan, hour)
                                time_non_citizen[processing.flight.arrival_time.hour].append(wait_time)
            timespan += .1
            timespan = cleanup_float(timespan)
    timespan = 0
    while not (citizen.isEmpty() and non_citizen.isEmpty()):
        print(hour)
        for booth in booths:
            if timespan >= booth.next:
                if booth.open:
                    if booth.process_citizen:
                        if not citizen.isEmpty():
                            processing = citizen.dequeue()
                            wait_time = booth.process_passenger(processing, timespan, hour)
                            time_citizen[processing.flight.arrival_time.hour].append(wait_time)
                    else:
                        if not non_citizen.isEmpty():
                            processing = non_citizen.dequeue()
                            wait_time = booth.process_passenger(processing, timespan, hour)
                            time_non_citizen[processing.flight.arrival_time.hour].append(wait_time)
        timespan += .1
        timespan = cleanup_float(timespan)
        hour += 1
    print(time_citizen)
    print(time_non_citizen)

    for hour in range(0,24):
        if flight_count[hour] is not 0:
            print("Between "+ str(hour) + " and " + str(hour+1) + " there are " + str(flight_count[hour]) + " flights arrived")
            print("A total of " + str(total_passenger[hour]) + " passengers arrived, in which " + str(total_citizen[hour]) + " are citizens and " + str(total_non_citizen[hour]) + " are non-citizens")
            print("Average waiting time for U.S. citizens: "
                  + str(cleanup_float(average_time(time_citizen[hour], total_citizen[hour]))))
            print("Maximum waiting time for U.S. citizens: "
                  + str(max_time(time_citizen[hour])))
            print("Average waiting time for non-U.S. citizens: "
                  + str(cleanup_float(average_time(time_non_citizen[hour], total_non_citizen[hour]))))
            print("Maximum waiting time for non-U.S. citizens: "
                  + str(max_time(time_non_citizen[hour])))
            print("Average waiting time for all passengers: "
                  + str(cleanup_float(average_time(time_non_citizen[hour] + time_citizen[hour], total_non_citizen[hour] + total_citizen[hour]))))
            print("Maximum waiting time for all passengers: "
                  + str(max_time(time_non_citizen[hour] + time_citizen[hour])))
            print()
            print(str(sum(i <= 15 for i in time_citizen[hour]) + sum(
                i <= 15 for i in time_citizen[1])) + " passengers clear between 0-15 mins")
            print(str(sum(15 < i <= 30 for i in time_citizen[hour]) + sum(
                15 < i <= 30 for i in time_citizen[1])) + " passengers clear between 16-30 mins")
            print(str(sum(30 < i <= 45 for i in time_citizen[hour]) + sum(
                30 < i <= 45 for i in time_citizen[1])) + " passengers clear between 31-45 mins")
            print(str(sum(45 < i <= 60 for i in time_citizen[hour]) + sum(
                45 < i <= 60 for i in time_citizen[1])) + " passengers clear between 46-60 mins")
            print(str(sum(60 < i <= 90 for i in time_citizen[hour]) + sum(
                60 < i <= 90 for i in time_citizen[1])) + " passengers clear between 61-90 mins")
            print(str(sum(90 < i <= 120 for i in time_citizen[hour]) + sum(
                90 < i <= 120 for i in time_citizen[1])) + " passengers clear between 91-120 mins")
            print(str(sum(i > 120 for i in time_citizen[hour]) + sum(
                i > 120 for i in time_citizen[1])) + " passengers clear over 121 mins")
        else:
            print("No flight arrived between "+ str(hour) + " and " + str(hour+1))
        print(" ")
        print("-------------------------------------------------")
        print(" ")


    # print("There are a total of % flights arrived".format(total_flight))
    # print("A total of % passengers arrived, in which % are citizens and % are non-citizens"
    #       .format(total_passenger, total_citizen, total_non_citizen))
    # print("Maximum waiting time for U.S. citizens: " + average_time(time_citizen, total_citizen))
    # print("Average waiting time for U.S. citizens: " + max_time(total_citizen))
    # print("Maximum waiting time for non-U.S. citizens: " + average_time(time_non_citizen, total_non_citizen))
    # print("Average waiting time for non-U.S. citizens: " + max_time(total_non_citizen))
    # print("Maximum waiting time for all passengers: " + average_time(time_non_citizen + time_citizen,
    #                                                                  total_non_citizen + total_citizen))
    # print("Average waiting time for all passengers: " + max_time(time_non_citizen + time_citizen))


