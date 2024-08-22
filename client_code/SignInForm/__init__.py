#Created by Hugo Giles
#Date modified 22/08/24
#The sign_in_button_click function defines the 'username' and 'password' variabels as what was enterd into the text boxes.
#It then checks to see if the username and password are equal to 'admin' and 'password' if this is true then it it open the 'main form'

from ._anvil_designer import SignInFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class SignInForm(SignInFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def sign_in_button_click(self, **event_args):
        # Define username and password as what the user enters
        username = self.text_box_username.text
        password = self.text_box_password.text

        # Checks if the entered username & password are equal to the correct ones
        if username == 'admin' and password == 'password':
            open_form('Mainscreen')
        else:
            alert("Invalid username or password")


    
