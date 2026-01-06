

def get_attr_number(node):
    # your code goes here
    count = 0
    for elem in node.iter():
        count += len(elem.attrib)
    return count

