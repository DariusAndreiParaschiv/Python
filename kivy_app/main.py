from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import json, glob, random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.transition.direction = 'left'
        self.ids.fail.text = ""
        self.ids.user.text = ''
        self.ids.pas.text = ''
        self.manager.current = "sign_up_screen"
    def login(self, u, p):
        self.manager.transition.direction = 'left'
        self.ids.fail.text = ""
        self.ids.user.text = ''
        self.ids.pas.text = ''
        with open(r"kivy\users.json") as file:
            users = json.load(file)
        print(users)
        print(u, p)
        if u in users and users[u]['username'] == u and users[u]['password'] == p:
            self.manager.current = "login_screen_success"
        else:
            #self.manager.current = "login_screen_fail"
            self.ids.fail.text = "Wrong username or password"

'''class LoginScreenFail(Screen):
    def loginscreen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"'''

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        print(uname, pword)
        with open(r"kivy\users.json") as file:
            users = json.load(file)
        users[uname] = {'username': uname,
                        'password': pword,
                        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open(r"kivy\users.json", 'w') as file:
                json.dump(users, file)
        self.manager.current = "sign_up_screen_success"
    def lg(self):
        self.manager.current = "login_screen"
        self.manager.transition.direction = 'right'

class SignUpScreenSuccess(Screen):
    def loginscreen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.ids.feel.text = ''
        self.ids.quote.text = ''
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'
    def enlight(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob(r"kivy\quotes\*txt")
        '''for i in available_feelings:
            if feel == Path(i).stem:
                print(i)'''
        print(available_feelings)
        available_feelings = [Path(filename).stem for filename in
                                available_feelings]
        if feel in available_feelings:
            with open(f"kivy\\quotes\\{feel}.txt", encoding='utf-8') as file:
                quotes = file.readlines()
            print(quotes)
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
