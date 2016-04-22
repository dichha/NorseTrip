from django import template
register = template.Library()


@register.assignment_tag
def to_list(*args):
   return args

@register.filter(name='indent')
def indent_string(val, num_spaces=4):
	return val.replace('\n','\n'+' '*num_spaces)

@register.filter
def split(str,splitter):
	return str.split(splitter) 