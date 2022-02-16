#!/usr/bin/env python

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Line


class MyPaintWidget(Widget):
    def on_touch_down(self,touch):
        color = (random(),1,1)
        with self.canvas:
            Color(*color,mode='hsv')
            d=(random()*30.0)
#            Ellipse(pos=(touch.x - d/2,touch.y - d/2),size=(d,d))
            touch.ud['line'] = Line(points=(touch.x,touch.y),width=d)

    def on_touch_move(self,touch):
        touch.ud['line'].points += [touch.x,touch.y]


class MyPaintApp(App):
    def build(self):
        l = BoxLayout(orientation='vertical')
        self.painter = MyPaintWidget(size_hint=(1,.9))
        clearbtn = Button(text='clear',size_hint=(1,.1))
        clearbtn.bind(on_release=self.clear_canvas)
        l.add_widget(self.painter)
        l.add_widget(clearbtn)
        return l

    def clear_canvas(self,obj):
        self.painter.canvas.clear()

if __name__ == "__main__":
    MyPaintApp().run()

