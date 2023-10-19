import xml.etree.ElementTree as ET

xml_string = '''
<catalog xmlns:dc="http://example.com/dc" xmlns:ex="http://example.com/ex">
   <ex:book id="bk101">
      <author>
         <a>
            <b>
            <c>qef</c></b>
         </a> 
      </author>

      <dc:title>XML Developer's Guide</dc:title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications
      with XML.</description>
   </ex:book>   
   <ex:apple id="bk102">
      <dc:author>Ralls, Kim</dc:author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies,
      an evil sorceress, and her own childhood to become queen
      of the world.</description>
      <ex:longParent>
         <ex:longChild1>
            <ex:longChild2>
               <dc:targetElement>Original Value</dc:targetElement>
            </ex:longChild2>
         </ex:longChild1>
      </ex:longParent>
   </ex:apple>
</catalog>
'''

namespaces = {
    'dc': 'http://example.com/dc',
    'ex': 'http://example.com/ex'
}

def update_or_add_xml(xml_string, parent_path, tag, new_value, namespaces):
    root = ET.fromstring(xml_string)
    ET.register_namespace('ex', namespaces['ex'])
    ET.register_namespace('dc', namespaces['dc'])

    parent_element = root.find(parent_path, namespaces)
    if parent_element is None:
        raise ValueError(f"Parent element not found for path '{parent_path}'")

    element = parent_element.find(tag, namespaces)
    if element is not None:
        element.text = new_value
    else:
        new_element = ET.SubElement(parent_element, ET.QName(namespaces['dc'], tag))
        new_element.text = new_value

    return ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')


long_parent_path = './ex:apple/ex:longParent/ex:longChild1/ex:longChild2'
updated_xml = update_or_add_xml(xml_string, long_parent_path, 'dc:targetElement1', 'New Value1', namespaces)
print(updated_xml)
