from __future__ import annotations
import math

class Ch1Vector:
    Mag: float = None
    Angle: float = None
    Ax: float = None
    Ay: float = None
    Quadrant: int = None
    Axis: str = None
    Name: str = None

    def __init__(self,Name: str, Mag:float=None,Angle: float = None,Ax: float = None,Ay: float = None,Quadrant: int = None,Axis: str = 'x') -> None:
        self.Mag = Mag 
        self.Angle = Angle 
        self.Ax = Ax 
        self.Ay = Ay 
        self.Quadrant = Quadrant 
        self.Axis = Axis 
        self.Name = Name

    def auto_fill(self):
        if self.Ax is None or self.Ay is None:
            self.calculate_ax_ay()
        
        if self.Ax is not None and self.Ay is not None:
            self.calculate_ang_mag()  

        if self.Quadrant is None:
            self.calculate_quad()

        return self

    def calculate_ax_ay(self):
        if self.Mag is not None and self.Angle is not None and self.Quadrant is not None and self.Axis is not None:
            Ax = math.cos(math.radians(self.Angle)) * self.Mag
            Ay = math.sin(math.radians(self.Angle)) * self.Mag
            if self.Quadrant == 1:
                self.Ax = Ax if self.Axis == 'x' else Ay
                self.Ay = Ay if self.Axis == 'x' else Ax
            if self.Quadrant == 2:
                self.Ax = -Ax if self.Axis == 'x' else Ay
                self.Ay = Ay if self.Axis == 'x' else -Ax
            if self.Quadrant == 3:
                self.Ax = -Ax if self.Axis == 'x' else -Ay
                self.Ay = -Ay if self.Axis == 'x' else -Ax
            if self.Quadrant == 4:
                self.Ax = Ax if self.Axis == 'x' else -Ay
                self.Ay = -Ay if self.Axis == 'x' else Ax

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

    def __init__(self, X:float=None, XDelta:float=None, Distance:float=None,Acceleration:float=None,Vi:float=0,Xi:float=0,Speed:float=None,Displacement:float=None,Time:float=None,VFinal:float=None,Y_axis:str='x') -> None:
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
        if self.Time is None and self.XDelta is not None and self.Acceleration is not None:
            return self.fourth_equation()
        
        elif self.Xi is None and self.Vi is not None and self.VFinal is not None and self.Time is not None:
            return self.first_equation()
        
        elif self.X is None and self.Acceleration is not None and self.Xi is not None and self.Vi is not None and self.Time is not None:
            return self.third_equation()
        
        elif self.Vi is not None and self.Acceleration is not None and self.Time is not None:
            return self.second_equation()
        else:
            print("Insufficient amount of information")
            return None



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
print(Ch2Kinematics(Time=1.21,Acceleration=-9.792).solve()) # Uses equation 3 
