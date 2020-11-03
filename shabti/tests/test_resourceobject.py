# shabti/test/test_resourceobject.py
import pytest

from shabti import ResourceObject


class TestResourceObject(ResourceObject):
    __test__ = False

    def info(self):
        pass

    @classmethod
    def _create_path(cls, *args):
        pass


def test_new_object():
    test_object = TestResourceObject(1401561)

    assert isinstance(test_object, ResourceObject)
    assert test_object.id == 1401561
