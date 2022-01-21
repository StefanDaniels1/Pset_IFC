import xmltodict
import json as JSON
import os
import sys
from itertools import chain
import collections
from collections import defaultdict

class IfcFile:
    def __init__(self, ifcClassNames , psetName, propName):
        # properties from xml file
        self.ifcClassNames = ifcClassNames
        self.psetName = psetName
        self.propName = propName

    @classmethod
    def initializeDict(cls, dict):
        classNames = dict["PropertySetDef"]["ApplicableClasses"]["ClassName"]
        pSetNames = dict["PropertySetDef"]["Name"]
        properties = dict['PropertySetDef']['PropertyDefs']["PropertyDef"]
        return cls(classNames, pSetNames, properties)

    def toObject(self):
        return

#import files
def parser(filepath):
    with open(filepath, 'r') as file:
        # file to dictionary
        dict = xmltodict.parse(file.read())

    return dict


ifcVersion = "IFC2x3"
inputDirectory = f"../Source/{ifcVersion}/psd"

ifcDicts = []
for filename in os.listdir(inputDirectory):
    # Absolute path to xml file
    filepath = os.path.join(inputDirectory, filename)
    # Xml to dict
    ifcDict = parser(filepath)
    ifcNestedDict = IfcFile.initializeDict(ifcDict)
    ifcDicts.append(ifcNestedDict)





