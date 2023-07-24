from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import AsyncImage
from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from ruffier import test

age = 7
name = ""
p1, p2, p3 = 0, 0, 0


class CustomButton(ButtonBehavior, AsyncImage):
    pass


class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.background_color = (0, 1, 0, 1) 


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        lbl1 = Label(text="Enter a name:", halign="right")
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text="Enter age:", halign="right")
        self.in_age = TextInput(text="7", multiline=False)
        self.btn = CustomButton(source='button_background.png', size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.bind(on_press=self.next)
        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)


        bg_image = AsyncImage(source='titun.gif')
        outer.add_widget(bg_image)

        self.add_widget(outer)

    def next(self, *args):
        global name
        name = self.in_name.text
        self.manager.current = "pulse1"


class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_test1)

        line = BoxLayout(size_hint=(0.8, None), height="30sp")
        lbl_result = Label(text="Enter the result:", halign="right")
        self.in_result = TextInput(text="0", multiline=False)

        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        self.btn = CustomButton(source='button_background.png', size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.bind(on_press=self.next)
        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)


        bg_image = AsyncImage(source='background2.gif')
        outer.add_widget(bg_image)

        self.add_widget(outer)

    def next(self, *args):
        global p1
        p1 = int(self.in_result.text)
        self.manager.current = "sits"


class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)
        self.btn = CustomButton(source='button_background.png', size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.bind(on_press=self.next)
        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)


        bg_image = AsyncImage(source='background3.gif')
        outer.add_widget(bg_image)

        self.add_widget(outer)

    def next(self, *args):
        self.manager.current = "pulse2"


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3)
        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        lbl_result1 = Label(text="Result:", halign="right")
        self.in_result1 = TextInput(text="0", multiline=False)
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        lbl_result2 = Label(text="Result after rest:", halign="right")
        self.in_result2 = TextInput(text="0", multiline=False)
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)
        self.btn = CustomButton(source='button_background.png', size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.bind(on_press=self.next)
        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)


        bg_image = AsyncImage(source='background4.gif')
        outer.add_widget(bg_image)

        self.add_widget(outer)

    def next(self, *args):
        global p2, p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
        self.manager.current = "result"


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.instr = Label(text="")
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self, *args):
        global name
        self.instr.text = name + "\n" + test(p1, p2, p3, age)


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr"))
        sm.add_widget(PulseScr(name="pulse1"))
        sm.add_widget(CheckSits(name="sits"))
        sm.add_widget(PulseScr2(name="pulse2"))
        sm.add_widget(Result(name="result"))
        return sm


app = HeartCheck()
app.run()
