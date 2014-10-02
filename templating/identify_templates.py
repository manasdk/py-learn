from jinja2 import Template


def is_template(template_str):
    template = Template(template_str)
    rendered = template.render({})
    print template_str, rendered, template_str == rendered

is_template('{{a}} {{b}}')
is_template('John Doe.')
