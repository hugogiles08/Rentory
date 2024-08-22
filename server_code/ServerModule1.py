import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_all_furniture():
    # return all rows from the 'Furniture' data tabel
    return app_tables.furniture.search()



