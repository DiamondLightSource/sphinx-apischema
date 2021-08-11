import inspect
from unittest.mock import Mock, call

from sphinx_apischema import (
    __version__,
    before_process_signature,
    process_docstring,
    process_signature,
)
from sphinx_apischema import setup as sa_setup
from sphinx_apischema.example import MyClass, say_hello


def test_example():
    assert MyClass("foo", 32).summary(hide_age=True) == "foo: ***"
    assert MyClass.old("foo") == MyClass("foo", 100)
    assert MyClass.oldest() == 1000
    assert say_hello("me") == "Hello me"


def get_signature_docstring(obj, what, bound_method=False):
    before_process_signature("app", obj, bound_method)
    sig, _ = process_signature("app", what, "name", obj, "options", "()", "return")
    lines = inspect.getdoc(obj).splitlines()
    process_docstring("app", what, "name", obj, "options", lines)
    return sig, lines


def test_class():
    assert get_signature_docstring(MyClass, "class") == (
        "(name, age=5)",
        [
            "Holds some very useful information about an object.",
            "",
            ":param str name: The name of the object",
            ":param float age: How old it is - minimum: 0.0, maximum: 1000.0",
            "",
            "We might use this in a registry of all the objects we have",
        ],
    )


def test_method():
    assert get_signature_docstring(MyClass.summary, "method", True) == (
        "(hide_age=True)",
        [
            "Return a nicely formatted summary of the object",
            "",
            ":param bool hide_age: Be secretive about the true age",
            "",
        ],
    )


def test_classmethod():
    assert get_signature_docstring(MyClass.old, "method", True) == (
        "(name)",
        [
            "Return an old object",
            "",
            ":param str name: The name of the object",
            "",
        ],
    )


def test_staticmethod():
    assert get_signature_docstring(MyClass.oldest, "method") == (
        "()",
        ["Return the maximum age we support for an object"],
    )


def test_function():
    assert get_signature_docstring(say_hello, "function") == (
        "(name)",
        [
            "Return a polite greeting",
            "",
            ":param str name: The name of the object",
            "",
        ],
    )


def test_setup():
    app = Mock()
    assert sa_setup(app) == {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
    app.connect.assert_has_calls(
        [
            call("autodoc-before-process-signature", before_process_signature),
            call("autodoc-process-signature", process_signature),
            call("autodoc-process-docstring", process_docstring),
        ]
    )
