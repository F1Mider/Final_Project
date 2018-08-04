import datetime
import numpy as np


def load_flight_data() -> dict:
    """
    This function loads the flight schedule into the program with number of passengers on each flight. By changing the
    schedule, it is possible to simulate different situations of different airports.
    The current flight schedule is predicted based on flights arrived in Chicago O'Hare on August 2nd, 2018. The
    number of passengers is predicted based on aircraft type and destination.

    :return: A dictionary with hour as key and a list of flights in that hour.
    """
    all_flights = initiate_dict_by_hour()
    all_flights[0] = None
    all_flights[1] = []
    all_flights[1].append(Flight(datetime.time(1, 13), 168))
    all_flights[1].append(Flight(datetime.time(1, 26), 168))
    all_flights[2] = None
    all_flights[3] = []
    all_flights[3].append(Flight(datetime.time(3, 46), 146))
    all_flights[4] = []
    all_flights[4].append(Flight(datetime.time(4, 28), 158))
    all_flights[4].append(Flight(datetime.time(4, 59), 173))
    all_flights[5] = []
    all_flights[5].append(Flight(datetime.time(5, 33), 117))
    all_flights[6] = []
    all_flights[6].append(Flight(datetime.time(6, 28), 306))
    all_flights[6].append(Flight(datetime.time(6, 54), 278))
    all_flights[7] = None
    all_flights[8] = []
    all_flights[8].append(Flight(datetime.time(8, 33), 233))
    all_flights[9] = []
    all_flights[9].append(Flight(datetime.time(9, 13), 223))
    all_flights[9].append(Flight(datetime.time(9, 40), 326))
    all_flights[9].append(Flight(datetime.time(9, 43), 156))
    all_flights[10] = []
    all_flights[10].append(Flight(datetime.time(10, 12), 253))
    all_flights[10].append(Flight(datetime.time(10, 31), 213))
    all_flights[10].append(Flight(datetime.time(10, 33), 89))
    all_flights[11] = []
    all_flights[11].append(Flight(datetime.time(11, 00), 253))
    all_flights[11].append(Flight(datetime.time(11, 22), 213))
    all_flights[11].append(Flight(datetime.time(11, 35), 199))
    all_flights[12] = []
    all_flights[12].append(Flight(datetime.time(12, 8), 174))
    all_flights[12].append(Flight(datetime.time(12, 14), 126))
    all_flights[12].append(Flight(datetime.time(12, 33), 243))
    all_flights[12].append(Flight(datetime.time(12, 42), 256))
    all_flights[12].append(Flight(datetime.time(12, 49), 154))
    all_flights[12].append(Flight(datetime.time(12, 58), 172))
    all_flights[13] = []
    all_flights[13].append(Flight(datetime.time(13, 3), 184))
    all_flights[13].append(Flight(datetime.time(13, 9), 332))
    all_flights[13].append(Flight(datetime.time(13, 14), 194))
    all_flights[13].append(Flight(datetime.time(13, 19), 165))
    all_flights[13].append(Flight(datetime.time(13, 25), 254))
    all_flights[13].append(Flight(datetime.time(13, 27), 396))
    all_flights[13].append(Flight(datetime.time(13, 39), 228))
    all_flights[13].append(Flight(datetime.time(13, 43), 176))
    all_flights[13].append(Flight(datetime.time(13, 48), 289))
    all_flights[13].append(Flight(datetime.time(13, 52), 154))
    all_flights[13].append(Flight(datetime.time(13, 55), 287))
    all_flights[13].append(Flight(datetime.time(13, 59), 215))
    all_flights[14] = []
    all_flights[14].append(Flight(datetime.time(14, 4), 273))
    all_flights[14].append(Flight(datetime.time(14, 9), 265))
    all_flights[14].append(Flight(datetime.time(14, 13), 188))
    all_flights[14].append(Flight(datetime.time(14, 16), 265))
    all_flights[14].append(Flight(datetime.time(14, 26), 168))
    all_flights[14].append(Flight(datetime.time(14, 32), 233))
    all_flights[14].append(Flight(datetime.time(14, 39), 322))
    all_flights[14].append(Flight(datetime.time(14, 43), 199))
    all_flights[14].append(Flight(datetime.time(14, 49), 208))
    all_flights[14].append(Flight(datetime.time(14, 55), 200))
    all_flights[15] = []
    all_flights[15].append(Flight(datetime.time(15, 16), 229))
    all_flights[15].append(Flight(datetime.time(15, 22), 180))
    all_flights[15].append(Flight(datetime.time(15, 28), 227))
    all_flights[15].append(Flight(datetime.time(15, 34), 232))
    all_flights[15].append(Flight(datetime.time(15, 41), 384))
    all_flights[15].append(Flight(datetime.time(15, 47), 276))
    all_flights[15].append(Flight(datetime.time(15, 51), 243))
    all_flights[15].append(Flight(datetime.time(15, 55), 235))
    all_flights[15].append(Flight(datetime.time(15, 58), 299))
    all_flights[16] = []
    all_flights[16].append(Flight(datetime.time(16, 7), 238))
    all_flights[16].append(Flight(datetime.time(16, 14), 68))
    all_flights[16].append(Flight(datetime.time(16, 22), 243))
    all_flights[16].append(Flight(datetime.time(16, 31), 154))
    all_flights[16].append(Flight(datetime.time(16, 37), 148))
    all_flights[16].append(Flight(datetime.time(16, 43), 97))
    all_flights[16].append(Flight(datetime.time(16, 53), 382))
    all_flights[17] = []
    all_flights[17].append(Flight(datetime.time(17, 17), 43))
    all_flights[17].append(Flight(datetime.time(17, 28), 220))
    all_flights[17].append(Flight(datetime.time(17, 34), 234))
    all_flights[17].append(Flight(datetime.time(17, 42), 275))
    all_flights[18] = []
    all_flights[18].append(Flight(datetime.time(18, 14), 155))
    all_flights[18].append(Flight(datetime.time(18, 19), 211))
    all_flights[18].append(Flight(datetime.time(18, 26), 178))
    all_flights[18].append(Flight(datetime.time(18, 37), 213))
    all_flights[18].append(Flight(datetime.time(18, 41), 264))
    all_flights[18].append(Flight(datetime.time(18, 44), 193))
    all_flights[18].append(Flight(datetime.time(18, 49), 237))
    all_flights[18].append(Flight(datetime.time(18, 53), 256))
    all_flights[18].append(Flight(datetime.time(18, 57), 223))
    all_flights[19] = []
    all_flights[19].append(Flight(datetime.time(19, 4), 177))
    all_flights[19].append(Flight(datetime.time(19, 9), 165))
    all_flights[19].append(Flight(datetime.time(19, 22), 334))
    all_flights[19].append(Flight(datetime.time(19, 31), 231))
    all_flights[19].append(Flight(datetime.time(19, 38), 187))
    all_flights[19].append(Flight(datetime.time(19, 54), 292))
    all_flights[20] = []
    all_flights[20].append(Flight(datetime.time(20, 14), 334))
    all_flights[20].append(Flight(datetime.time(20, 34), 403))
    all_flights[21] = []
    all_flights[21].append(Flight(datetime.time(21, 17), 241))
    all_flights[21].append(Flight(datetime.time(21, 43), 208))
    all_flights[22] = []
    all_flights[22].append(Flight(datetime.time(22, 8), 206))
    all_flights[23] = []
    all_flights[23].append(Flight(datetime.time(23, 24), 186))
    all_flights[23].append(Flight(datetime.time(23, 34), 168))
    all_flights[23].append(Flight(datetime.time(23, 55), 118))

    return all_flights


