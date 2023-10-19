from lxml import etree


def extract_namespaces(xpath):
    parts = xpath.split('/')
    namespaces = {}
    for part in parts:
        if ':' in part:
            prefix, _ = part.split(':')
            if prefix not in namespaces:
                namespaces[prefix] = None
    return namespaces


def create_or_update_xpath(xml_string, xpath, value):
    root = etree.fromstring(xml_string)
    namespaces = extract_namespaces(xpath)

    for prefix in namespaces.keys():
        ns = root.nsmap.get(prefix)
        if ns is not None:
            namespaces[prefix] = ns

    existing_element = root.xpath(xpath, namespaces=namespaces)

    if existing_element:
        existing_element[0].text = value
    else:
        xpath_parts = xpath.strip('/').split('/')
        current_element = root

        for part in xpath_parts:
            prefixed_part = part.split(':')[1] if ':' in part else part
            next_element = current_element.find(prefixed_part, namespaces=namespaces)

            if next_element is None:
                next_element = etree.SubElement(current_element, prefixed_part)

            current_element = next_element

        current_element.text = value

    return etree.tostring(root, pretty_print=True).decode('utf-8')


# Example usage
xml_string = '''
<ns:catalog xmlns:ns="http://example.com/namespace">
    <ns:book>
        <ns:chapter>
            <ns:sentence>
                <ns:word>existing_value</ns:word>
            </ns:sentence>
        </ns:chapter>
    </ns:book>
</ns:catalog>
'''

xpath = '/ns:catalog/ns:book/ns:chapter/ns:sentence/ns:word'
value = 'pranita'

new_xml_string = create_or_update_xpath(xml_string, xpath, value)
print(new_xml_string)
