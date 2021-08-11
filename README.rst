sphinx-apischema
================

|code_ci| |docs_ci| |coverage| |pypi_version| |license|

Sphinx extension to autodoc for apischema annotated classes/functions

============== ==============================================================
PyPI           ``pip install sphinx-apischema``
Source code    https://github.com/dls-controls/sphinx-apischema
Documentation  https://dls-controls.github.io/sphinx-apischema
============== ==============================================================

If you have a class that looks like this:

.. code:: python

    from dataclasses import dataclass
    from apischema import schema
    from typing_extensions import Annotated as A

    @dataclass
    class MyClass:
        """Holds some very useful information about an object.

        We might use this in a registry of all the objects we have
        """

        name: A[str, schema(description="The name of the object")]
        age: A[float, schema(description="How old it is", min=0.0, max=1000.0)] = 5

        def summary(
            self,
            hide_age: A[bool, schema(description="Be secretive about the true age")] = True,
        ) -> str:
            """Return a nicely formatted summary of the object"""
            age = "***" if hide_age else self.age
            return f"{self.name}: {age}"

Generates documenation that looks like this:

|MyClass|

.. |code_ci| image:: https://github.com/dls-controls/sphinx-apischema/workflows/Code%20CI/badge.svg?branch=master
    :target: https://github.com/dls-controls/sphinx-apischema/actions?query=workflow%3A%22Code+CI%22
    :alt: Code CI

.. |docs_ci| image:: https://github.com/dls-controls/sphinx-apischema/workflows/Docs%20CI/badge.svg?branch=master
    :target: https://github.com/dls-controls/sphinx-apischema/actions?query=workflow%3A%22Docs+CI%22
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/dls-controls/sphinx-apischema/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dls-controls/sphinx-apischema
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/sphinx-apischema.svg
    :target: https://pypi.org/project/sphinx-apischema
    :alt: Latest PyPI version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

.. |MyClass| image:: https://raw.githubusercontent.com/dls-controls/spinx-apischema/master/docs/images/MyClass.png

See https://dls-controls.github.io/sphinx-apischema for more detailed documentation.
