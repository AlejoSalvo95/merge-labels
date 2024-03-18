from xml.dom import minidom

def prettify_xml(xml_content):
    # Parse the XML content
    parsed_xml = minidom.parseString(xml_content)
    # Pretty print with indentation, then decode
    pretty_xml = parsed_xml.toprettyxml(indent="  ", newl="\n", encoding="utf-8").decode("utf-8")
    # Eliminate lines that contain only whitespace
    pretty_xml = '\n'.join(line for line in pretty_xml.split('\n') if line.strip())
    # Convert self-closing tags back to open and close tags for specific elements
    pretty_xml = pretty_xml.replace('/>', '></note>')
    return pretty_xml

# Your XML content
xml_content = """<?xml version='1.0' encoding='utf-8'?>
<notes version="1">
  <labels>
    <label id="0" color="40D301">Label 0</label>
    <label id="1" color="B0FFB0">Label 1</label>
    <label id="2" color="CF54CC">Label 2</label>
    <label id="3" color="5500">Label 3</label>
    <label id="4" color="FFAEFF">Label 4</label>
    <label id="5" color="80FF">Label 5</label>
    <label id="6" color="303EFF">Label 6</label>
    <label id="7" color="1985FF">Label 7</label>
  </labels>
  <note player="user1" label="1" update="1679833283"></note>
  <note player="user2" label="1" update="1679833283"></note>
</notes>"""

# Use the function to prettify the XML
pretty_xml = prettify_xml(xml_content)

# Print or write the pretty XML to a file
print(pretty_xml)
