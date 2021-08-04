import sys
from importlib import import_module
from neomodel import (RelationshipDefinition, StructuredRel, OUTGOING, RelationshipManager, INCOMING, EITHER)


# basestring python 3.x fallback
class OverWriteManager(RelationshipManager):
    def __str__(self):
        direction = 'either'
        if self.definition['direction'] == OUTGOING:
            direction = 'a outgoing'
        elif self.definition['direction'] == INCOMING:
            direction = 'a incoming'

        return "{0} in {1} direction of type {2} on node ({3}) of class '{4}'".format(
            self.description, direction,
            self.definition['relation_type'], self.source.id, self.source_class.__name__)

    def _check_node(self, obj):
        """check for valid node i.e correct class and is saved"""
        if not issubclass(type(obj), tuple(self.definition['node_class'])):
            raise ValueError("Expected node of class " + str(self.definition['node_class']))
        if not hasattr(obj, 'id'):
            raise ValueError("Can't perform operation on unsaved node " + repr(obj))


class OverWriteDefinition(RelationshipDefinition):
    def __init__(self, relation_type, cls_names, direction, manager=OverWriteManager, model=None):
        super().__init__(relation_type, cls_names, direction, manager=OverWriteManager, model=None)

    def _lookup_node_class(self):
        self.definition['node_class'] = []
        for cls_name in self._raw_class:
            if not isinstance(cls_name, str):
                self.definition['node_class'].append(cls_name)
            else:
                name = cls_name
                if name.find('.') == -1:
                    module = self.module_name
                else:
                    module, _, name = name.rpartition('.')

                if module not in sys.modules:
                    # yet another hack to get around python semantics
                    # __name__ is the namespace of the parent module for __init__.py files,
                    # and the namespace of the current module for other .py files,
                    # therefore there's a need to define the namespace differently for
                    # these two cases in order for . in relative imports to work correctly
                    # (i.e. to mean the same thing for both cases).
                    # For example in the comments below, namespace == myapp, always
                    if not hasattr(self, 'module_file'):
                        raise ImportError("Couldn't lookup '{0}'".format(name))

                    if '__init__.py' in self.module_file:
                        # e.g. myapp/__init__.py -[__name__]-> myapp
                        namespace = self.module_name
                    else:
                        # e.g. myapp/models.py -[__name__]-> myapp.models
                        namespace = self.module_name.rpartition('.')[0]

                    # load a module from a namespace (e.g. models from myapp)
                    if module:
                        module = import_module(module, namespace).__name__
                    # load the namespace itself (e.g. myapp)
                    # (otherwise it would look like import . from myapp)
                    else:
                        module = import_module(namespace).__name__
                self.definition['node_class'].append(getattr(sys.modules[module], name))


def create_relationship_to(cls_names, rel_type, cardinality=None, model=None):
    for obj in cls_names:
        if not isinstance(obj, (str, object)):
            raise ValueError('Expected class name or class got ' + repr(obj))

    if model and not issubclass(model, (StructuredRel,)):
        raise ValueError('model must be a StructuredRel')
    return OverWriteDefinition(rel_type, cls_names, OUTGOING, cardinality, model)


def create_relationship_from(cls_names, rel_type, cardinality=None, model=None):
    for obj in cls_names:
        if not isinstance(obj, (str, object)):
            raise ValueError('Expected class name or class got ' + repr(obj))

    if model and not issubclass(model, (StructuredRel,)):
        raise ValueError('model must be a StructuredRel')
    return OverWriteDefinition(rel_type, cls_names, INCOMING, cardinality, model)


def create_relationship(cls_names, rel_type, cardinality=None, model=None):
    for obj in cls_names:
        if not isinstance(obj, (str, object)):
            raise ValueError('Expected class name or class got ' + repr(obj))

    if model and not issubclass(model, (StructuredRel,)):
        raise ValueError('model must be a StructuredRel')
    return OverWriteDefinition(rel_type, cls_names, EITHER, cardinality, model)
