# Author: Jerrad Flores
# coin_info.py

import data_retrieval

# It should be a safe assumption that when a CoinInfo class object is created, all of the data should instantly be available to view.

# When the price wants to be displayed, we have the ability to do so (with self.retrieve_price)

# Any additional critical information can be retrieved by calling self.retrieve_important_information.


class CoinInfo:
  def __init__(self, name):
    self.name = name
    self.price = 0
    self.data = data_retrieval.retrieve_data(name)


  def retrieve_price(self):
    price = data_retrieval.retrieve_price(self.name)
    return price

  
  def retrieve_important_information(self):
    data_retrieval.retrieve_additional_information(self.name)