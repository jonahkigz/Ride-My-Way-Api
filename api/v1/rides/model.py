#variable that holds all the journeys and their details
rides = []

class RidesModel:

    def __init__(self, from_, to, available_seats, date_and_time): 

    #initialising class attributes
        self.ride_id = self.auto_id(rides)
        self.available_seats = available_seats
        self.date_and_time = date_and_time
        self.from_ = from_
        self.to = to

    def addOne(self):
   
    #creating a dictionary from an object and returning it

        ride = {
            "Id": self.ride_id,
            "available_seats": self.available_seats,
            "date_and_time": self.date_and_time,
            "from_": self.from_,
            "to": self.to
        }
        rides.append(ride)

        return ride
    @staticmethod
    def auto_id(ride_ids):
    #methods aids auto generation of ride_ids
        if ride_ids:
            return ride_ids[-1].get("Id") + 1
        return 1

    @staticmethod
    def returnAll():
    #This methord retrieves or returns all rides in the dictionary
        
        if rides:
            return rides
        return "No existing Ride offer"

    @staticmethod
    def returnOne( ride_id):
    #methord returns a single ride
        for ride in rides:
            if ride.get('Id') == ride_id:
                return ride
            continue

        return "Ride not Found"

    @staticmethod
    def removeOne( ride_id):
    #methord deletes a specified ride
        for count, ride in enumerate(rides):
            if ride.get("Id") == ride_id:
                rides.pop(count)
                return rides
        return "Ride not Found"

   
