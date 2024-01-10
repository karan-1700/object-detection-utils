from xml.dom import minidom
import os
import glob
import pandas as pd

all_classes = []
number_of_xml_files = 0

# Path to the folder that contians the XML files
# For Windows: XML_PATH = "F:\\Project Images\\drive-download\\KGC_F3_E4"
# For Linux: XML_PATH = "F:/Project Images/drive-download/KGC_F3_E4"
XML_PATH = "F:\\Project Images\\drive-download\\KGC_F3_E4"

# For Windows: for fname in glob.glob(XML_PATH + "\\*.xml"):
# For Linux: for fname in glob.glob(XML_PATH + "/*.xml"):
for fname in glob.glob(XML_PATH + "\\*.xml"):
    xmldoc = minidom.parse(fname)
    itemlist = xmldoc.getElementsByTagName('object')
    
    for item in itemlist:
        # get class label
        classid =  (item.getElementsByTagName('name')[0]).firstChild.data
        # print(classid)
        
        all_classes.append(classid)
    
    number_of_xml_files += 1
            
# print("\nall_classes = ",all_classes)

df = pd.DataFrame(all_classes, columns=["Class_Name"])

statistics_dict = df.groupby("Class_Name").Class_Name.count().to_dict()

print("\n[INFO] Total .xml files processed = ", number_of_xml_files)
print("\n[INFO] Annotation Statistics: \n")

for key, value in statistics_dict.items():
    print(key, ":", value)

total_sum = df["Class_Name"].count()
print("\n[INFO] Total objects annotated = ", total_sum)
print()
