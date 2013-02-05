import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from googlevoice import Voice
import gvoice_config


class DialPadButton(Button):
    def __init__(self, number, reminder_text, *args, **kwargs):
        kwargs['text'] = "[b]%s[/b] %s" % (number, reminder_text)
        kwargs['markup'] = True
        kwargs['font_size'] = '20sp'
        super(DialPadButton, self).__init__(*args, **kwargs)
        self.number = number

dial_pad_data = {
    '1': '    ', '2': ' abc', '3': ' def',
    '4': ' ghi', '5': ' jkl', '6': ' mno',
    '7': 'pqrs', '8': ' tuv', '9': 'wxyz',
    '*': '    ', '0': '    ', '#': '    ',
}
dial_pad_key = map(str, [1,2,3,4,5,6,7,8,9,'*',0,'#'])


class DialPad(GridLayout):
    def __init__(self, *args, **kwargs):
        kwargs['rows'] = 4
        super(DialPad, self).__init__(*args, **kwargs)
        self.buttons = {}
        for name in dial_pad_key:
            self.buttons[name] = DialPadButton(name, dial_pad_data[name])
            self.add_widget(self.buttons[name])


class PhoneNumberLabel(Label):
    def __init__(self, *args, **kwargs):
        super(PhoneNumberLabel, self).__init__(*args, **kwargs)
        self.halign = 'right'
        self.text_size = (self.width, None)

    def add_number(self, number):
        self.text = self.text + str(number)

    def clear(self):
        self.text = ''


class Dialer(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.phone_number = PhoneNumberLabel()
        self.phone_number.size_hint = (1.0, .1)
        layout.add_widget(self.phone_number)

        # actions bar
        actions = BoxLayout()
        actions.size_hint = (1.0, 0.2)
        clear_button = Button(text='Clear', font_size='20sp')
        clear_button.bind(on_press=lambda _: self.phone_number.clear())
        call_button = Button(text='[b]Call[/b]', font_size='20sp', markup=True)
        call_button.bind(on_press=lambda _: self.dial(self.phone_number.text))
        actions.add_widget(clear_button)
        actions.add_widget(call_button)
        layout.add_widget(actions)

        dial_pad = DialPad()
        dial_pad.size_hint = (1.0, 0.7)
        for number, button in dial_pad.buttons.iteritems():
            button.bind(on_press=lambda i: self.phone_number.add_number(i.number))
        layout.add_widget(dial_pad)
        return layout

    def dial(self, number):
        print "dialing number: %s" % number
        voice = Voice()
        voice = voice.login(gvoice_config.email, gvoice_config.passwd)
        voice.call(number, gvoice_config.phone_to_ring, gvoice_config.phone_to_ring_type)

if __name__ in ('__main__', '__android__'):
    Dialer().run()
