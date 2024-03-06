from math import*
class Employee:
    Employee_number = 100
    number_of_employees = 0

    def __init__(self, hours = 40.0):
        self.__employee_number = Employee_number
        self.__regular_hours = hours
        self.__overtime_hours = []
        
    def getemployee_number(self):
        return self.__employee_number
    def getregular_hour(self):
        return self.__regular_hours
    def getovertime_hour(self) :
        return self.__overtime_hours
    
    def setregular_weekly_hour(self,__regular_hours):
        self.__regular_hours = __regular_hours
        
    def total_overrun_time(self):
        sum = 0
        for i in self.__overtime_hours:
            sum += i
        return(sum)
    
    def average_overrun_time(self):
        average = self.total_overrun_time()/len(self.__overtime_hours)
        
    def add_element(self,hours):
        self.__overtime_hours.append(hours)
        
    def __str__(self):
        return "Employee :" +str(self.__employee_number)+"\n"+\
                "Regular Hours :" + str(self.__regular_hours) +"\n"+\
                "Overtime Hours :" + str(self.__overtime_hours)
        
    
    
