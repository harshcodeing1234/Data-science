# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

class train:
    def __init__(self,train_name,seats,fare):
        self.train_name = train_name
        self.seats = seats
        self.fare = fare
    
    def book_ticket(self):
        if self.seats > 0:
            self.seats -=1
            print(f"✅ Ticket booked! Seats left: {self.seats}")
        else:
            print("❌ Sorry! No seats available.")
    def get_status(self):
        print(f"🚆 Train: {self.train_name}")
        print(f"Available Seats: {self.seats}")
    
    def get_fare_info(self):
        print(f"💰 Fare per ticket for {self.train_name}: ₹{self.fare}")

t1 = train("Rajdhani Express",3,900)
t1.book_ticket()
t1.get_status()
t1.get_fare_info()
