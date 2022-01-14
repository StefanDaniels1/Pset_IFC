import xmltodict
import json
import os


#creates blueprint for objects
class IfcClass:
    def __init__(self, IfcName):
        self.IfcName = IfcName
#Writes objects to json format, here you need to create the right json tree
    def toJson(self):
        return { self.IfcName: [{ "name": self.IfcName }] }
#creates objects from json file, here all entities need to be defined to get tot the list
    @classmethod
    def initializeFromJson(cls, jsonObject):
        classnames = jsonObject["PropertySetDef"]["ApplicableClasses"]["ClassName"]

        if isinstance(classnames, list):
            return cls("Multiple_classnames!")
        else:
            return cls(classnames)

def list_creator(self):
    name = classmethod(IfcClass.ifc_name)
    print(name)
    return

# list_creator()
#parses the xml files to json
def parser(filepath):
    with open(filepath, 'r') as myfile:
        obj = xmltodict.parse(myfile.read())
    return obj
#loads the json into json objects
def to_json(obj):
    jsonString = json.dumps(obj)
    jsonObject = json.loads(jsonString)
    return jsonObject

#creates list of ifc objects
ifcversion = "IFC2x3"
directory = f"../Source/{ifcversion}/psd"
result = []
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    print(filename)
    Pset_json = to_json(parser(filepath))
    ifcObject = IfcClass.initializeFromJson(Pset_json)
    result.append(ifcObject)
    print(ifcObject)
    print(ifcObject.toJson())

#uses json class function and dumps it in correct json format
outputdirectory = f"../Source/{ifcversion}"
# result : List<IfcClass>
jsonString = json.dumps([ifcObject.toJson() for ifcObject in result])
print(jsonString)

#writes  json to file
with open(f"{outputdirectory}/json_data.json", 'w+') as outfile:
    outfile.write(jsonString)




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













