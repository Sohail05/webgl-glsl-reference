import os


commands = {}
list = open( "list.txt" , "r") 
commands = list.read().split("\n")
list.close()
print commands


sections = open("sections.html", "w")

html = ""
summary = ""
for command in commands:

	
	html+="""<section id="""+command+""">
              <h2>"""+command+"""</h2>
              <h2>Summary</h2>
              <p>"""+summary+"""</p>
              <h2>Syntax</h2>
              <p>float x(float)</p>
              <p>vec2 x(vec2)</p>
              <p>vec3 x(vec3)</p>
              <p>vec4 x(vec4)</p>
              <h2>Example</h2>
              <pre><code></code></pre>
              <h2>See Also</h2>
              <p></p>
              <h2>Links</h2>
              <p></p>
          </section>"""

sections.write(html)
sections.close()