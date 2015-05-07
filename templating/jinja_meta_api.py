from jinja2 import Template, Environment, StrictUndefined, meta


env = Environment(undefined=StrictUndefined)


def is_template(template_str):
    template = Template(template_str)
    return template_str != template.render({})


def analyze_dependency(template_dict):
    context = {}
    to_render = {}
    for k, v in template_dict.items():
        if not is_template(str(v)):
            context[k] = v
        else:
            to_render[k] = v
    print 'to_render : ', to_render
    print 'context : ', context
    dependencies = {}
    for k, v in to_render.items():
        ast = env.parse(v)
        dependencies[k] = meta.find_undeclared_variables(ast)

    def check_dependencies(dep_chain):
        last_idx = len(dep_chain) - 1
        last_value = dep_chain[last_idx]
        for dependency in dependencies.get(last_value, []):
            if dependency in dep_chain:
                dep_chain.append(dependency)
                return True
            dep_chain.append(dependency)
            if check_dependencies(dep_chain):
                return True
            dep_chain.pop()

    for k in dependencies:
        dep_chain = []
        dep_chain.append(k)
        if check_dependencies(dep_chain):
            print 'Circular dependecy found - ', dep_chain
            return True

print '----------'
analyze_dependency({
    'a': 1,
    'b': '{{a}}',
    'c': '{{a}} {{b}}'
})

print '\n----------'
analyze_dependency({
    'x': '{{y}} {{z}}',
    'y': '1',
    'z': '{{y}}'
})

print '\n----------'
analyze_dependency({
    'a': '{{b}}',
    'b': '{{c}}',
    'c': '{{a}}'
})

print '\n----------'
analyze_dependency({
    'a': '{{a}}',
    'b': '{{c}}',
    'c': '{{a}}'
})

print '\n----------'
analyze_dependency({
    'a': '{{b}}',
    'b': '{{c}}',
    'c': '{{d}}',
    'd': '{{e}}',
    'e': '{{a}}'
})

print '\n----------'
analyze_dependency({
    'a': '{{b}} {{c}}',
    'b': '{{c}}',
    'c': '{{d}}',
    'd': '1'
})
