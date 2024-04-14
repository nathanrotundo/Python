# super class employee with production worker subclass
class Employee:
    def __init__(self, name, employ_number):
        self.name = name
        self.employ_number = employ_number
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_employ_number(self):
        return self.employ_number
    def set_employ_number(self, employ_number):
        self.employ_number = employ_number
# production worker subclass
class ProductionWorker(Employee):
    def __init__(self, name, employ_number, shift_number, hourly_pay_rate):
        super().__init__(name, employ_number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate
    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate
    def get_shift_number(self):
        if self.shift_number == 1:
            return "Day"
        else:
            return "Night"  # if loop to get day or night shift
    def get_shift_name(self):
        return self.get_shift_number() 

def main():
    print("Enter the following details of the Employee")
    name = input("Enter Employee Name: ")
    employ_number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift_number = int(input("Enter Shift Number (1 or 2): "))

    employee1 = ProductionWorker(name, employ_number, shift_number, pay_rate)
    # method to print the information
    print("Info of Employee:")
    print("Name:", employee1.get_name())
    print("Employee Number:", employee1.get_employ_number())
    print("Shift:", employee1.get_shift_name())
    print("Pay Rate:", employee1.get_hourly_pay_rate())

main()