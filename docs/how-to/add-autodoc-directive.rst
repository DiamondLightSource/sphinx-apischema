.. _API:

Add autodoc directive
=====================

Once you have followed the `../tutorials/installation`, then
`sphinx.ext.autodoc` will call sphinx-apischema for every `automodule`,
`autoclass`, `automethod` and `autofunction` it finds.

Example code
------------

The following code is distributed as ``sphinx_apischema.example``:

.. literalinclude:: ../../sphinx_apischema/example.py
    :language: python

The directive
-------------

You can add documentation for it to your sphinx project by placing the following
directive in any rst file:

.. code:: rst

    .. automodule:: sphinx_apischema.example
        :members:

This will generate the following documentation in your output HTML:

.. automodule:: sphinx_apischema.example
    :members:
