# Created by Hugo Giles
# Date modified 22/08/24
# This code defines a template for displaying individual furniture items.
# The button_add_to_cart_click function allows the user to add the item to the shopping cart by retrieving the specified quantity,
# creating an item dictionary, adding it to the cart in the main form, and notifying the user that the item has been added.

from ._anvil_designer import FurnitureItemTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class FurnitureItemTemplate(FurnitureItemTemplateTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        # Assume 'self.item' contains the current item details from the Furniture table
        self.label_furniture_name.text = self.item['Name']
        self.label_category.text = self.item['Category']
        self.label_price.text = f"${self.item['Price']}"
        self.image_furniture.source = self.item['Image']
        self.label_instock.text = f"In Stock: {self.item['Stock']}"
      
    def button_add_to_cart_click(self, **event_args):
        # Get the quantity from the quantity TextBox
        quantity = int(self.text_box_quantity.text)

        # Create a dictionary for the item
        item_to_add = {
            'item_id': self.item['id'],  # Use the unique ID from the data table
            'name': self.item['Name'],
            'quantity': quantity,
            'price': self.item['Price']
        }

        # Add the item to the cart in MainForm
        get_open_form().add_to_cart(item_to_add)
        
        # Notify the user
        alert(f"Added {quantity} of {self.item['Name']} to the cart.")




  
  