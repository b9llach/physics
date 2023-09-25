from __future__ import annotations
import math
import re

# Go to https://www.online-python.com/
# Delete all of the code you see
# Paste all the code in here into there
# Click the green play button that says run


class Ch1Vector:
    Mag: float = None
    Angle: float = None
    Ax: float = None
    Ay: float = None
    Quadrant: int = None
    Axis: str = None
    Name: str = None

    def __init__(self,Name: str="A", Mag:float=None,Angle: float = None,Ax: float = None,Ay: float = None,Quadrant: int = None,Axis: str = 'x') -> None:
        self.Mag = Mag 
        self.Angle = Angle 
        self.Ax = Ax 
        self.Ay = Ay 
        self.Quadrant = Quadrant 
        self.Axis = Axis 
        self.Name = Name

    def auto_fill(self):
        if self.Ax is None or self.Ay is None:
            print("calcing Ax Ay")
            self.calculate_ax_ay()
        
        if self.Ax is not None and self.Ay is not None:
            self.calculate_ang_mag()  

        if self.Quadrant is None:
            self.calculate_quad()

        return self

    def calculate_ax_ay(self):
        if self.Mag is not None and self.Angle is not None:
            Ax = math.cos(math.radians(self.Angle)) * self.Mag
            Ay = math.sin(math.radians(self.Angle)) * self.Mag
            if self.Quadrant == 1:
                self.Ax = Ax if self.Axis == 'x' else Ay
                self.Ay = Ay if self.Axis == 'x' else Ax
            elif self.Quadrant == 2:
                self.Ax = -Ax if self.Axis == 'x' else Ay
                self.Ay = Ay if self.Axis == 'x' else -Ax
            elif self.Quadrant == 3:
                self.Ax = -Ax if self.Axis == 'x' else -Ay
                self.Ay = -Ay if self.Axis == 'x' else -Ax
            elif self.Quadrant == 4:
                self.Ax = Ax if self.Axis == 'x' else -Ay
                self.Ay = -Ay if self.Axis == 'x' else Ax
            else:
                self.Ax = Ax
                self.Ay = Ay

        return self
    
    def calculate_ang_mag(self):
        if self.Ax is not None and self.Ay is not None:
            self.Mag = math.sqrt((self.Ax ** 2) + (self.Ay ** 2))
            self.Angle = math.degrees(math.atan2(self.Ay, self.Ax) if self.Ax != 0 else math.pi / 2)

    def calculate_quad(self):
        if self.Ax > 0 and self.Ay > 0:
            self.Quadrant = "1"
        elif self.Ax < 0 and self.Ay > 0:
            self.Quadrant = "2"
        elif self.Ax < 0 and self.Ay < 0:
            self.Quadrant = "3"
        elif self.Ax > 0 and self.Ay < 0:
            self.Quadrant = "4"
        elif self.Ax == 0 and self.Ay != 0:
            self.Quadrant = "Y axis"
        elif self.Ax != 0 and self.Ay == 0:
            self.Quadrant = "X axis"
        else:
            self.Quadrant = "Origin"

    def __str__(self) -> str:
        return f"\nName: {self.Name}\n----------\nMag = {self.Mag}\nAngle = {self.Angle}\nAx = {self.Ax}\nAy = {self.Ay}\nQuadrant = {self.Quadrant}\nAxis = {self.Axis}\n"

    def __add__(self, vec2: Ch1Vector) -> Ch1Vector | None:
        return Ch1Vector(Name=f"{self.Name} + {vec2.Name}",Ax=self.Ax + vec2.Ax, Ay=self.Ay + vec2.Ay).auto_fill() if self.Ax is not None and self.Ay is not None else None
    
    def __sub__(self, vec2: Ch1Vector) -> Ch1Vector | None:
        return Ch1Vector(Name=f"{self.Name} - {vec2.Name}",Ax=self.Ax - vec2.Ax, Ay=self.Ay - vec2.Ay).auto_fill() if self.Ax is not None and self.Ay is not None else None
    
    def __mul__(self, vec2: Ch1Vector) -> Ch1Vector | None:
        return Ch1Vector(Name=f"{self.Name} - {vec2.Name}",Ax=self.Ax * vec2.Ax, Ay=self.Ay * vec2.Ay).auto_fill() if self.Ax is not None and self.Ay is not None else None
    
    def __sub__(self, vec2: Ch1Vector) -> Ch1Vector | None:
        return Ch1Vector(Name=f"{self.Name} - {vec2.Name}",Ax=self.Ax / vec2.Ax, Ay=self.Ay / vec2.Ay).auto_fill() if self.Ax is not None and self.Ay is not None else None


