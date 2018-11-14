from docxtpl import DocxTemplate
import jinja2

jinja_env = jinja2.Environment()

def my_filterA(value, my_string_arg):
    return_value = value + ' ' + my_string_arg
    return return_value


def my_filterB(value, my_float_arg):
    return_value = value + my_float_arg
    return return_value

jinja_env.filters['my_filterA'] = my_filterA
jinja_env.filters['my_filterB'] = my_filterB


context = {'base_value_string' : ' Hello', 'base_value_float' : 1.5 }

tpl=DocxTemplate('test_template.docx')
tpl.render(context, jinja_env)
tpl.save('test_output.docx')
