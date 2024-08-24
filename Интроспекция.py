def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    obj_doc = obj.__doc__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module, 'obj_doc': obj_doc}
    return info


number_info = introspection_info(42)
print(number_info)
