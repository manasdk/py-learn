import sys

from jinja2 import Template, Environment, StrictUndefined


env = Environment(undefined=StrictUndefined)


def is_template(template_str):
    template = Template(template_str)
    return template_str != template.render({})


def is_circular(dependencies):
    def next(dependency):
        if not dependency:
            return None
        return dependencies.get(dependency, None)
    single = dependencies.items()[0][0]
    # double moves at 2x the speed
    double = next(next(single))
    print single, double
    if not double:
        return False
    while double != single:
        single = next(single)
        double = next(next(double))
        print single, double
        if not single or not double:
            return False
    return True


def render_with_self(template_dict):
    context = {}
    to_render = {}
    dependency = {}
    for k, v in template_dict.items():
        if not is_template(str(v)):
            context[k] = v
        else:
            to_render[k] = v
    print 'to_render : ', to_render
    while len(context) != len(template_dict):
        for k, v in to_render.items():
            template = env.from_string(v)
            try:
                rendered = template.render(context)
                null_rendered = Template(v).render({})
                if rendered != null_rendered:
                    context[k] = rendered
                to_render
            except:
                msg = sys.exc_info()[1].message
                first_quote = msg.find('\'')
                start = first_quote + 1
                end = first_quote + msg[first_quote + 1:].find('\'') + 1
                dependency[k] = msg[start: end]
                # print k, 'Failed to render.', msg
        if is_circular(dependency):
            print 'Circular dependency found.'
            break
    print 'dependency : ', dependency
    print 'context : ', context

print '----------'
render_with_self({
    'a': 1,
    'b': '{{a}}',
    'c': '{{a}} {{b}}'
})

print '\n----------'
render_with_self({
    'x': '{{y}} {{z}}',
    'y': '1',
    'z': '{{y}}'
})

print '\n----------'
render_with_self({
    'a': '{{b}}',
    'b': '{{c}}',
    'c': '{{a}}'
})

print '\n----------'
render_with_self({
    'a': '{{a}}',
    'b': '{{c}}',
    'c': '{{a}}'
})

print '\n----------'
render_with_self({
    'a': '{{b}}',
    'b': '{{c}}',
    'c': '{{d}}',
    'd': '{{e}}',
    'e': '{{a}}'
})
