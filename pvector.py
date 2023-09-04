from __future__ import annotations
import math

class Vector:
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

    def __add__(self, vec2: Vector) -> Vector | None:
        return Vector(Name=f"{self.Name} + {vec2.Name}",Ax=self.Ax + vec2.Ax, Ay=self.Ay + vec2.Ay).auto_fill() if self.Ax is not None and self.Ay is not None else None
    
    def __sub__(self, vec2: Vector) -> Vector | None:
        return Vector(Name=f"{self.Name} - {vec2.Name}",Ax=self.Ax - vec2.Ax, Ay=self.Ay - vec2.Ay).auto_fill() if self.Ax is not None and self.Ay is not None else None
    
    def __mul__(self, vec2: Vector) -> Vector | None:
        return Vector(Name=f"{self.Name} - {vec2.Name}",Ax=self.Ax * vec2.Ax, Ay=self.Ay * vec2.Ay).auto_fill() if self.Ax is not None and self.Ay is not None else None
    
    def __sub__(self, vec2: Vector) -> Vector | None:
        return Vector(Name=f"{self.Name} - {vec2.Name}",Ax=self.Ax / vec2.Ax, Ay=self.Ay / vec2.Ay).auto_fill() if self.Ax is not None and self.Ay is not None else None