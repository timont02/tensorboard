import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button
from PIL import Image
import xml.etree.ElementTree as ET
import sys

directory = './Tensorflow/workspace/images/collected_images'
labelToRefactor: str = 'tomato'

def ofLabelToRefactor(object) -> bool:
    for element in object:
        if element.tag == 'name':
            if element.text == labelToRefactor:
                return True
    return False

def getBoundingBox(object) -> patches.Rectangle:
    for element in object:
        if element.tag == 'bndbox':
                            x = 0
                            y = 0
                            width = 0
                            height = 0

                            for coord in element:
                                if coord.tag == "xmin":
                                    xmin = int(coord.text)
                                elif coord.tag == "ymin":
                                    ymin = int(coord.text)
                                elif coord.tag == "xmax":
                                    xmax = int(coord.text)
                                elif coord.tag == "ymax":
                                    ymax = int(coord.text)
                
                            x = xmin
                            y = ymin
                            width = xmax - xmin
                            height = ymax - ymin

                            return patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')


def main() -> int:
    
    
    for file in os.listdir(directory):
        if file.endswith('.png'):
            imgFilename = directory + '/' + file
            print(imgFilename)

            xmlFilename = '.' + imgFilename.rsplit('.')[1] + '.xml'
            print(xmlFilename)

            xmlTree = ET.parse(xmlFilename)
            rootElement = xmlTree.getroot()

            print(imgFilename)
            img = Image.open(imgFilename)
            
            # Create figure and axes
            fig, ax = plt.subplots()

            # Display the image
            ax.imshow(img)

            for object in rootElement.findall("object"):
                if ofLabelToRefactor(object):

                    # Display bounding box
                    bbox = getBoundingBox(object)
                    ax.add_patch(bbox)
                    
                    plt.ion()
                    plt.draw()
                    plt.pause(0.001)

                    print('If RipeTomato,   enter [r]')
                    print('If UnripeTomato, enter [u]')
                    inputChar = input()

                    for element in object:
                        if element.tag  == "name":
                            if(inputChar == 'r'):
                                element.text = 'RipeTomato'
                            elif(inputChar == 'u'):
                                element.text = 'UnripeTomato'
                            else:
                                print('Unknwon input: {}'.format(inputChar))

                    bbox.remove()
                    xmlTree.write(xmlFilename)
            
            plt.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())