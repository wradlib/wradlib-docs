Release Notes
=============

Please note that :math:`\omega radlib` releases follow `semantic versioning <https://semver.org/>`_. API breaks will be announced via deprecation warnings. All :math:`\omega radlib` releases come without any warranty. Release notes might be incomplete. See `here <https://github.com/wradlib/wradlib/commits/master>`_ for a complete record of changes.

You can install the latest :math:`\omega radlib` release from PyPI via ``$ pip install wradlib`` or specific version via ``$ pip install wradlib==x.y.z``. The recommended installation process is described in :doc:`installation`.

Version 1.6.0
-------------

**Highlights**

* improvements of georef.raster module (:pull:`376`) by `@egouden <https://github.com/egouden>`_
* implement multi-file ODIMH5-reader/writer (:pull:`397`, :pull:`409` and :pull:`410`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_ and `@egouden <https://github.com/egouden>`_
* simplify `zr`-module, add handling of multidimensional arrays (:pull:`408`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use __all__ in submodules (georef, io) to specify exported/documented functions (:gh:`386`, :pull:`388`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**New features**

* add STATUS product to Iris/Sigmet reader (:pull:`378`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* improvements of georef.raster module (:pull:`376`) by `@egouden <https://github.com/egouden>`_
* add PRF and NSAMPLES to ODIM reader (:pull:`393`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* refactor code into `assign_root`-function (:pull:`393`) by `@egouden <https://github.com/egouden>`_
* add ODIM WRAD moment (:pull:`406`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Bugfixes**

* apply correct decoding of VEL, WIDTH and KDP IrisCartesianProductFile (:pull:`378`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add missing `requests` dependency to CI (:pull:`374`) by `@s-m-e <https://github.com/s-m-e>`_
* correct error in documentation of sweep_centroids (:pull:`383`) by `@ElmerJeanpierreLopez <https://github.com/ElmerJeanpierreLopez>`_
* adapt `georef.polar.sweep_centroids` to only use angles in degrees (:pull:`385`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* work around issue, where ODIM `startime` == `endtime` (:pull:`391`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* improve handling of equal sized dimensions (:pull:`393`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use xarray `Dataset.drop_vars` instead of deprecated `Dataset.drop` (:pull:`398`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use xarray.Dataset.rename instead of rename_dims (:pull:`402`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add missing `+`-sign in projection string (:pull:`405`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* fix filter_cloudtype (low cloud switch removes everything) (:pull:`401`) by `@egouden <https://github.com/egouden>`_
* use Dataset.swap_dims instead of rename (:pull:`406`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.5.0
-------------

**Highlights**

* consolidation of xarray based functionality, bugfixing, feature adding
* speedup zonal statistics by using `/vsimem`, by creation of spatial and attribute index files as well as by faster reading of attributes and properties

**New features**

* make OdimH5 reader accept list of files and merge into one structure
* make `chunks` available for transparently use dask with OdimH5 and CfRadial readers
* make gdal3 compatible (added by `@egouden <https://github.com/egouden>`_)
* use `loaddata='xarray'` kwargs to output data as Xarray Dataset in `read_radolan_composite`
* CI: add Appveyor to run test-suite under Windows OS

**Bugfixes**

* use `importlib` in `import_optional`, correct multidimensional calling in `gradient_along_axis`
* several fixes for OdimH5 and Cf/Radial readers/writers
* set destination projection to destination dataset in `reproject_raster_dataset` (spotted by `wradlib-forum <https://groups.google.com/forum/#!msg/wradlib-users/-dvRhDCjgV0/X0JR4yL3BgAJ>`_)

Version 1.4.0
-------------

**Highlights**

* read sigmet/iris ingest files, redesign of sigmet reader (suggested by `@aschueth <https://github.com/aschueth>`_)
* enhance/rewrite fuzzy echo classifier (implemented with `@overeem11 <https://github.com/overeem11>`_)

**New features**

* parametrize xarray based OdimH5-reader (suggested by `@egouden <https://github.com/egouden>`_)
* add depolarization ratio calculation (implemented by `@overeem11 <https://github.com/overeem11>`_)
* add script for test profiling (added by `@egouden <https://github.com/egouden>`_)

**Bugfixes**

* remove unnecessary seek in radolan-reader (suggested by `@PPazderski <https://github.com/PPazderski>`_)
* correct handling of edge cases in `dp.texture` processing (spotted by `@overeem11 <https://github.com/overeem11>`_)
* correct decoding of DB_FLIQUID2 (sigmet-reader) (implemented by `@ckaradavut <https://github.com/ckaradavut>`_)
* correct handling of non-precip in 2D hmc (spotted by and fixed with `@bzohidov <https://github.com/bzohidov>`_)
* fix semver handling and install process (suggested by `@s-m-e <https://github.com/s-m-e>`_)
* fix import for MutableMapping (added by `@zssherman <https://github.com/zssherman>`_)

Version 1.3.0
-------------

**Highlights**

* wradlib is considered Python3 only working with Python >= 3.6
* xarray-powered reader/writer for Cf/Radial 1.X and 2.0 as well as ODIM_H5
* xarray-powered plotting using DataArray via xarray-DataArray Accessor

**New features**

* creation of xarray DataArray from spherical coordinates and radar data
* update test machinery to use pytest (mainly CI use)
* correctly apply `semver`

**Bugfixes**

* beamblockage calculation, precisely detect clear or blocked beam
* catch HTTPError in `test_radiosonde`, graceful skip test
* `spherical_to_xyz` better aligns with input dimensions

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
