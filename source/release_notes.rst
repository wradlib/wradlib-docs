Release Notes
=============

Please note that :math:`\omega radlib` releases follow `semantic versioning <https://semver.org/>`_. API breaks will be announced via deprecation warnings. All :math:`\omega radlib` releases come without any warranty. Release notes might be incomplete. See `here <https://github.com/wradlib/wradlib/commits/master>`_ for a complete record of changes.

You can install the latest :math:`\omega radlib` release from PyPI via ``$ pip install wradlib`` or specific version via ``$ pip install wradlib==x.y.z``. The recommended installation process is described in :doc:`installation`.


Bleeding Edge
-------------

**Highlights**

* added xarray-powered reader/writer for Cf/Radial and ODIM_H5

Version 1.2.0
-------------

**Highlights**

* significantly speed up functions using interpolation classes
* add `classify` module including 2d membershipfunctions hydrometeor classification
* fix conformance, correctness and consistency issues in wradlib-docs (thanks `@CAM-Gerlach <https://github.com/CAM-Gerlach>`_)

**New features**

* add new header token `VR` and `U` to radolan header parser
* add `load_vector`-method to `zonaldata.DataSource`
* enable `zonaldata.ZonaldataBase` to take `DataSource` objects as parameters
* add `get_radiosonde` to `io.misc` to retrieve radiosonde data from internet
* add `minalt` keyword argument to `vpr.make_3d_grid`

**Bugfixes**

* update links, fix typos, improve CI workflow
* fix bug in all adjustment classes when checking for None
* show angle axis curvelinear grid again
* align docstring with actual code and use `sweep` in iris-reader

Version 1.1.0
-------------

**Highlights**

* use with-statement in rainbow-reader
* fix in gpm-reader and rainbow_reader
* fix issues with cg-plot in vis-module
* fix in gdal/ogr exception handling
* update in versioning/release procedure
* automatic build of devel-docs

Version 1.0.0
-------------

**Highlights**

* export ``notebooks`` into dedicated `wradlib-notebooks <https://github.com/wradlib/wradlib-notebooks/>`_
* export ``doc`` into dedicated `wradlib-docs <https://github.com/wradlib/wradlib-docs/>`_
* complete rewrite of CI-integration
* complete rework of modules

Pre 1.0.0 Versions
------------------

Versions before 1.0.0 are available from the `wradlib-old <https://github.com/wradlib/wradlib-old/>`_ repository.
