import os
import xml.etree.ElementTree as ET
import collections

command_list = []
commad_info = {}

def get_command_list( path_file ):

    file = open( path_file, "r")
    commands = []
    commands = file.read().split("\n")
    file.close()
    return commands

def get_file( path_file ):
    xtree = ET.parse(path_file)
    root = xtree.getroot()
    commad_info[root.attrib["id"]] ={}

    #summary
    str = ""
    str =  root[1][1].text
    str = str.replace( u'\u2014', "")
    commad_info[root.attrib["id"]]["summary"] = str[len(root.attrib["id"])+2:]

    #Get function prototype
    findall = xtree.findall('.//div[@class="funcsynopsis"]')
    count = len(findall)
    functionProto = []
    if count > 1:
        functionProto.append(findall[0])
        functionProto.append(findall[1])
    else:
        functionProto.append(findall[0])

    commad_info[root.attrib["id"]]["proto"] =[]
    for function in functionProto:
        #return value
        returntype = function.find('.//code[@class="funcdef"]')

        if returntype.text == "genIType ":
            continue

        params = function.findall('.//var[@class="pdparam"]/../.')
        paramstr = ""
        for i,param in enumerate(params):
            paramstr += param.text.replace(" ","")
            if i >= 0 and i != len(params)-1 and 1 != len(params) :
                paramstr+=", "

        print(paramstr)
        paramstr = paramstr.replace("vec, vec, bvec, bvec, ivec, ivec, uvec, uvec","vec, vec" )
        paramstr = paramstr.replace("vec, vec, ivec, ivec, uvec, uvec","vec, vec" )
        paramstr = paramstr.replace("vec, vec, ivec, ivec, bvec, bvec, uvec, uvec","vec, vec" )
        commad_info[root.attrib["id"]]["proto"].append(returntype.text +  root.attrib["id"] +"(" + paramstr +")")

    #seealso
    commad_info[root.attrib["id"]]["seealso"] = []
    seealso = xtree.find('.//div[@id="seealso"]')
    for child in seealso[1]:
        print (child.attrib["href"])
        commad_info[root.attrib["id"]]["seealso"].append(child.attrib["href"])

command_list = get_command_list("data/list.txt")
#print command_list

for command in command_list:
    pathfile = "el3"+"\\"+command+".xhtml"
    if(os.path.isfile(pathfile)):
        get_file(pathfile)
    else:
        print (pathfile +" not found")

sorted_commad_info = collections.OrderedDict(sorted(commad_info.items()))
sections = open("sections.html", "w")

html = ""
for command in sorted(commad_info.items()):

    html+="<section id="+str(command[0])+">\n"
    html+="<h2>"+str(command[0])+"</h2>\n"
    html+="<h2>Summary</h2>\n"
    html+="<p>"+command[1]["summary"]+"</p>\n"
    html+='<h2>Syntax</h2>\n<pre class="language-c">'

    for i in command[1]["proto"]:
        html+="""<code>"""+i+"""</code>"""

    example_file = open("examples/"+str(command[0])+".txt", "r")
    example = "";
    example = example_file.read();
    example_file.close()


    html+='</pre><h2>Example</h2><pre class="language-c">'
    for text in example.split("\n"):

        html+="<code>"+text+"</code>\n"

    html+='</pre><h2>See Also</h2>\n<p>'
    for i in command[1]["seealso"]:
        html+= "<a href=#"+i+">"+i+"</a>\n"

    html+="</p>"
    html+="""<h2>Links</h2>
             <a></a>\n
         </section>"""

sections.write(html)
sections.close()
