from bs4 import BeautifulSoup
import json

for filename in os.listdir("../Source/IFC2x3"):
    if filename.startswith("Pset_"):
        print(filename)
    # xml_parser = BeautifulSoup(ope)

