from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        layout = Button(text='Clique-me!')
        layout.bind(on_press=self.on_button_click)
        return layout
    
    def on_button_click(self, instance):
        idade = 25

        if idade < 18:
            mensagem = 'Menor de Idade'
        elif idade >= 18 and idade < 65:
            mensagem = 'Adulto'
        else:
            mensagem =  'Idoso'

        instance.text = mensagem


if __name__ == "__main__":
    MeuApp().run()