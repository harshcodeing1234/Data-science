# inheritence
class customer:
    def __init__(self,id,name,phone_no,address):
        self.id = id
        self.name = name
        self.__phone_no = phone_no
        self.__address = address
    def showdetails(self):
        print(f"name of customer is: id = {self.id} and name = {self.name}")
class orders(customer,):
    def __init__(self,order_id,order_item,price):
        # super().__init__(order_id,order_item)
        self.order_id = order_id
        self.order_item = order_item
        self.price = price  

    def showorder(self):
        print(f"Order id = {self.order_id}, item = {self.order_item}, Price is Rs.{self.price}")

c1 = customer(12,"Akash kumar",9798817881,"patna,bihar")
o1 = orders(12444,"Boat Headphone",12099)
c1.showdetails()
o1.showorder()

    


    