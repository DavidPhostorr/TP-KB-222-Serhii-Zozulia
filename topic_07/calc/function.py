import datetime
import os
logFile = "logs.txt"
dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir, "logs.txt")
class function:
    
    def ZeroDivisionError(self, x, y):
        while True:
            try:
                if x == 0 or y == 0:
                    return "Impossible"
            except ZeroDivisionError:
                print("Impossible")

    def GetIntValue(self,prompt):
        while True:
            try:
                x = float(input(prompt))
                return x
            except ValueError:
                print("Value error")
                
    def logs(self,choice,n1,n2,result):
        
            date = datetime.datetime.now()
            DateFormat = date.strftime("%Y-%m-%d %H:%M:%S")
            
            with open(path, 'a') as logfile:
                logfile.write(f"{DateFormat}: Operation: {choice}, Number1: {n1}, Number2: {n2}, Result:{result}\n")
        