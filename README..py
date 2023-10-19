import xml.etree.ElementTree as ET

xml_string = '''
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications
      with XML.</description>
   </book>
</catalog>
'''

def update_or_add_xml(xml_string, parent_path, tag, new_value):
    root = ET.fromstring(xml_string)

    parent_element = root.find(parent_path)
    if parent_element is None:
        raise ValueError(f"Parent element not found for path '{parent_path}'")

    element = parent_element.find(tag)
    if element is not None:
        element.text = new_value
    else:
        new_element = ET.SubElement(parent_element, tag)
        new_element.text = new_value

    return ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')


updated_xml = update_or_add_xml(xml_string, './book/author', 'rohan1', 'Elemalue')
print(updated_xml)
