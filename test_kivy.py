from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Kivy Çalışıyor!', font_size='30sp')
        button = Button(text='Kapat', size_hint_y=None, height=50)
        button.bind(on_press=lambda x: exit())
        layout.add_widget(label)
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    TestApp().run()
