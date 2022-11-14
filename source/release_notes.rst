.. currentmodule:: wradlib

Release Notes
=============

Please note that :math:`\omega radlib` releases follow `semantic versioning <https://semver.org/>`_. API breaks will be announced via deprecation warnings. All :math:`\omega radlib` releases come without any warranty. Release notes might be incomplete. See `here <https://github.com/wradlib/wradlib/commits/main>`_ for a complete record of changes.

You can install the latest :math:`\omega radlib` release from PyPI via ``$ pip install wradlib`` or specific version via ``$ pip install wradlib==x.y.z``. The recommended installation process is described in :doc:`installation`.

Version 1.18.0
--------------

**New features**

* Histo cut enhancement (:issue:`602`) by `@overeem11 <https://github.com/overeem11>`_, (:pull:`603`) and (:pull:`605`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance code**

* xradar compatibility preparations (:pull:`599`) and (:pull:`602`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance - CI**

* MNT: update CI actions, python versions (:pull:`604`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Bugfixes**

* Changes in # read metadata under get_radiosonde() (:issue:`596`) and (:pull:`597`) by `@JulianGiles <https://github.com/JulianGiles>`_
* FIX: cfradial2 coordinates (:issue:`600`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.17.0
--------------

**New features**

* MNT: use Bearer Token instead of credentials (:pull:`584`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* FIX: enable ODIM reader to read `qualityN` fields (similar to `dataN`) (:pull:`588`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* ENH: read RADOLAN ascii format (:issue:`593`) by `@SandeepAllampalli <https://github.com/SandeepAllampalli>`_ and (:pull:`594`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* ENH: add RADVOR products RV, RE and RQ (:issue:`591`) by `@heistermann <https://github.com/heistermann>`_ and (:pull:`594`) by `@heistermann <https://github.com/heistermann>`_ and `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance code**

* MNT: add pre-commit (:pull:`577`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* Pre Erad2022 (:pull:`580`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* MNT: fix SRTM testing if resource is not available, implement timeout (:issue:`586`) and (:pull:`587`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Bugfixes**

* Use numpy.linspace in ipol.interpolate_polar (:pull:`576`) by `@syedhamidali <https://github.com/syedhamidali>`_
* FIX: explicitely cast ray indices to int in cfradial1 reader (:pull:`579`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* FIX: add missing finally (:pull:`581`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* FIX: cfradial1 reader alignments (:pull:`585`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* FIX: use 'None' instead of ambiguous 'False' (`0`) for comparison (:pull:`595`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.16.0
--------------

**New features**

* add "ancillary"-keyword to io.radolan._radolan_file (:pull:`574`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* update DWD grids (:pull:`568`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add open_gpm_dataset (:pull:`571`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance - Code**

* update docstring for classify_echo_fuzzy (:pull:`570`) by `@swatelet <https://github.com/swatelet>`_
* use np.expand_dims instead of np.newaxis to make functions work with xarray DataArray (:pull:`568`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance - CI**

* add nc-time-axis to notebook-environment (:pull:`568`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Bugfixes**

* fix RADOLAN xarray coordinates (which have been off by 0.5km) (:pull:`568`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Deprecations**

* removes GDAL < 3 compatibility code (:pull:`568`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.15.0
--------------

**New features**

* add Furuno backend (``scn`` and ``SCNX`` files) for ``Xarray`` (:pull:`567`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.14.0
--------------

**New features**

* zonalstats enhancements, new VectorSource class, geopandas connector and more (:pull:`558`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance - Code**

* refactor deprecated xarray functionality  (:pull:`533`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use f-strings where appropriate (:pull:`537`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* remove unnecessary object-inheritance (:pull:`538`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* replace distutils.version.LooseVersion with packaging.version.Version (:pull:`539`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use dict-literals (:pull:`542`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance - Build/CI**

* cancel previous CV builds (:pull:`534`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use provision-with-micromamba action (:pull:`543`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Bugfixes**

* remove zero padding of bits in rainbow format (truncate excess bits from flagmap) (:issue:`549`) (:pull:`550`) by `@binomaiheu <https://github.com/binomaiheu>`_
* raise ValueError if projection cannot be determined from source dataset (:issue:`551`) (:pull:`553`) `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* output full timeslice when calling to_netcdf with no timestep (:issue:`552`) (:pull:`554`) `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* handle variable number of gates in CfRadial1 backend (:issue:`545`) (:pull:`555`) `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use radar site altitude in bin_altitude calculation (:issue:`546`) (:pull:`556`) `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* take precision into account for RADOLAN WN product (:issue:`548`) (:pull:`557`) `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* correct elevation for negative angles in iris/sigmet RAW data (:issue:`560`) (reported by Ozan Pirbudak from Turkish Met Service)  (:pull:`561`) `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* fix AttributeError: 'str' object has no attribute 'item' (:issue:`562`) (:pull:`561`) `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use start date/time if end date/time is missing for ODIM reader (:issue:`563`) (reported by Anna Gabbert from University of Graz) (:pull:`564`) `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.13.0
--------------

**New features**

* add IRIS/Sigmet backend for ``Xarray`` (:issue:`361`) (:pull:`520`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add Rainbow backend for ``Xarray`` (:issue:`394`, :issue:`459`) suggested by `@wcwoo <https://github.com/wcwoo>`_ and `@maxok <https://github.com/maxok>`_ (:pull:`522`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance**

* optionalize dependencies (dask, gdal, h5netcdf, h5py, netCDF4, requests, xmltodict) (:pull:`531`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* utilize pytest-doctestplus (:pull:`530`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* update deprecated matplotlib functionality (:pull:`530`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* docstring updates in several functions (:pull:`530`, ) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* docstring updates in several functions

**Bugfixes**

* use reasonable default values in `io.xarray.to_odim` (gain, offset, nodata, undetect, fillvalue)
* add cf attributes when reading GAMIC files (:pull:`523`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* fix regression in legacy GAMIC reader (:pull:`523`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* catch `dt.accessor` TypeError (:pull:`529`)  by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* fix thread-lock issue, if dask is not installed (:pull:`531`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use int instead np.int in radolan header parser (:pull:`531`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* fix several tests (:pull:`531`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* other minor fixes distributed over several PR's

Version 1.12.0
--------------

* withdrawn, please use 1.13.0.

Version 1.11.0
--------------

**New features**

* add support for RADOLAN HG product (:pull:`495`) by `@v4lli <https://github.com/v4lli>`_
* add %M, %J and %Y RADOLAN products (:issue:`504`) (:pull:`517`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance**

* rename master -> main
* fix docstrings (links, types, minor issues) (:pull:`518`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add .git-blame-ignore-revs (:pull:`519`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Bugfixes**

* minor fixes in GAMIC and CfRadial readers (:pull:`492`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use default values for ODIM/OPERA what-group (:pull:`496`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* do not restrict variables, but read all variables for Cf/Radial1 data (:pull:`497`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* correct calculation of angle resolution in ODIM/GAMIC xarray readers reported by `@TiemoMathijssen <https://github.com/TiemoMathijssen>`_ (:pull:`501`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add mode-kwarg to radolan coordinates/grid functions (:issue:`499`) reported by `@gogglesguy <https://github.com/gogglesguy>`_ (:pull:`502`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add kwarg origin and FutureWarning to IRIS CartesianImage reader (:issue:`493`) (:pull:`503`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* remove unnecessary gridshape kwarg from docstring in CartesianVolume (:issue:`444`) by `@fuxb <https://github.com/fuxb>`_ (:pull:`505`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* correctly handle single/multiple elevations in wradlib.vis.plot_scan_strategy (:pull:`507`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* fix ODIM xarray reader issues (:issue:`513`), (:issue:`514`) (:pull:`515`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* mention dask in all open_*_mfdataset functions (:issue:`510`) by `@Guruprasadhegde <https://github.com/Guruprasadhegde>`_ (:pull:`516`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.10.0
--------------

**New features**

* add ODIM/GAMIC/CfRadial backends for ``Xarray`` (:pull:`487`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add RADOLAN backend for ``Xarray`` (:pull:`480`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* decode IRIS ``DB_XHDR`` as numpy structured array (:issue:`362`) (:pull:`488`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance**

* move CI to GitHub Actions (:pull:`477`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* create/use earthdata credentials for srtm data (:pull:`481`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* address numpy DeprecationWarnings (:pull:`479`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Bugfixes**

* fix _FillValue and GAMIC dynamic range (:pull:`486`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* fix doctest example in vpr-module (:pull:`478`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* fix handle kwarg change scipy.cKDTree (:pull:`474`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.9.0
-------------

**New features**

* make wradlib.io capable of consuming file-like objects (:issue:`448`) (:pull:`469`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* read truncated RADOLAN composites (reported by `@franzmueller <https://github.com/franzmueller>`_) (:pull:`471`) by `@franzmueller <https://github.com/franzmueller>`_ and `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance**

* use micromamba on CI to save CI time (:issue:`457`) (:pull:`452`, :pull:`464`, :pull:`465`, :pull:`470`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add Python 3.9 builds to all CI (:pull:`463`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* adapt to new tsring handling in h5py >= 3.0 (:pull:`468`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Bugfixes**

* add capability to decode old DX header (:issue:`455`) reported by `@GolGosh <https://github.com/GolGosh>`_ (:pull:`467`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* simplify dimension angle handling ODIM/GAMIC (:pull:`462`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.8.0
-------------

**New features**

* add WN product size (1200,1000) to radolan grid, add test for correct reference point (lower left) (:issue:`448`) reported by `@julste <https://github.com/julste>`_ (:pull:`449`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add `WN` and `YW` products to radolan to xarray converter (:pull:`450`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance**

* remove deprecated and unused code and handle upstream deprecations (:pull:`450`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Bugfixes**

* fix srtm downloads windows path issues and region selection (:pull:`445`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* make `georeference_dataset` work with ND datasets (:pull:`446`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.7.4
-------------

**Bugfixes**

* update `vis.plot_scan_strategy()` (:issue:`441`) originally reported at `wradlib-users group <https://groups.google.com/g/wradlib-users/c/Vud23QpQtmo/m/ni-e_biVBAAJ>`_ by `@pandasambit15 <https://github.com/pandasambit15>`_ (:pull:`442`) by `@jorahu <https://github.com/jorahu>`_ and `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* add switch to keep elevation data unaltered (DWD terrain following scan) (:issue:`437`, :pull:`443`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.7.3
-------------

**Bugfixes**

* always translate ODIM attributes to CF attributes (:issue:`373`, :pull:`438`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* specify keys (sweep_groups) which should be saved using to_netcdf (:pull:`440`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance**

* pin isort  (:pull:`438`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.7.2
-------------

**Bugfixes**

* rework ODIM RHI elevation angle retrieval (:pull:`435`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**Maintenance**

* use pytest for testing, implement "@require_data" to be able to run tests in case of missing wradlib-data (:pull:`434`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* enhance azure ci workflow by adding flake8 linter and uploading coverage (:pull:`436`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* minor changes to README.md

Version 1.7.1
-------------

**Maintenance**

* add azure CI tests
* code formatting according to black/isort/flake8, add setup.cfg
* add show_versions
* use new semver parse
* add github templates
* all above done in (:pull:`432`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.7.0
-------------

**Highlights**

* implement generalized :py:func:`util.derivate` function with improved NaN-handling (:pull:`419`, :pull:`423`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* complete rework of phidp/kdp estimation code (Vulpiani) including new keyword-parameters, handling of ndimensional arrays,
  using ``scipy.integrate.cumtrapz`` instead of ``np.cumsum`` (:pull:`412`, :pull:`422`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* new interpolators on regular grids (:pull:`390`, :pull:`429`, :pull:`430`) by `@egouden <https://github.com/egouden>`_ and `@kmuehlbauer <https://github.com/kmuehlbauer>`_

**New features**

* reimplement `dp.linear_despeckle` as :py:func:`util.despeckle` (:pull:`420`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* read RHI in ODIM reader (:pull:`424`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* new :py:func:`.get_earth_projection` and :py:func:`.get_radar_projection` functions (:pull:`379`) by `@egouden <https://github.com/egouden>`_
* new convenience functions :py:func:`.set_raster_indexing` and :py:func:`.set_coordinate_indexing` (:pull:`429`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* implement rainrate decoder to iris reader (:pull:`428`) by `@tsmsalper <https://github.com/tsmsalper>`_

**Bugfixes**

* correct padding and nan-filling for multidimensional arrays in ``dp.texture`` (:pull:`418`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* introduce ``call_kwargs`` in :py:func:`comp.togrid` (:issue:`373`) reported by `@jorahu <https://github.com/jorahu>`_  (:pull:`425`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.6.2
-------------

* re-add removed IRIS features (:issue:`415`, :pull:`416`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.6.1
-------------

* use LooseVersion to check for dependency matching (:issue:`413`, :pull:`414`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

Version 1.6.0
-------------

**Highlights**

* improvements of georef.raster module (:pull:`376`) by `@egouden <https://github.com/egouden>`_
* implement multi-file ODIMH5-reader/writer (:pull:`397`, :pull:`409` and :pull:`410`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_ and `@egouden <https://github.com/egouden>`_
* simplify `zr`-module, add handling of multidimensional arrays (:pull:`408`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_
* use __all__ in submodules (georef, io) to specify exported/documented functions (:issue:`386`, :pull:`388`) by `@kmuehlbauer <https://github.com/kmuehlbauer>`_

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
