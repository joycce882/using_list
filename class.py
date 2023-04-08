# friends = ["Tom", "Tom", "Kaven", "Jim", "baijun", "Li"]
# Lucky_numbers = [2, 5, 8, 6, 10]
# print(friends.index("Jim"))
# print(friends.count("Tom"))
# Lucky_numbers.reverse()
# print(Lucky_numbers)
# Lucky_numbers.sort()
# print(Lucky_numbers)
#
# friends2 = friends.copy()
# print(friends2)

# 无返回类型
# def Say_hi(name,age):
#     print("Hello "+name,"you are" +str(age))
#
#
# Say_hi("Mike",20)
# def sum(a,b):
#     sum = a + b
#     return sum
# result = sum(3,8)
# print(result)
class Car:
    def __init__(self, make, mode, year):
        self.make = make
        self.mode = mode
        self.year = year
        self.odometer_reading = 100
    def get_descrptive_name(self):
        long_name = f"{self.make},{self.year},{self.mode}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} mile on it")
    def update_odomater(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't change the odometer!")
    def increase_odomater(self,miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't change the odometer!")


#定义一个使用Car大类的函数
my_new_car = Car("Audi","A4","2020")
print(my_new_car.get_descrptive_name())

# 直接修改属性并显示
my_new_car.odometer_reading = 100
my_new_car.read_odometer()

# 改变里程数，间接修改
my_new_car.update_odomater(50)
# my_new_car.read_odometer()

# 更新里程数
my_new_car.increase_odomater(100)
my_new_car.read_odometer()

#修改里程数
my_new_car.increase_odomater(-20)