import xml.etree.ElementTree as ET
import os

directory = 'Tensorflow/workspace/images/trainset'

for file in os.listdir(directory):
    if file.endswith('.xml'):
        filename = os.path.join(directory, file)
        print('found:       ' + file)

        xmlTree = ET.parse(filename)
        rootElement = xmlTree.getroot()

        if not rootElement.findall('path'):
            PathElement = ET.Element("path")
            PathElement.text = filename
            rootElement.insert(2,PathElement)
            print('added path: ' + filename)

        if not rootElement.find('source'):
            SourceElement = ET.Element("source")
            DatabaseElement = ET.Element("database")
            DatabaseElement.text = 'Unknown'
            SourceElement.append(DatabaseElement)
            rootElement.insert(3,SourceElement)
            print('added source: database: unknown')

        for element in rootElement.findall("object"):
            if element.find('name').text == 'RipeTomato' or element.find('name').text == 'UnripeTomato':
                element.find("name").text = 'Tomato'
            elif element.find('name').text == 'tomato':
                element.find("name").text = 'Tomato'
            elif element.find('name').text == 'Tomato':
                i = 0
            else:
                print('Found unexpected element: ' + element.find('name').text)

            for child in element:
                if child.tag  == "occluded":
                    element.remove(child)
                    print('removed occluded')
            
        xmlTree.write(filename)
        print('refactored:  ' + file)