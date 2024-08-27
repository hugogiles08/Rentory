from ._anvil_designer import OrderDetailsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class OrderDetails(OrderDetailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    app_tables.customer.add_row(
            Name=self.textbox_name.text,
            Email=self.textbox_email.text,
            Phone=self.textbox_phone.text
        )

    
