How it works
============

It works by hooking into 3 `sphinx.ext.autodoc` events


autodoc-before-process-signature
--------------------------------

This is the only place it is declared if we are looking at a bound method or
not, so sphinx-apischema just keeps a record of whether the object to be
documented is a bound method or not


autodoc-process-signature
-------------------------

Autodoc currently formats ``Annotated[str, schema(...)]`` as ``str[str]``, so
sphinx-apischema reformats the signature to remove the types.

For instance what autodoc would show as ``(arg1: float[float], arg2: str[str] =
"default")`` it will produce ``(arg1, arg2="default")``


autodoc-process-docstring
-------------------------

This takes the docstring and ``:param:`` information into it after the first
blank line.

For instance it will take a docstring that looks like::

    """An introductory paragraph

    More paragraphs
    """

And produce::

    """An introductory paragraph

    :param arg1 float: The decription for arg1
    :param arg2 str: The description for arg2

    More paragraphs
    """

It will format any of the arguments to ``apischema.schema`` like ``minimum`` and
add to the description