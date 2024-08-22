from ._anvil_designer import FurnitureItemTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class FurnitureItemTemplate(FurnitureItemTemplateTemplate):
  def __init__(self, **properties):
        self.init_components(**properties)
        self.label_furniture_name.text = self.item['Name']
        self.label_category.text = self.item['Category']
        self.label_quantity.text = str(self.item['Quantity'])
        self.label_price.text = f"${self.item['Price']}"
  
  