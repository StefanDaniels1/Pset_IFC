import xmltodict
import json
import pandas as pd


def parser():
    with open('../Source/IFC2x3/psd/Pset_ActionRequest.xml', 'r') as myfile:
        obj = xmltodict.parse(myfile.read())

    return obj

def printt(obj):
    print(json.dumps(obj))

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

printt(parser())











