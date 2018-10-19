Developer Guide
===============

Setup
-----
The section :doc:`installation` will provide you with detailed guidance on how to install :math:`\omega radlib` and the required dependencies for different operating systems (MS Windows, Linux, Mac OS). :math:`\omega radlib` |release| has been tested with the latest Anaconda Python on linux-64, osx-64 and MS Windows 32 and 64 versions.

As a developer, though, you should rather link into :math:`\omega radlib`'s version control. This way, it will be easier for you to track changes and to contribute your changes to :math:`\omega radlib`'s main respository (see next section). Just install `Git <https://git-scm.com/>`_, then clone the :math:`\omega radlib` repository to your local system by executing the following command in your shell: ``git clone https://github.com/wradlib/wradlib.git``. Do not forget to set the ``PYTHONPATH`` to point to the corresponding directory.


Contributing to :math:`\omega radlib`
-------------------------------------
Everyone can contribute to the developement of :math:`\omega radlib` by using the Fork and Pull model. For this purpose, you need to set up ``Git`` (see section `Setup`_). Then see section :doc:`community` for further instructions on how to create a Pull Request.


Building the docs
-----------------
In order to build the documentation, you need to download the `wradlib-docs <https://github.com/wradlib/wradlib-docs>`_ repository. You need to satisfy a few more dependencies which are mainly related to Sphinx. These are specified in the `readthedocs_environment.yml <https://github.com/wradlib/wradlib-docs/blob/master/readthedocs_environment.yml>`_.

Once these requirements are met, you can open a console window within the ``wradlib-docs``-repository and execute ``sphinx-build -v -b html source/ doc-build``. This will give you the latest documentation under the ``wradlib-docs/doc-build`` directory. Simply open the index.html file to view the documentation.


Testing
-------
:math:`\omega radlib` uses the `unittest <https://pythontesting.net/framework/unittest/unittest-introduction/>`_ framework. New functions should come with corresponding unittests in the ``wradlib/wradlib/tests`` directory. Just have a look at `available tests <https://github.com/wradlib/wradlib/tree/master/wradlib/tests>`_ to get an idea. In addition, examples and docstrings are a good way to combine testing and documentation. Have a look at the `wradlib-notebooks <https://github.com/wradlib/wradlib-notebooks/tree/master/notebooks>`_ in order to get an idea on how to set these up correctly. In the docstrings, the ``Examples`` section will be tested by our testing framework. This could look like this::

    def foo(a):
        """Docstring to be evaluated by doctest

        Examples
        --------
        >>> from wradlib.some_module import foo
        >>> print(foo(3))
        4
        """
        return a + 1


Continuous Integration
----------------------
We use `Travis_CI <https://travis-ci.org>`_ for Continuous Integration (CI). CI means, in our case, that each commit pushed to :math:`\omega radlib`'s main repository will trigger the test suites on Travis-CI. If all tests pass successfully, a new documentation will be built on https://readthedocs.org and published on https://docs.wradlib.org. In case a new release tag is associated with a commit, a new release will be distributed via `PyPI <https://pypi.org/project/wradlib/>`_.
