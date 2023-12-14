from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.botao = Button(text='Clique-me!')
        self.botao.bind(on_press=self.mostrar_mensagem)
        layout.add_widget(self.botao)
        self.label = Label(text="Pressione o Botão")
        layout.add_widget(self.label)

        
        return layout
    
    def mostrar_mensagem(self, instance):
        self.label.text= "Você clicou no botão!"

if __name__ == "__main__":
    MeuApp().run()