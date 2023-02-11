Installation
============

.. _ref-installation:

Anaconda/Conda
--------------

In order to run :math:`\omega radlib`, you need to have a Python interpreter installed on your local computer, as well as a number of Python packages (`Dependencies`_). We recommend installing `Anaconda <https://www.anaconda.com/products/individual>`_ as it includes Python, numerous required packages, and other useful tools (e.g. `Spyder <https://www.spyder-ide.org/>`_).

Using Anaconda the installation process is harmonised across platforms. Download and install the latest `Anaconda distribution <https://www.anaconda.com/products/individual>`_ for your specific OS. We recommend using the minimal `Miniforge or Mambaforge <https://github.com/conda-forge/miniforge>`_ if you do not want to install a full scientific python stack (see `Mambaforge`_).

We are constantly performing tests with `conda-forge <https://conda-forge.org/>`_ community channel (for the most recent 3 python versions).

If your Anaconda Python installation is working, the following command (in a console) should work::

    $ python --version
    Python 3.7.3 :: Continuum Analytics, Inc.

Now you can use the ``conda`` package and environment manager (`conda documentation <https://conda.io/docs/>`_) to setup your :math:`\omega radlib` installation.

#. Add the conda-forge channel, where :math:`\omega radlib` and its dependencies are located. Read more about the community effort `conda-forge <https://conda-forge.org/>`_::

    $ conda config --add channels conda-forge

#. Use strict channel priority to prevent channel clashes::

    $ conda config --set channel_priority strict

#. Create a new environment from scratch::

    $ conda create --name wradlib python=3.11

#. Activate the :math:`\omega radlib` environment::

    $ conda activate wradlib

#. Install :math:`\omega radlib` and its dependencies::

    (wradlib) $ conda install wradlib

Now you have a ``conda`` environment with a working :math:`\omega radlib` installation.

Mambaforge
----------

This is our recommended method. The install procedure is essentially the same as with Anaconda/Miniconda but it will utilize the fast drop-in replacement `mamba <https://mamba.readthedocs.io/>`_. Please refer to their documentation.

Testdrive
---------

