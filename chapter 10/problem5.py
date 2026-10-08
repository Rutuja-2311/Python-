# Write a class train which has methods to book a ticket, get status(no of seats), get fare information of train runing under indian railwas,
from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro , to):
       print(f"Ticket booked successfully for train number: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train {self.trainNo} has available seats.")

    def getFare(self, fro , to):
        print(f"Ticket fare for train number {self.trainNo} from {fro} to {to} is {randint(100, 1000)}")

t = Train(12345)
t.book("Mumbai", "Pune")
t.getStatus()
t.getFare("Mumbai", "Pune")
