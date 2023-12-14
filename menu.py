from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        self.tarefas = []
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_tarefa = TextInput(hint_text='Digite uma tarefa')
        layout.add_widget(self.input_tarefa)

        adicionar_botao = Button(text='Adicionar Tarefa')
        adicionar_botao.bind(on_press=self.adicionar_tarefa)
        layout.add_widget(adicionar_botao)

        self.lista_layout = BoxLayout(orientation='vertical', spacing=5)
        layout.add_widget(self.lista_layout)

        
        return layout
    
    def adicionar_tarefa(self, instance):
        texto_tarefa = self.input_tarefa.text
        if texto_tarefa:
            tarefa_label = Label(text=texto_tarefa)
            self.lista_layout.add_widget(tarefa_label)
            self.tarefas.append(texto_tarefa)
            self.input_tarefa.text = ""

if __name__ == "__main__":
    MeuApp().run()