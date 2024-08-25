def introspection_info(obj):
    obj_type = type(obj).__name__
    dir_ = dir(obj)
    attributes = [attribute for attribute in dir_ if not callable(getattr(obj, attribute))]
    methods = [method for method in dir_ if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}
    return info


number_info = introspection_info(42)
print(number_info)
"""number_info = introspection_info(42.33)
print(number_info)
number_info = introspection_info("(42, 33)")
print(number_info)
number_info = introspection_info([42, 33])
print(number_info)
number_info = introspection_info((42, 33))
print(number_info)
number_info = introspection_info({42, 33})
print(number_info)
number_info = introspection_info({42: 33})
print(number_info)"""
