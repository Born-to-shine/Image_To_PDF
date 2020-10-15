# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:38:37 2020

@author: user
"""

import os
from PIL import Image
def image_pdf(image_path):
  file_name = str(image_path.split("\\")[-1])
  new_file = os.path.join(image_path.replace(file_name.split(".")[-1], "pdf"))
  image_file = Image.open(image_path)
  parsed = image_file.convert("RGB")
  return parsed.save(new_file)
if __name__ == "__main__":
  #Add the path of the image
  image_path = 'cup_coffee_books.jpg'
  pdf = image_pdf(image_path)
  print(image_path)
