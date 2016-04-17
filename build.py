import os
import generate

file = open("data/index_template.html", "r")
index_source = file.read()
file.close()

file = open("sections.html", "r")
sections_source = file.read()
file.close()

index_source = index_source.replace( "{$commad_list_info}" , sections_source )

file = open("index.html", "w")
file.write(index_source)
file.close()

print("index updated!")