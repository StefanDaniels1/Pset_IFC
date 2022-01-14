import xmltodict
import json
import pandas as pd
import os
import xml.etree.ElementTree as ET


class IfcClass:
    def __init__(self, IfcName):
        self.IfcName = IfcName

    @classmethod
    def ifc_name(cls, object):
        return cls(object["PropertySetDef"]["ApplicableClasses"]["ClassName"])

def list_creator(self):
    name = classmethod(IfcClass.ifc_name)
    print(name)
    return

# list_creator()


def parser():
    with open('../Source/IFC2x3/psd/Pset_ActionRequest.xml', 'r') as myfile:
        obj = xmltodict.parse(myfile.read())
    return obj

def to_json(obj):
    jsonString = json.dumps(obj)
    jsonObject = json.loads(jsonString)
    return jsonObject


Pset_json = to_json(parser())
ifc = IfcClass.ifc_name(Pset_json)
print(ifc)





# #
# #
# def file_command(filepath):
#     f = open(filepath)
#
#
#
# a_directory = "../Source/IFC2x3/psd"
# for filename in os.listdir(a_directory):
#     with open(a_directory + "/" + filename, 'r') as filename:
#         obj = xmltodict.parse(filename.read())
#
#     file_command(filepath)
#
#



# parser()

# def pd_json(obj):
#     df = pd.read_json(obj)
#     df['PropertySetDef'].applly(pd.Series)
#     print(df)


#
# def json(obj):
#     Properties = []
#     classname = str(obj["PropertySetDef"]["ApplicableClasses"]["ClassName"])
#     Pset_name = str(obj["PropertySetDef"]["Name"])
#     for each in obj["PropertySetDef"]["PropertyDefs"]["PropertyDef"]:
#         Properties.append(str(each["Name"]))
#     # for i in obj["PropertySetDef"]["PropertyDefs"]["PropertyDef"]:
#     #     Properties.append(str(i["Name"]))
#     # dict = {classname: {'name': Pset_name, 'properties': {Properties}}
#     # json_dump = json.dump(dict)
#
#     y = {classname:{"name":[Pset_name]}, "properties":[{"name":Propertie, "type":Type}]}
#     # print(json.dump(y))

    #
    #
    #
    # {
    #     classname: [
    #         {
    #             "name": Pset_name,
    #             "properties": [
    #                 {
    #                     "name": Propertie,
    #                     "type": Type
    #                 },
    #                 {
    #                     "name": Propertie,
    #                     "type": Type
    #                 }
    #             ]
    #         }
    #     ]
    # }













