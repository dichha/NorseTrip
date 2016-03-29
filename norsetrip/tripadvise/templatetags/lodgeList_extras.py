from django import template
register = template.Library()

#@register.tag
# def collect(parser, token):
#     bits = list(token.split_contents())
#     if len(bits) > 3 and bits[-2] == 'as':
#         varname = bits[-1]
#         items = bits[1:-2]
#         return CollectNode(items, varname)
#     else:
#         raise template.TemplateSyntaxError('%r expected format is "item [item ...] as varname"' % bits[0])

# class CollectNode(template.Node):
#     def __init__(self, items, varname):
#         self.items = map(template.Variable, items)
#         self.varname = varname

#     def render(self, context):
#         context[self.varname] = [i.resolve(context) for i in self.items]

@register.tag('to_list')
def to_list(_parser, token):
    try:
        parts = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, \
          "%r tag requires at least one argument" % token.contents.split()[0]

    return AsListNode(parts[1:])

class AsListNode(template.Node):
    def __init__(self, parts):
        self.parts = map(lambda p: template.Variable(p), parts)

    def render(self, context):
        resolved = []
        for each in self.parts:
            resolved.append(each.resolve(context))
        return resolved