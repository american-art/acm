import xml.etree.ElementTree as ET

fpath = "AAC_AmonCarter_ObjectData_Updated_URIs.xml"
tree = ET.parse(fpath)
root = tree.getroot()

count = 1
fno = 0
fo = open("acm-objects/acm-objects1.xml","w")
fo.write("<table>\n")

for child in root.getchildren():
	ET.ElementTree.write(ET.ElementTree(child), fo)
	count += 1

	if count == 1000:
		count = 1
		fno += 1
		fo.write("</table>\n")
		fo.close()
		fo = open("acm-objects/acm-objects"+str(fno)+".xml","w")
		fo.write("<table>")

fo.write("</table>")
fo.close()