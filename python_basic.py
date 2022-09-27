class Classbasic():
    roll_num = 30
    def __init__(self,name,gender,dept,year):
        self.name=name
        self.gender=gender
        self.dept=dept
        self.year=year
    def address(self):
        addr=f"Name={self.name}\n Gender={self.gender}\n Dept={self.dept}\n Year={self.year}"
        return addr
    def new_roll_num(self,new):
        self.roll_num=f"Can rollnum= {self.roll_num - new}"
    def anotheraddress():
        print("Im done basics")
can1=Classbasic("sanjay"," male", "cse", 3)
can2=Classbasic("sanjana","female","ece",3)
can1.new_roll_num(21)
can2.new_roll_num(19)

print(can1.address())
print(can2.address())
print(can1.roll_num)
print(can2.roll_num)
Classbasic.anotheraddress()