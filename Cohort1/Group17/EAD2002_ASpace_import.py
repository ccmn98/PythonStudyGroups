



from lxml import etree
import random
import string

# Function to generate a random string
def generate_random_string():
    length = random.randint(5, 10)
    letters = string.ascii_letters
    random_part = ''.join(random.choice(letters) for _ in range(length))
    # Include the prefix 'container_'
    random_string = 'container_' + random_part
    return random_string
    

# Parse the XML file
xml_file_path = r'U:\StrikeTeam\ArchivesSpace\Mike converted\ms009117_ead2002schema.xml'
tree = etree.parse(xml_file_path)
root = tree.getroot()

# Define the namespaces
namespace = {'ead': 'urn:isbn:1-931666-22-9'}

# Register the namespace with etree
etree.register_namespace('ead', 'urn:isbn:1-931666-22-9')

# Find all physdesc elements
physdesc_elements = root.xpath('.//ead:physdesc', namespaces=namespace)

# Update each physdesc element
for physdesc in physdesc_elements:
    # Get the current text content
    extent_text = physdesc.text.strip() if physdesc.text else ''

    # Create a new extent element
    extent_element = etree.Element('{urn:isbn:1-931666-22-9}extent')
    extent_element.text = extent_text

    # Clear the current physdesc element and set its attributes
    physdesc.clear()
    physdesc.set('label', 'Extent')
    physdesc.set('encodinganalog', '300')

    # Append the new extent element
    physdesc.append(extent_element)

# Find all container elements and add an id attribute with a random string
container_elements = root.xpath('.//ead:container', namespaces=namespace)

for container in container_elements:
    container.set('id', generate_random_string())

# Save the modified XML to a new file
new_file_path = r'U:\StrikeTeam\ArchivesSpace\Mike converted\python_reconfigured\python_ms009117_ASpace_test_2.xml'
tree.write(new_file_path, pretty_print=True, xml_declaration=True, encoding='utf-8')

print(f"XML file has been updated and saved as {new_file_path}.")
