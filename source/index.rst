.. wradlib documentation main file, created by
   sphinx-quickstart on Wed Oct 26 13:48:08 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

wradlib: An Open Source Library for Weather Radar Data Processing
=================================================================

:Release: |release-link|
:Date: |today|
:notebooks: |notebooks-link|
:docs: |docs-link|

The :math:`\omega radlib` project has been initiated in order facilitate the use of weather radar data as well as to provide a common platform for research on new algorithms. :math:`\omega radlib` is an open source library which is well documented and easy to use. It is written in the free programming language `Python <https://www.python.org>`_. As of version 1.3 :math:`\omega radlib` is Python 3 only.

.. note::

   Please cite :math:`\omega radlib` as *Heistermann, M., Jacobi, S., and Pfaff, T.: Technical Note: An open source library for processing weather radar data (wradlib), Hydrol. Earth Syst. Sci., 17, 863-871,* doi:`10.5194/hess-17-863-2013, 2013 <https://hess.copernicus.org/articles/17/863/2013/hess-17-863-2013.pdf>`_

   If you refer to a specific :math:`\omega radlib` version please cite using :math:`\omega radlib`'s zenodo doi:`10.5281/zenodo.1209843 <https://doi.org/10.5281/zenodo.1209843>`_ for this version.


.. image:: images/old_radarpic.png

Weather radar data is potentially useful in meteorology, hydrology and risk management. Its ability to provide information on precipitation
with high spatio-temporal resolution over large areas makes it an invaluable tool for short term weather forecasting or flash flood forecasting.

:math:`\omega radlib` is designed to assist you in the most important steps of processing weather radar data. These may include: reading common data formats, georeferencing, converting reflectivity to rainfall intensity, identifying and correcting typical error sources (such as clutter or attenuation) and visualising the data.

This documentation is under steady development. It provides a complete library reference as well as a set of tutorials which will get you started in working with :math:`\omega radlib`.

Documentation
-------------

**Installation**

* :doc:`installation`
* :doc:`docker`
* :doc:`ide`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Getting started

   installation
   docker

**User Guide**

* :doc:`user_guide`
* :doc:`notebooks/fileio`
* :doc:`notebooks/georeferencing`
* :doc:`Echo Classification <notebooks/classify>`
* :doc:`Attenuation Correction <notebooks/attenuation/wradlib_attenuation>`
* :doc:`Interpolation <notebooks/interpolation/wradlib_ipol_example>`
* :doc:`Rainfall Adjustment <notebooks/multisensor/wradlib_adjust_example>`
* :doc:`zonalstatistics`
* :doc:`Visualisation <notebooks/plotting>`
* :doc:`specials`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Tutorials & examples

   user_guide
   notebooks/fileio
   notebooks/georeferencing
   Echo Classification <notebooks/classify>
   Attenuation Correction <notebooks/attenuation/wradlib_attenuation>
   Interpolation <notebooks/interpolation/wradlib_ipol_example>
   Rainfall Adjustment <notebooks/multisensor/wradlib_adjust_example>
   zonalstatistics
   Visualisation <notebooks/plotting>
   specials

**Help & reference**

* :doc:`reference`
* :doc:`community`
* :doc:`dev_guide`
* :doc:`zreferences`
* :doc:`release_notes`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Help & reference

   reference
   community
   dev_guide
   zreferences
   release_notes

License
-------

wradlib is available under the open source `MIT License`__.

__ https://opensource.org/licenses/MIT

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
