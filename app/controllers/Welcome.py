from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

   
    def index(self):
        names = self.models['WelcomeModel'].show_all_names()
        print names
        return self.load_view('index.html', names=names)