def load_booths_data() -> dict:
    """
    This function returns the booths opened in each hour. The ratio of booths for citizens vs non-citizens is predicted.

    :return: A dictionary with hour as key and a list of booths opened for citizens and non-citizens, respectively.
    """
    all_booths = initiate_dict_by_hour()
    all_booths[1] = [6, 5]
    all_booths[3] = [2, 2]
    all_booths[4] = [4, 3]
    all_booths[5] = [8, 6]
    all_booths[6] = [8, 7]
    all_booths[8] = [5, 4]
    all_booths[9] = [6, 5]
    all_booths[10] = [7, 5]
    all_booths[11] = [11, 9]
    all_booths[12] = [8, 7]
    all_booths[13] = [13, 11]
    all_booths[14] = [12, 11]
    all_booths[15] = [13, 12]
    all_booths[16] = [14, 13]
    all_booths[17] = [8, 8]
    all_booths[18] = [14, 12]
    all_booths[19] = [10, 8]
    all_booths[20] = [6, 5]
    all_booths[21] = [7, 6]
    all_booths[22] = [5, 5]
    all_booths[23] = [6, 5]
    return all_booths


def initiate_dict_by_hour(param_type=None) -> dict:
    """
    This function generates an empty dictionary with 24 slots regarding 24 hours of a day.

    :param param_type: The type that the empty dictionary will have by default. Type list for an empty list for each
                        hour; type int for 0 for each hour. By default each hour will be filled with None.
    :return: A dictionary with 24 keys representing 24 hours and default empty value of specified parameter type.
    """
    dictionary = {}
    for each_hour in range(0, 24):
        if param_type == list:
            dictionary[each_hour] = []
        elif param_type == int:
            dictionary[each_hour] = 0
        else:
            dictionary[each_hour] = None
    return dictionary


