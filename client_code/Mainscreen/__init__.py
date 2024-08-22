from ._anvil_designer import MainscreenTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
import datetime

class Mainscreen(MainscreenTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        # Initialize an empty cart list
        self.cart = []

        # Retrieve all furniture items from the Furniture table and display them in the RepeatingPanel
        furniture_items = app_tables.furniture.search()
        self.repeating_panel_furniture.items = furniture_items

    def add_to_cart(self, item_to_add):
        # Check if the item is already in the cart
        for item in self.cart:
            if item['item_id'] == item_to_add['item_id']:
                # If the item is already in the cart, just increase the quantity
                item['quantity'] += item_to_add['quantity']
                break
        else:
            # If the item is not in the cart, add it
            self.cart.append(item_to_add)
        
        # Optionally, print the cart contents for debugging
        print(self.cart)
        #when this button is clicked run the show_cart_contents fuction
    def button_view_cart_click(self, **event_args):
        self.show_cart_contents()

    def show_cart_contents(self):
        #if self.cart is empty, tell user its empty
        if not self.cart:
            alert("Your cart is empty.")
        else:
            # Create a string to display cart contents
            cart_contents = "\n".join([f"{item['quantity']} x {item['name']} @ ${item['price']} each" for item in self.cart])
            response = alert(cart_contents, title="Cart Contents", buttons=[("Edit", "edit"), ("Close", "close")])
            #if user selects edit button, run edit_cart fuction
            if response == "edit":
                self.edit_cart()

    def edit_cart(self):
        for index, item in enumerate(self.cart):
            new_quantity = int(prompt(f"Enter new quantity for {item['name']}: ", value=item['quantity']))

            if new_quantity <= 0:
                # Remove item from cart if quantity is zero or negative
                del self.cart[index]
            else:
                # Update the quantity
                item['quantity'] = new_quantity

        alert("Cart updated.")

    def button_confirm_order_click(self, **event_args):
        if not self.cart:
            alert("Your cart is empty.")
            return

        # Calculate the total price of the order
        total_price = sum(item['quantity'] * item['price'] for item in self.cart)

        # Save the order to the Orders table
        app_tables.Orders.add_row(
            items=self.cart,
            total_price=total_price,
            created_at=datetime.datetime.now(),
            status="Pending"
        )

        # Clear the cart after saving the order
        self.cart = []
        alert("Order confirmed and saved!")

  
