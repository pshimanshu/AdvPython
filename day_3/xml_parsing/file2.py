from xml.dom.minidom import parse

f = parse("source.xml")

# access the root tag
collection = f.documentElement
element = collection.getElementsByTagName("element")

for i in element:
    mname = i.getElementsByTagName("mname")[0]
    print(mname.childNodes[0].data)
    mtype = i.getElementsByTagName("mtype")[0]
    print(mtype.childNodes[0].data)
    duration = i.getElementsByTagName("duration")[0]
    print(duration.childNodes[0].data)
    print("-"*45)