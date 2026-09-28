
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CarConverterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='ZOKII BUILDER - PS4 Car Converter', font_size=20))
        
        btn1 = Button(text='SELECT FOLDER WITH PC / DLC FILES', size_hint_y=None, height=50)
        btn2 = Button(text='PC -> PS4 • CONVERT', size_hint_y=None, height=50)
        btn3 = Button(text='BUILD RPF7 FROM OUTPUT', size_hint_y=None, height=50)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout

if __name__ == '__main__':
    CarConverterApp().run()
