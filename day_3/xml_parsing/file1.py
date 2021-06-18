import xml.etree.ElementTree as et

f = et.parse("source.xml")

root = f.getroot()
# print("Root tag is %s"%(root.tag))
# print("Root attribute is {}".format(root.attrib))

# print(root[1].tag)
# print(root[1].attrib)

print(root[2][0].tag)
print(root[2][0].text)