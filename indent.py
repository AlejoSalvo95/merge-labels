from xml.dom import minidom
import re

def prettify_xml_file(input_file_path, output_file_path=None):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    parsed_xml = minidom.parseString(xml_content)
    pretty_xml = parsed_xml.toprettyxml(indent="  ", newl="\n", encoding="utf-8").decode("utf-8")
    pretty_xml = '\n'.join(line for line in pretty_xml.split('\n') if line.strip())
    pretty_xml = pretty_xml.replace('/>', '></note>')
    pretty_xml = re.sub(r'(<note[^>]*>)\s+(</note>)', r'\1\2', pretty_xml)

    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(pretty_xml)
    else:
        print(pretty_xml)
