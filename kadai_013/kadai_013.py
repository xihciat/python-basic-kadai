# -*- coding: utf-8 -*-
"""kadai_013.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k6T67Ds9HA2gD_tEAxnifzQwYuLTvrXS
"""

def calculate_total_price(price, tax_rate):
  total = price + price * tax_rate/100
  print(f"合計金額は{total}円です。")

calculate_total_price (3000, 10)