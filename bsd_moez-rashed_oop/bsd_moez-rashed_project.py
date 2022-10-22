from abc import ABC,abstractmethod
from tkinter import E
import turtle as t
import numpy as np
import math 
from math import *
from time import sleep as s
class Polygon(ABC):
    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class EqTriangle(Polygon):
    def __init__(self,side):
        self.__side=side
    def draw(self):
        t.forward(self.__side*50)
        t.left(120)
        t.forward(self.__side*50)
        t.left(120)
        t.forward(self.__side*50)
        s(15)
    def area(self):
        return(((self.__side)/2*math.tan(np.radians(180/3)))*self.perimeter())/2
    def perimeter(self):
        return(self.__base*3)
class IsoTriangle(Polygon):
    def __init__(self,base,height):
        self.__base=base
        self.__height=height   
    def draw(self):
        self.__hypot=(math.sqrt(pow((1/2)*self.__base,2)+pow(self.__height,2))) 
        self.__bottomangle = degrees(math.atan(( (self.__height) / ((self.__base)*1/2) )))
        self.__topangle = 180 - (self.__bottomangle*2)
        t.forward(self.__base * 30)
        t.left(180-self.__bottomangle)
        t.forward(self.__hypot * 30)
        t.left(180-self.__topangle)
        t.forward(self.__hypot * 30)
        t.left(180-self.__bottomangle)  

        print(self.__height)
        
        print(self.__base)
        print(self.__topangle)
        print(self.__bottomangle)

        s(15)             
    def area(self):
        return(((1/2)*self.__base*self.__height))
    def perimeter(self):
        return(self.__base+2*(math.sqrt(pow((1/2)*self.__base,2)+pow(self.__height,2))))        
class Quadriletral(Polygon):
    def __init__(self,side):
        self.__side=side
    def draw(self):
        t.forward(self.__side*50)
        t.left(90)
        t.forward(self.__side*50)
        t.left(90)
        t.forward(self.__side*50)
        t.left(90)
        t.forward(self.__side*50)
        s(15)
    def area(self):
        return(((self.__side)/2*math.tan(np.radians(180/4)))*self.perimeter())/2
    def perimeter(self):
        return(self.__base*4)
class Pentagon(Polygon):
    def __init__(self,side):
        self.__side=side
    def draw(self):
        t.forward(self.__side*50)
        t.left(360/5)
        t.forward(self.__side*50)
        t.left(360/5)
        t.forward(self.__side*50)
        t.left(360/5)
        t.forward(self.__side*50)
        t.left(360/5)
        t.forward(self.__side*50)
        s(15)
    def area(self):
        return(((self.__side)/2*math.tan(np.radians(180/5)))*self.perimeter())/2
    def perimeter(self):
        return(self.__base*5)
class Hexagon(Polygon):
    def __init__(self,side):
        self.__side=side
    def draw(self):
        t.forward(self.__side*30)
        t.left(360/6)
        t.forward(self.__side*30)
        t.left(360/6)
        t.forward(self.__side*30)
        t.left(360/6)
        t.forward(self.__side*30)
        t.left(360/6)
        t.forward(self.__side*30)
        t.left(360/6)
        t.forward(self.__side*30)
        s(15)
    def area(self):
        return(((self.__side)/2*math.tan(np.radians(180/6)))*self.perimeter())/2
    def perimeter(self):
        return(self.__base*6)
class Octagon(Polygon):
    def __init__(self,side):
        self.__side=side
    def draw(self):
        t.forward(self.__side*20)
        t.left(360/8)
        t.forward(self.__side*20)
        t.left(360/8)
        t.forward(self.__side*20)
        t.left(360/8)
        t.forward(self.__side*20)
        t.left(360/8)
        t.forward(self.__side*20)
        t.left(360/8)
        t.forward(self.__side*20)
        t.left(360/8)
        t.forward(self.__side*20)
        t.left(360/8)
        t.forward(self.__side*20)
        s(15)
    def area(self):
        return(((self.__side)/2*math.tan(np.radians(180/8)))*self.perimeter())/2
    def perimeter(self):
        return(self.__base*8)
tt = IsoTriangle(5,10)
tt.draw()