class Passenger:
    """
    The Passenger class is used to store information about an arriving passenger.
    """
    def __init__(self, arrived_flight: "Flight", is_citizen: bool):
        """
        Parameters:
        is_processed: Boolean value of whether the passenger has cleared immigration
        is_citizen: Boolean value of whether the passenger is a US Citizen
        flight: Flight class object of the flight info the passenger is arriving in
        time_processed: timestamp when the passenger is called by the officer

        :param arrived_flight: The Flight on which passenger is arriving on
        :param is_citizen: Whether the citizen is a US Citizen or not
        """
        self.is_processed = False
        self.is_citizen = is_citizen
        self.flight = arrived_flight
        self.time_processed = None

    def process(self, time: float) -> float:
        """
        This function will record the time this passenger is called by the officer, and how long it takes to process
        this passenger..

        :param time: The timestamp in 0.1 minutes of when the passenger is called by the officer.
        :return: A float number of time taken to process this passenger, in 0.1 minutes.
        """
        if not self.is_processed:
            self.is_processed = True
            self.time_processed = time
            p = self.process_time
            return cleanup_float(p)

    @property
    def process_time(self) -> float:
        """
        This function generates a random number for time taken to process each passenger. It utilizes different
        distribution for citizens vs non-citizens. Note that this distribution is a predicted model and may vary from
        real life.

        :return: A float number of time taken to process this passenger, in 0.1 minutes.
        """
        if self.is_citizen:
            a = -1
            while a <= 0:
                a = np.random.normal(0.6, 0.15)
            return a
        else:
            a = -1
            while a <= 0:
                # a = random.choice([np.random.normal(0.8, 0.25),np.random.normal(1.5, 0.4)])
                a = np.random.normal(1.0, 0.5)
            return a


class Flight:
    """
    This class stores information of a flight, which will be used in other calculations.
    """
    def __init__(self, arrival: datetime.time, count: int):
        """
        Parameters:
        arrival_time: hour and minute when the aircraft arrived at the terminal
        passenger_count: total number of passengers on this flight
        citizen_count: total number of U.S. citizens on this flight, generated randomly
        non_citizen_count: total number of non-U.S. citizens on this flight

        :param arrival: datetime.time of time when the aircraft arrived at the terminal
        :param count: total number of passengers on this flight
        """
        self.arrival_time = arrival
        self.passenger_count = count
        self.citizen_count = int(self.passenger_count * get_citizen_ratio())
        self.non_citizen_count = self.passenger_count - self.citizen_count


class Booth:
    """
    This class stores information of a booth in airport.
    """

    def __init__(self, processing_citizen: bool, opening=False, next_time=0):
        """
        Parameters:
        open: a boolean value of whether the booth is opened or not
        process_citizen: a boolean value of whether this booth is processing citizens.
        next: the timestamp when this booth is able to process next passenger

        :param processing_citizen: A boolean value of whether the booth is processing citizen. Required when creating
                                    a new instance of this class.
        :param opening: A boolean value of whether the booth is opened with default value False.
        :param next_time: The timestamp, in 0.1 minutes, when this booth is able to process next passenger, with
                           default value 0.
        """
        self.open = opening
        self.process_citizen = processing_citizen
        self.next = next_time

    def open_booth(self, time: float):
        """
        This function will open the booth and record the new time available to process next passenger..

        :param time: Timestamp, in 0.1 minutes, when the booth is opened.
        """
        if not self.open:
            self.next = time
            self.open = True

    def close_booth(self):
        """
        This function will shut down the booth
        """
        if self.open:
            self.open = False

    def change_to_citizen(self):
        """
        This function will convert the booth to process citizens.
        """
        self.process_citizen = True

    def change_to_non_citizen(self):
        """
        This function will convert the booth to process non-citizens.
        """
        self.process_citizen = False

    def process_passenger(self, passenger: Passenger, time: float, current_hour: int):
        """
        This function is called when the booth is processing the next passenger. It records the time when this booth is
        available again and the waiting time of the current passenger.

        :param passenger: The passenger that is processed in this booth.
        :param time: The timestamp, in 0.1 minutes, at which the passenger is called.
        :param current_hour: The hour when the passenger is called
        :return: The total waiting time for the passenger to be called.
        """
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
        """
        Thi function defines an empty queue.
        """
        self.queue = []

    def is_empty(self) -> bool:
        """
        This function returns whether the queue is empty.

        :return: A boolean value of whether the queue is empty.
        """
        return self.queue == []

    def enqueue(self, item):
        """
        Adding a new object to the end of the queue

        :param item: The item to be added to the queue
        """
        self.queue.insert(0, item)

    def enqueue_list(self, items):
        """
        Adding a list to the end of the queue, with the first item in list as the first enqueue.

        :param items: The list to be added to the queue.
        """
        for item in items:
            self.queue.insert(0, item)

    def dequeue(self):
        """
        Removes the first item in queue and returns its value.

        :return: The first item in queue.
        """
        return self.queue.pop()

    def size(self):
        """
        Returns the number of items in the queue.

        :return: The number of items in the queue.
        """
        return len(self.queue)