class Ch2Kinematics:
    Distance: float
    Speed: float
    Displacement: float
    Time: float
    Velocity: float
    Y_axis: str
    Acceleration: float
    XDelta: float
    SolveFor: str

    def __init__(self, SolveFor:str=None,X:float=None, XDelta:float=None, Distance:float=None,Acceleration:float=None,Vi:float=0,Xi:float=0,Speed:float=None,Displacement:float=None,Time:float=None,VFinal:float=None,Y_axis:str='x') -> None:
        self.Displacement = Displacement
        self.Distance = Distance
        self.Speed = Speed
        self.Time = Time
        self.VFinal = VFinal
        self.Y_axis = Y_axis.lower()
        self.Xi = Xi
        self.Vi = Vi
        self.X = X
        self.Acceleration = Acceleration
        self.XDelta = XDelta
        self.SolveFor = SolveFor

    def set_attribute(self, attribute_name, value):
        self.attributes[attribute_name] = value

    def get_attribute(self, attribute_name):
        return self.attributes.get(attribute_name)

    def calculate_speed(self) -> Ch2Kinematics:
        self.Speed = self.Distance / self.Time
        return self

    def calculate_vel(self) -> Ch2Kinematics:
        self.Velocity = self.Displacement / self.Time
        return self

    def get_average_speed_at_time(self,x1,y1,x2,y2) -> float:
        """
        Returns average speed at certain time
        Params:
            x1: float | int
            x2: float | int
            y1: float | int
            y2: float | int
        """
        return (x2-x1) / (y2-y1)
    

    def solve_for(self) -> float | int:
        if self.SolveFor is None:
            return None
        if self.SolveFor == 'xdelta':
            pass


    def first_equation(self) -> float | int:
        """
        Requires Xi, Vi, VFinal, Time
        """

        print("Using Equation #1")
        return self.Xi + (.5*(self.Vi + self.VFinal)) * self.Time



    def second_equation(self) -> float | int:
        """
        Requires Vi, Acceleration, Time
        """
        print("Using Equation #2")
        return self.Vi + (self.Acceleration * self.Time)



    def third_equation(self) -> float | int:
        """
        Requires Xi, Vi, Time, Acceleration
        """
        print("Using Equation #3")
        return self.Xi + self.Vi * self.Time + (.5 * self.Acceleration) * self.Time**2



    def fourth_equation(self) -> float | int:
        """
        Requires XDelta, Acceleration
        """
        print("Using Equation #4")
        return math.sqrt((2*self.XDelta)/self.Acceleration)



    def solve(self) -> float | int:
        """
        Uses provided information to solve problem
        """
        if self.Xi is not None and self.Vi is not None and self.VFinal is not None and self.Time is not None:
            return self.first_equation()
        
        if self.Vi is not None and self.Acceleration is not None and self.Time is not None and self.Xi is None:
            return self.second_equation()
        
        if self.Acceleration is not None and self.Xi is not None and self.Vi is not None and self.Time is not None:
            return self.third_equation()
        
        if self.Time is None and self.XDelta is not None and self.Acceleration is not None:
            return self.fourth_equation()
        
        else:
            print("Insufficient amount of information")
            return None

class Ch3Kinematics2d():
    Vx: float
    Vix: float
    Vy: float
    Viy: float
    Time: float
    Ax: float
    Ay: float
    XDelta: float
    YDelta: float
    def __init__(self, Vx: float=None, Vix: float=None, Vy:float=None, Viy: float=None, Time:float=None, Ax: float=None, Ay:float=None,XDelta:float=None, YDelta:float=None) -> None:
        self.Vx = Vx
        self.Vy = Vy
        self.Vix = Vix
        self.Viy = Viy
        self.Time = Time
        self.Ax = Ax
        self.Ay = Ay
        self.XDelta = XDelta
        self.YDelta = YDelta
        
    def solve(self, axis: str='x'):
        if axis.lower() == 'x':
            ch2 = Ch2Kinematics(VFinal=self.Vx, Vi=self.Vix, Time=self.Time, Acceleration=self.Ax, XDelta=self.XDelta)
            ch2.solve()
        elif axis.lower() == 'y':
            ch2 = Ch2Kinematics(VFinal=self.Vy, Vi=self.Viy, Time=self.Time, Acceleration=self.Ay, XDelta=self.YDelta)
            ch2.solve()
        

# Params you can pass in: 
# Displacement 
# Distance 
# Speed 
# Time 
# VFinal 
# Y_axis
# Xi 
# Vi
# X
# Acceleration 
# XDelta

# Xi=3,Vi=5,VFinal=4,Time=5                 1st equation
# Vi=0,Time=3,Acceleration=-9.792           2nd equation
# Xi=3,Vi=0,Time=0,Acceleration=9.792       3rd equation
# Acceleration=-9.8,XDelta=-8.75            4th equation

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def convert(var, t):
    try:
        return t(var)
    except:
        return None
def wait_for_keypress(p="Press enter to continue... "):
    # awesome
    input(p)
    
def has_math(s:str):
    if '+' in s:
        return True, '+'
    if '-' in s:
        return True, '-'
    if '**' in s:
        return True, '**'
    if '*' in s:
        return True, '*'
    if '/' in s:
        return True, '/'
    return False, -1
        
