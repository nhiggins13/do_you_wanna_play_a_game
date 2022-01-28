import enum
import logging
from typing import Union, Any, Dict, Optional, Type


def make_factory_class(factory_name: str, factory_label_enum: Optional[Type[enum.Enum]] = None):
    """
    Create a new factory class

    :param factory_name: Name of the factory class
    :param factory_label_enum: Optional Enum used as labels in the factory
    :return:  A ModelFactory derived class
    """

    class _NewFactory(ModelFactory):
        label = factory_label_enum
        registry: Dict[str, type] = dict()

    _NewFactory.__name__ = factory_name
    return _NewFactory


class ModelFactory(object):
    """
    Factory base class that provides class method implementations
    for common functionality for all derived factory classes

    A derived factory class only needs to provide a registry map
    when defined:

    class XFactory(ModelFactory):
        registry = {}
    """

    @classmethod
    def create(self, label: str, *args: Any, **kwargs: Any):
        """

        :param label:
        :param args:
        :param kwargs:
        :return:
        """

        klass = self.registry.get(label, None)

        if not klass:
            raise ValueError("Factory %s does not have the droid you're looking for(%s)" % (self.__name__, label))

        #  Initialize and return object instance
        logger = logging.getLogger(__name__)
        obj = klass(*args, **kwargs)

        if logger.hasHandlers():
            logger.debug("Initialized instance %s of from %s" %(label, self.__name__))

        return obj

    @classmethod
    def register(self, label: str, klass):
        if not isinstance(label, str):
            raise ValueError('label %s not a string')

        if label in self.registry:
            raise ValueError('Label %s already registered' % label)

        self.registry[label] = klass

        logger = logging.getLogger(__name__)
        if logger.hasHandlers():
            logger.debug('"%s" registered in %s' % (label, self.__name__))


def register(class_name: str, factory: ModelFactory):

    def _decorator(klass: Any) -> Any:
        factory.register(class_name, klass)
        return klass

    return _decorator


test = make_factory_class('test')