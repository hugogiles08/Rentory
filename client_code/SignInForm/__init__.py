from ._anvil_designer import SignInFormTemplate
from anvil import *


class SignInForm(SignInFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

def sign_in_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    username = self.text_box_username.text
    password = self.text_box_password.text
    
    if username == 'admin' and password == 'password':
        open_form('Mainscreen')
    else:
        alert("Invalid username or password")

    
