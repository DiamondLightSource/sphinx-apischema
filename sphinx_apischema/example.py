from dataclasses import dataclass
from typing import Type, TypeVar

from apischema import schema
from typing_extensions import Annotated as A

# Maximum age we support for an object
_MAX_AGE = 1000.0

#: TypeVar representing MyClass or a subclass of it
Cls = TypeVar("Cls", bound="MyClass")

# Used below whenever we have a name argument
AName = A[str, schema(description="The name of the object")]


@dataclass
class MyClass:
    """Holds some very useful information about an object.

    We might use this in a registry of all the objects we have
    """

    name: AName
    age: A[float, schema(description="How old it is", min=0.0, max=_MAX_AGE)] = 5

    def summary(
        self,
        hide_age: A[bool, schema(description="Be secretive about the true age")] = True,
    ) -> str:
        """Return a nicely formatted summary of the object"""
        age = "***" if hide_age else self.age
        return f"{self.name}: {age}"

    @classmethod
    def old(cls: Type[Cls], name: AName) -> Cls:
        """Return an old object"""
        return cls(name, age=100)

    @staticmethod
    def oldest() -> float:
        """Return the maximum age we support for an object"""
        return _MAX_AGE


def say_hello(name: AName) -> str:
    """Return a polite greeting"""
    return f"Hello {name}"
