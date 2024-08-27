# Created by Hugo Giles
# Date modified 22/08/24
# The sign_in_button_click function defines the 'username' and 'password' variables as what was entered into the text boxes.
# It then checks to see if the username and password are equal to 'admin' and 'password'. If this is true, it opens the 'Mainscreen' form.

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
        # Capture the text entered by the user into the 'username' and 'password' text boxes
        username = self.text_box_username.text
        password = self.text_box_password.text

        # Check if the entered username and password match the predefined values 'admin' and 'password'
        if username == 'user123' and password == 'password123':
            # If the credentials are correct, open the Mainscreen form
            open_form('Mainscreen')
        else:
            # If the credentials are incorrect, display an alert message to the user
            alert("Invalid username or password")

    