import os
import time
variables = {}
vectors = {}
names = ["Displacement", "Distance", "Speed", "Time", "VFinal", "Y_axis", "Xi", "Vi", "X", "Acceleration", "XDelta"]
ch2 = Ch2Kinematics()
while True:
    try:
        cls()
        x = input("(type help for more commands)\nChapters\n[1] Vectors\n[2] 1D Kinematics\n[3] 2D Kinematics\n> ")
        if x == '1':
            cls()
            op = input("[1] Make new vector\n[2] Perform math on 2 vectors\n[3] Print vectors to screen\n> ")
            if '1' in op:
                cls()
                print("If you don't have a value for a variable, just hit enter\nIt will autofill for you once it is made!\n---------------")
                name = convert(input("Vector Name: "),str)
                vectors[name] = Ch1Vector(Name=name)
                vectors[name].Angle = convert(input("Angle: "),float)
                vectors[name].Mag = convert(input("Magnitude: "),float)
                vectors[name].Ax = convert(input("Ax: "),float)
                vectors[name].Ay = convert(input("Ay: "),float)
                vectors[name].Axis = convert(input("Axis: "),str)
                vectors[name].Quadrant = convert(input("Quadrant: "),int)
                vectors[name].auto_fill()
                cls()
                print(vectors[name])
                print("Vector made!")
                wait_for_keypress()
            if '2' in op:
                cls()
                sign = ''
                new_name = input("Name for vector after operation\n> ")
                operation = input("Example: A+B shows Vector A + Vector B\nExample: A*B shows Vector A * Vector B, etc.\nEnter operation\n> ").replace(" ",'')
                if '+' in operation:
                    new = operation.split('+')
                    sign = '+'
                if '-' in operation:
                    new = operation.split('-')
                    sign = '-'
                if '*' in operation:
                    new = operation.split('*')
                    sign = '*'
                if '/' in operation:
                    new = operation.split('/')
                    sign = '/'
                new_str = ''
                c = 0
                for i in new:
                    new_str = new_str + f"vectors['{i}']"
                    if c == 0:
                        new_str += sign
                        c+=1
                vectors[new_name] = eval(new_str)
                vectors[new_name].Name = new_name
                variables[new_name] = vectors[new_name]
                print(vectors[new_name])
                wait_for_keypress()
            if '3' in op:
                cls()
                for i in vectors.keys():
                    print(vectors[i])
                wait_for_keypress()
            
        elif x == '2':
            cls()
            print("If you don't have a value for a variable, just hit enter\n\
    It will auto solve for you, doesn't work if you don't meet all required variables\n---------------")
            ch2.Acceleration = convert(input("Acceleration: "),float)
            ch2.Xi = convert(input("Xi: "),float)
            ch2.Vi = convert(input("Vi: "),float)
            ch2.VFinal = convert(input("VFinal: "),float)
            ch2.Time = convert(input("Time: "),float)
            ch2.Speed = convert(input("Speed: "),float)
            ch2.XDelta = convert(input("XDelta: "),float)
            cls()
            print(ch2.solve())
            wait_for_keypress()
            
        elif x.startswith("var("):
            cls()
            var_name = x.split("var(")[1].split(')')[0]
            var_type = x.split("=")[1].split('<')[1].split('>')[0]
            var_val = x.split(var_type + ">")[1]
            try:
                variables[var_name] = eval(var_type+f"({var_val})")
            except:
                variables[var_name] = eval(var_type+f"('{var_val}')")
            print(f"{var_name}={variables[var_name]}")
            wait_for_keypress()
            
        elif x.startswith("delvar("):
            cls()
            var_name = x.split("var(")[1].split(')')[0]
            if var_name in variables.keys():
                variables.pop(var_name)
                print(f"{var_name} was deleted")
            else:
                print(f"{var_name} does not exist")
            
        elif x.lower() == 'vars':
            cls()
            for i in variables.keys():
                print(f"{i}={variables[i]}")
            wait_for_keypress()
            
        elif x.lower() == 'help':
            cls()
            print("new variable: \n   var(variable name)=<type>val\n   Exmaple: var(a)=<int>32\n   Created a variable named a, which is an integer thats value is 32\n")
            print("vars - prints current variabls to screen\n")
            wait_for_keypress()
        else:
            # really interesting way to do math without doing complex stuff, not for vectors although technically does count and can put in type
            hm = has_math(x)
            if hm[0] is True:
                if ',' in x:
                    var_name = x.split(",")[1]
                    x = x.replace(" ","")
                    variables[var_name] = (eval(str(variables[x.split(hm[1])[0]]) + hm[1] + str(variables[x.split(hm[1])[1].split(',')[0]])))
                    print(f"{var_name}={variables[var_name]}")
                    wait_for_keypress()
                else:
                    x = x.replace(" ","")
                    if x.split(hm[1])[0] in variables.keys():
                        variables[var_name] = (eval(str(variables[x.split(hm[1])[0]]) + hm[1] + str(variables[x.split(hm[1])[1].split(',')[0]])))
                        print(f"{variables[var_name]}")
                    else:
                        print(eval(x))
                    wait_for_keypress()
            else:
                if x in variables.keys():
                    print(f"{x}={variables[x]}")
                    wait_for_keypress()
    except Exception as e:
        print(e)
        wait_for_keypress()
        continue
