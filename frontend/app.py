import dom

print("Hello from Python!")

dom.document.title = "Hello world"
div = dom.document.getElementById("pyconsole")
div.innerHTML = div.innerHTML + "\n\nHello, World!\n\n"

raise ValueError("Just testing out exceptions!")