def average_time(time: list, total_passengers: int) -> float:
    """
    Find out the average waiting time from the given list of waiting times and number of passengers.

    :param time: A list of waiting times.
    :param total_passengers: The number of passengers to be calculated.
    :return: The average waiting time for the given group of passengers.
    """
    if total_passengers == 0:
        return 0
    return cleanup_float(sum(time)/total_passengers)


def max_time(time: list):
    """
    Find the maximum waiting time in the given list of times.

    :param time: A list of waiting times.
    :return: The maximum value in the list
    """
    return max(time)


def get_citizen_ratio():
    """
    This function generates a random number of ratio of citizens vs non-citizens. The distribution is predicted and
    may vary from real life.

    :return: The ration of citizens in all passengers.
    """
    a = -1
    while a < 0 or a > 1:
        a = np.random.normal(0.6, 0.1, 1)
    return a


def cleanup_float(f: float):
    """
    This function rounds any float to exactly one tenths.

    :param f: The float to be processed.
    :return: Rounded number from f
    """
    return round(f*10)/10


def initiate_booths(booths_list: list, count: int) -> list:
    """
    This function will generate the specified number of booths.

    :param booths_list: The list of booths that will be processed
    :param count: The number of booths to be added to the list
    :return: The new list of booths with added ones.
    """
    for j in range(1, count+1):
        booths_list.append(Booth(True, False))
    return booths_list


def renew_booths(booths_list, booth_schedule, timestamp):
    """
    This function is called when a new plan of booths is in use.

    :param booths_list: The list of booths to be processed
    :param booth_schedule: The new count of opened booths, as a list with number of booths opened for citizens and
                            non-citizens, respectively.
    :param timestamp: The timestamp, in 0.1 minutes, when the new plan is in effective.
    :return: The processed list of booths with updated status.
    """
    cit = 0
    non_cit = 0
    for each_booth in booths_list:
        if cit < booth_schedule[0]:
            each_booth.open_booth(timestamp)
            each_booth.change_to_citizen()
            cit += 1
        elif non_cit < booth_schedule[1]:
            each_booth.open_booth(timestamp)
            each_booth.change_to_non_citizen()
            non_cit += 1
        else:
            each_booth.close_booth()
    return booths_list


