import xmltodict
import json as JSON
import os

# This script converts a list of IFC XML files to a single json file with only the desired properties.

#creates blueprint for IFC objects (from XML files)
class IfcFile:
    def __init__(self, ifcClassNames , psetName, propName):
        # properties from xml file
        self.ifcClassNames = ifcClassNames
        self.psetName = psetName
        self.propName = propName

    # Writes objects to json format
    # A IFC file can contain multiple class names, we treat them equally, so for each class name
    # a json object is returned with the same child properties.
    def toJson(self):
        jsonObjects = []
        for classname in self.ifcClassNames:
            jsonObjects.append({classname: [{"name": self.psetName, "properties": self.propName}]})
        return jsonObjects

    # Creates object from json
    # Wanted properties are selected from the json object.
    @classmethod
    def initializeFromJson(cls, jsonObject):
        classNames = jsonObject["PropertySetDef"]["ApplicableClasses"]["ClassName"]
        pSetNames = jsonObject["PropertySetDef"]["Name"]
        properties = jsonObject["PropertySetDef"]["PropertyDefs"]["PropertyDef"]

        # json properties are a dict, when only a single "PropertyDef" exists, then it is read as dict,
        # but when multiple exist then it is read as a list of dicts. We always want to work with the same
        # type. So if only 1 property exists (= dict) then we put that single one in a list.
        if isinstance(properties, dict):
            properties = [properties]

        # Removes "ValueDef" and "Definition" from json objects of property, such that when we
        # set the json object of the property in our class, it no longer contains these values.

        # enumurate makes from all elements in an object a set of 2 elements [9,8,7] --> ([0,9], [1,8], [2,7]), underscore deletes the last item from every object
        # TODO: Definition and ValueDef are not always removed, see IFCSHAREDBLDGELEMENTS/IfcBeam
        for p in properties:
            # pop normally extracts and removed the value from the dict, if it doesn't exist an error
            # occurs. By adding None that is used as a default if it does not exist, so no error.
            p.pop("ValueDef", None)
        for p in properties:
            p.pop("Definition", None)

        # Same as for properties, classNames are strings, but when multiple exist then it is read
        # as a list of strings. So handle a single classname (= string) as a list of strings.
        if isinstance(classNames, list):
            # classNames = [ className1, className2, className3 ]
            return cls(classNames, pSetNames, properties)
        else:
            #  classNames = "123"
            ifcname = classNames
            return cls([ifcname], pSetNames, properties)


# Parses the xml file to a json object
def parser(filepath):
    with open(filepath, 'r') as file:
        # file to dictionary
        dict = xmltodict.parse(file.read())

        # dictionary to json
        jsonString = JSON.dumps(dict)
        jsonObject = JSON.loads(jsonString)
        return jsonObject


# This must be equal to the folder which contains the ifc xml files.
ifcVersion = "IFC2x3"
inputDirectory = f"../Source/{ifcVersion}/psd"

# ifcFiles : List<IfcFile>
ifcFiles = []
# For every file in directory retrieve the path and parse this file from xml to json. We pass the json
# to the class initializer such that is is converted to a Python object.
for filename in os.listdir(inputDirectory):
    print(filename)
    # Absolute path to xml file
    filepath = os.path.join(inputDirectory, filename)
    # Xml to Json
    json = parser(filepath)
    # json to Python object
    ifcFile = IfcFile.initializeFromJson(json)

    # Add each python object to the list
    ifcFiles.append(ifcFile)


# Convert the ifcFiles (List<IfcFile>) back to json objects.
# Since one ifc file can contain multiple class names, a list of json objects is returned for each
# ifc file. We want to output a single json list, so we have to merge the results of each file.
jsonObjects = []
for ifcFile in ifcFiles:
    fileJsonObjects = ifcFile.toJson()
    for fileJsonObject in fileJsonObjects:
        jsonObjects.append(fileJsonObject)

jsonString = JSON.dumps(jsonObjects)

# Writes json to file
outputDirectory = f"../Source/{ifcVersion}"
with open(f"{outputDirectory}/json_data{ifcVersion}.json", 'w+') as outfile:
    outfile.write(jsonString)