Test the integrity of your :math:`\omega radlib` installation by opening a console window and typing calling the python interpreter::

    $ python
    Python 3.11.0 | packaged by conda-forge | (main, Jan 14 2023, 12:27:40) [GCC 11.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.

The Python prompt should appear. Then type::

    >>> import wradlib
    >>> wradlib.__version__
    '1.19.0'

If everything is ok, this will show the running :math:`\omega radlib` version. If the :math:`\omega radlib` package is not found by the interpreter, you will get::

    >>> import wradlib
    ImportError: No module named wradlib

Alternatively, you can install the `Bleeding edge code`_, but you have to keep track of :math:`\omega radlib's` dependencies yourself.


Bleeding edge code
------------------

.. warning:: The :math:`\omega radlib` version on `PyPI <https://pypi.org/project/wradlib>`__ might lag behind the actual developments. You can use the bleeding edge code from the :math:`\omega radlib` `repository <https://github.com/wradlib/wradlib>`_. Note, however, that you need to make sure yourself that all `Dependencies`_ are met (see below).

`Download <https://codeload.github.com/wradlib/wradlib/zip/main>`_ the source, unzip, and run::

    $ python -m pip install .

Alternatively, you can add the :math:`\omega radlib` directory to your environment variable ``PYTHONPATH``.


Installing via pip
------------------

Although we recommend using the Anaconda Python Environment you can install :math:`\omega radlib` from `PyPi <https://pypi.org/project/wradlib/>`__ via ``pip``.

Open a terminal and run::

    $ python -m pip install wradlib

Depending on your system you might need to be root (or sudo the above command) for this to work.
``pip`` will then fetch the source distribution from the Python Package Index and run the installation.

Afterwards it will check for any dependencies not met, yet.

Be aware that using ``pip`` we can only look for python-module dependencies.
For example the numpy module itself depends on some other libraries, which need to be present in order for the module to compile properly after being downloaded by ``pip``. We have no control over these dependencies and it is rather hard to give a complete overview.

Therefore we recommend trying to satisfy the dependencies using your favorite package management system.

Installing via ``pip`` tries to install all dependencies, but be sure to have all depending non-python libraries installed. Wheels are not available for all dependencies (eg. GDAL).


.. _ref-dependencies:

Dependencies
------------

:math:`\omega radlib` was not designed to be a self-contained library. Besides extensive use of Numpy and Scipy, :math:`\omega radlib` uses additional libraries, which you might need to install before you can use :math:`\omega radlib` depending on your system and installation procedure.

.. tabularcolumns:: |L|L|L|

+------------+-----------+-------------+
| Package    |    min    | recommended |
+============+===========+=============+
| numpy      | >= 1.9    | >= 1.21.0   |
+------------+-----------+-------------+
| scipy      | >= 1.0    | >= 1.7.0    |
+------------+-----------+-------------+
| matplotlib | >= 3      | >= 3.3.0    |
+------------+-----------+-------------+
| xarray     | >= 0.17   | >= 0.20.2   |
+------------+-----------+-------------+
| xradar     | >=0.0.13  | >= 0.0.13   |
+------------+-----------+-------------+

You can check whether the required `Dependencies`_ are available on your computer by opening a Python console and enter:

>>> import <package_name>
ImportError: No module named <package_name>

This will be the response in case the package is not available.

In case the import is successful, you should also check the version number:

>>> package_name.__version__
some version number

The version number should be consistent with the above `Dependencies`_.


Optional Dependencies
---------------------

Apart from the obligatory `Dependencies`_, some dependencies in :math:`\omega radlib` are optional. This is because the installation of these dependencies can be somewhat tedious while many :math:`\omega radlib` users will not need them anyway. In case users use a :math:`\omega radlib` function that requires an optional dependency, and this dependency is not satisfied in the local environment, :math:`\omega radlib` will raise an exception.

As for now, the following dependencies are defined as optional:

.. tabularcolumns:: |L|L|L|

+------------+-----------+-------------+
| Package    |    min    | recommended |
+============+===========+=============+
| cartopy    | >= 0.21   | >= latest   |
+------------+-----------+-------------+
| dask       | >= 2.20   | >= latest   |
+------------+-----------+-------------+
| gdal       | >= 2.4    | >= 3.1.0    |
+------------+-----------+-------------+
| h5py       | >= 2.0.1  | >= 3.1.0    |
+------------+-----------+-------------+
| h5netcdf   | >= 0.8.0  | >= 0.10.0   |
+------------+-----------+-------------+
| netCDF4    | >= 1.0    | >= 1.5.0    |
+------------+-----------+-------------+
| requests   | >= 2.23.0 | >= 2.26.0   |
+------------+-----------+-------------+
| xmltodict  | >= 0.11   | >= 0.12.0   |
+------------+-----------+-------------+

The following libraries are used by `netCDF4`, `h5py`/`h5netcdf` and `gdal` packages and should apply to these requirements:

.. tabularcolumns:: |L|L|L|L|

+------------+-----------+-------------+---------+
| Library    |    min    | recommended | used by |
+============+===========+=============+=========+
| geos       | >= 3.7.0  | >= 3.10.0   | gdal    |
+------------+-----------+-------------+---------+
| hdf5       | >= 1.9.0  | >= 1.12.1   | h5py    |
+------------+-----------+-------------+---------+
| libnetcdf  | >= 4.7.3  | >= 4.8.1    | netCDF4 |
+------------+-----------+-------------+---------+
| proj       | >= 5.2.0  | >= 8.0.0    | gdal    |
+------------+-----------+-------------+---------+


**The speedup module**

The speedup module is intended as a collection of Fortran code in order to speed up specific :math:`\omega radlib` function that are critical for performance.
In order to build the speedup module as a shared library, you need to use f2py (https://numpy.org/doc/stable/f2py/usage.html). f2py usually ships with numpy and should be available via the command line. To test whether f2py is available on your system, execute ``f2py`` on the system console. Or, alternatively, ``f2py.py``. If it is available, you should get a bunch of help instructions. Now change to the :math:`\omega radlib` module directory and execute on the system console::

    $ f2py.py -c -m speedup speedup.f

Now the speedup module should be available.

.. _ref-knownissues:

Known Issues
------------

Depending on your OS and installation method you may encounter different problems. Here are some guidelines for attacking them.

We strongly recommend using the Anaconda conda package and environment manager (see `Installation`_). Using `conda-forge <https://conda-forge.org/>`_ we will maintain the `wradlib-feedstock <https://github.com/conda-forge/wradlib-feedstock/>`_ for constant availability of recent :math:`\omega radlib` versions.

If you can't use Anaconda/Miniconda/Mambforge, it is generally a good idea to use your systems package manager to install dependencies. This will also take account for other needed bindings, libs etc.

If you encounter problems installing :math:`\omega radlib`, check on your favorite search engine or create an issue `at the wradlib issue tracker <https://github.com/wradlib/wradlib/issues>`_ with details on the problem or check with the `openradar-discourse <https://openradar.discourse.group/>`_.
