def createInstance(module_name, class_name, kwargs):
    module_meta = __import__(module_name, globals(), locals(), [class_name])
    class_meta = getattr(module_meta, class_name)
    print(class_meta)
    obj = class_meta(**kwargs)
    return obj


dic = {"name": "oo", "url": "asdsad"}
obj = createInstance("PreprocessData.all_class_files.Book", "Book", dic)
hh = "name"
if getattr(obj,hh) is not None:
  print(getattr(obj,hh))
print(obj.additionalType, obj.name, obj.url)
