import xml.etree.ElementTree as ET
import xml.dom.minidom

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

#Set base directory
base_route = ""

def merge_notes(xml1, xml2):
    merged = ET.Element("notes", version="1")
    labels = xml1.find('labels')
    if labels is not None:
        merged.append(labels)

    notes_dict = {}
    for note in xml1.findall('.//note') + xml2.findall('.//note'):
        notes_dict[note.attrib['player']] = note

    insert_index = 1 if labels is not None else 0

    for note in notes_dict.values():
        if note.text is None or not note.text.strip():
            note.text = ' '
        merged.insert(insert_index, note)
        insert_index += 1

    return merged


def save_xml(root, file_path):
    def indent(elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or elem.text.strip():
                elem.text = i + "  "
            for child in elem:
                indent(child, level + 1)
            if not elem.tail or elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or elem.tail.strip()):
                elem.tail = i
        if not elem.tail or elem.tail.strip():
            elem.tail = "\n" + (level - 1) * "  "

    indent(root)
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)


xml1 = read_xml(base_route + 'first.xml')
xml2 = read_xml(base_route + 'second.xml')

merged_xml = merge_notes(xml1, xml2)

save_xml(merged_xml, base_route + 'merged.xml')
