# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:01:50 2025

@author: em1184
"""

from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount


        triangle = Triangle()  # create a square
        triangle.rotate(PI / 4)  # rotate a certain amount
        

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))
        self.play(Transform(circle, triangle))
        self.play(FadeOut(circle))  # fade out animation
        self.play(Transform(triangle, square))
        self.play(FadeOut(triangle))
        self.wait(1)