from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is Booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"train no: {self.trainNo} is running on time")

    def getfare(self,fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")

t = Train(1597)
t.book("patna", "bangloure")
t.getStatus()
t.getfare("patna", "bangloure")
