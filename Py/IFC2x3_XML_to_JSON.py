import xmltodict
import json


def Parser():
    with open('../Source/IFC2x3/psd/Pset_ActionRequest.xml', 'r') as myfile:
        obj = xmltodict.parse(myfile.read())
    print(json.dumps(obj))
    return obj


def Json(obj):
    classname = obj["PropertySetDef"]["ApplicableClasses"]["ClassName"][0]

    for url in obj["PropertySetDef"]["ApplicableClasses"]["urls"]:
        if url["key"] == "MOBILE":



# Pset = {
#     classname: [
#         {
#             "name": name
#             "Properties": [
#                 {
#                     "name": name,
#                     "type": "",
#                 }
#             ]
#         }
#     ]
# }



