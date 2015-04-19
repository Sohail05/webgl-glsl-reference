import os

if not os.path.exists("website/index_ori.html"):
	print "website/index_ori.html doesnt not exist"

	index_source=""	
file = open("website/glsl_ori.html", "r")
index_source = file.read()
file.close()

file = open("sections.html", "r")
sections_source = file.read()
file.close()

index_source = index_source.replace( "{$commad_list_info}" , sections_source )

file = open("website/glsl.html", "w")
file.write(index_source)
file.close()
