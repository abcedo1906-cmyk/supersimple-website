from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Display takes full width
        self.display = TextInput(font_size=80, readonly=True, halign="right", multiline=False, size_hint=(1, 0.2))
        self.add_widget(self.display)

        # Buttons grid below display
        buttons_layout = GridLayout(cols=4, spacing=5, size_hint=(1, 0.8))

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for label in buttons:
            button = Button(text=label, font_size=24)
            button.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(button)

        self.add_widget(buttons_layout)

        self.last_was_operator = False
        self.last_button = None

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == 'C':
            self.display.text = ''
        elif button_text == '=':
            try:
                result = str(eval(current))
                self.display.text = result
            except Exception:
                self.display.text = 'Errore'
        else:
            if button_text in '+-/*':
                if current == '' or self.last_was_operator:
                    return
                self.last_was_operator = True
            else:
                self.last_was_operator = False

            self.display.text += button_text

        self.last_button = button_text

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()
