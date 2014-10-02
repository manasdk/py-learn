from jinja2 import Template

template_str = 'first={{first}}\n' \
               'last={{last}}'
template = Template(template_str)
stream = template.stream({'first': 'John', 'last': 'Doe'})

count = 0
while True:
    try:
        count += 1
        resolved = stream.next()
        print count, resolved
    except StopIteration:
        break

generator = template.generate({'first': 'John', 'last': 'Doe'})

count = 0
for s in generator:
    count += 1
    print count, s
