# import html5lib as h
# from lxml import etree

# with open("./Python/Doxgen_parsingTask/html/_file_8c.html" , "rb") as file:
#     Doxygen_content = h.parse(file)
#     walker = h.getTreeWalker("etree")
#     stream = walker(Doxygen_content)
#     s = h.serializer.HTMLSerializer()
#     output = " ".join(s.serialize(stream))
#     print(output)
#     # root = etree.fromstring(output)
#     # print(root)

from bs4 import BeautifulSoup as Bsoup

with open("./Python/Doxgen_parsingTask/html/_file_8c.html" , 'r') as file :
    Content = file.read()
    soup = Bsoup(Content , "lxml")
    ModuleName = soup.find("head").find("title").text
    print(ModuleName)