if __name__ == '__main__':

    # initiate variables
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

    # The main iteration that simulates a day of CBP
    for hour in range(0, 24):
        flights = Queue()   # The flights that will be received in this hour
        next_flight = None  # The next flight that will arrive

        # Add flights that will arrive in this hour to the queue
        if flight_schedule[hour] is not None:
            flights.enqueue_list(flight_schedule[hour])
            flight_count[hour] = flights.size()
            next_flight = flights.dequeue()
        timespan = 0    # The main controlling number that represents the current time, in minutes, with 0.1 increments.

        # If there is a new plan for the booths, load it
        if booths_schedule[hour] is not None:
            booths = renew_booths(booths, booths_schedule[hour], timespan)

        # Simulate each 0.1 minutes of current hour
        while timespan < 60.0:

            # Load passengers to the queue if the flight has arrived.
            if next_flight is not None:
                if next_flight.arrival_time.minute == timespan:
                    for i in range(1, next_flight.citizen_count):
                        citizen.enqueue(Passenger(next_flight, True))
                    for i in range(1, next_flight.non_citizen_count):
                        non_citizen.enqueue(Passenger(next_flight, False))
                    total_passenger[hour] += next_flight.passenger_count
                    total_citizen[hour] += next_flight.citizen_count
                    total_non_citizen[hour] += next_flight.non_citizen_count
                    if not flights.is_empty():
                        next_flight = flights.dequeue()
                    else:
                        next_flight = None

            # If a booth is available, process the next passenger in queue
            for booth in booths:
                if timespan >= booth.next:
                    if booth.open:
                        if booth.process_citizen:
                            if not citizen.is_empty():
                                processing = citizen.dequeue()
                                wait_time = booth.process_passenger(processing, timespan, hour)
                                time_citizen[processing.flight.arrival_time.hour].append(wait_time)
                        else:
                            if not non_citizen.is_empty():
                                processing = non_citizen.dequeue()
                                wait_time = booth.process_passenger(processing, timespan, hour)
                                time_non_citizen[processing.flight.arrival_time.hour].append(wait_time)

            # increment
            timespan += .1
            timespan = cleanup_float(timespan)

    # If there are passengers not processed at the end of the day (23:59), continue processing until the line is
    # cleared and no one is waiting.
    hour = 24
    timespan = 0
    while not (citizen.is_empty() and non_citizen.is_empty()):
        print(hour)
        if timespan == 60:
            timespan = 0
            hour += 1
        for booth in booths:
            if timespan >= booth.next:
                if booth.open:
                    if booth.process_citizen:
                        if not citizen.is_empty():
                            processing = citizen.dequeue()
                            wait_time = booth.process_passenger(processing, timespan, hour)
                            print(wait_time)
                            time_citizen[processing.flight.arrival_time.hour].append(wait_time)
                    else:
                        if not non_citizen.is_empty():
                            processing = non_citizen.dequeue()
                            wait_time = booth.process_passenger(processing, timespan, hour)
                            time_non_citizen[processing.flight.arrival_time.hour].append(wait_time)
        timespan += .1
        timespan = cleanup_float(timespan)
    print(time_citizen)
    print(time_non_citizen)

    # Print out the results in the similar way the CBP data is presented.
    for hour in range(0, 24):
        if flight_count[hour] is not 0:
            print("Between " + str(hour) + " and " + str(hour + 1) + " there are "
                  + str(flight_count[hour]) + " flights arrived")
            print("A total of " + str(total_passenger[hour]) + " passengers arrived, in which " 
                  + str(total_citizen[hour]) + " are citizens and "
                  + str(total_non_citizen[hour]) + " are non-citizens")
            print("Average waiting time for U.S. citizens: "
                  + str(average_time(time_citizen[hour], total_citizen[hour])))
            print("Maximum waiting time for U.S. citizens: "
                  + str(max_time(time_citizen[hour])))
            print("Average waiting time for non-U.S. citizens: "
                  + str(average_time(time_non_citizen[hour], total_non_citizen[hour])))
            print("Maximum waiting time for non-U.S. citizens: "
                  + str(max_time(time_non_citizen[hour])))
            print("Average waiting time for all passengers: "
                  + str(average_time(time_non_citizen[hour] + time_citizen[hour],
                                     total_non_citizen[hour] + total_citizen[hour])))
            print("Maximum waiting time for all passengers: "
                  + str(max_time(time_non_citizen[hour] + time_citizen[hour])))
            print()
            print(str(sum(i <= 15 for i in time_citizen[hour]) + sum(
                i <= 15 for i in time_non_citizen[hour])) + " passengers clear between 0-15 mins")
            print(str(sum(15 < i <= 30 for i in time_citizen[hour]) + sum(
                15 < i <= 30 for i in time_non_citizen[hour])) + " passengers clear between 16-30 mins")
            print(str(sum(30 < i <= 45 for i in time_citizen[hour]) + sum(
                30 < i <= 45 for i in time_non_citizen[hour])) + " passengers clear between 31-45 mins")
            print(str(sum(45 < i <= 60 for i in time_citizen[hour]) + sum(
                45 < i <= 60 for i in time_non_citizen[hour])) + " passengers clear between 46-60 mins")
            print(str(sum(60 < i <= 90 for i in time_citizen[hour]) + sum(
                60 < i <= 90 for i in time_non_citizen[hour])) + " passengers clear between 61-90 mins")
            print(str(sum(90 < i <= 120 for i in time_citizen[hour]) + sum(
                90 < i <= 120 for i in time_non_citizen[hour])) + " passengers clear between 91-120 mins")
            print(str(sum(i > 120 for i in time_citizen[hour]) + sum(
                i > 120 for i in time_non_citizen[hour])) + " passengers clear over 121 mins")
        else:
            print("No flight arrived between " + str(hour) + " and " + str(hour+1))
        print(" ")
        print("-------------------------------------------------")
        print(" ")
