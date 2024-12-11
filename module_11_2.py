import inspect

def introspection_info(obj):
    my_dict = {}
    my_dict['Тип объекта: '] = type(obj)
    atributes = dir(obj)
    my_dict['Атрибуты объекта: '] = atributes
    methods = [attr for attr in atributes if callable(getattr(obj, attr))]
    my_dict['Методы объекта: '] = methods
    my_dict['Модуль, к которому объект принадлежит: '] = inspect.getmodule(obj)
    return my_dict


number_info = introspection_info(inspect)
for key, value in number_info.items():
    print(key, value)
