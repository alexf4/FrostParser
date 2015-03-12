__author__ = 'kharbush'

import xml.etree.ElementTree as ET

#This is the main method. It is the entry point into the python script
def main():

    tree = ET.parse('data.xml')
    root = tree.getroot()

    outputString = ""

    for child in root.iter("Placemark"):
        outputString = ""
        for child2 in child:
            if child2.tag == 'name':
                outputString += "Name: " + child2.text
            if child2.tag == 'Point':
                for point in child2:
                    outputString += ", Coordinates: " + point.text
                print outputString


if __name__ == "__main__":
    main()