from django import template
register = template.Library()


@register.assignment_tag
def to_list(*args):
   return args

@register.filter
def not_in( hotel,hotel_list,):
    return hotel not in hotel_list

@register.filter
def is_in(hotel, mylist):
    return hotel in mylist

@register.filter
def unique_hotel(hotel_list):
    noDupes = []
    [noDupes.append(hotel) for hotel in hotel_list if not noDupes.count(hotel)]
    return noDupes

@register.filter(name='indent')
def indent_string(val, num_spaces=4):
	return val.replace('\n','\n'+' '*num_spaces)

@register.filter
def split(str,splitter):
	return str.split(splitter) 
    
    

    