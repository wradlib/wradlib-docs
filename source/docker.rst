Using Docker
============

Overview
--------

Especially for easy integration with servers we setup the `wradlib-docker <https://github.com/wradlib/wradlib-docker/>`_ repository. There we provide build three different docker images. Those docker images are build automatically and are available on `docker-hub <https://hub.docker.com/r/wradlib/wradlib-docker/tags/>`_.

#. base

   * based on *centos7*
   * plain miniforge installation

#. master-min

   * based on *base*
   * conda *wradlib* environment with latest wradlib github master including all runtime dependencies

#. master-full

   * based on *base*
   * conda *wradlib* environment with latest wradlib release including all runtime dependencies
   * additional notebook and development packages

#. X.Y.Z-min

   * based on *base*
   * conda *wradlib* environment with X.Y.Z wradlib github master including all runtime dependencies

#. X.Y.Z-full

   * based on *base*
   * conda *wradlib* environment with X.Y.Z wradlib release including all runtime dependencies
   * additional notebook and development packages

Installation
------------

In order to run these docker images as containers, you need to have *docker* installed on your local computer or server. Please refer to the `docker documentation <https://docs.docker.com/install/>`_ for installation guidance. Once you have docker installed and running you can use the provided *wradlib-docker* images. You can either pull them directly from docker hub or create them locally from the `wradlib-docker <https://github.com/wradlib/wradlib-docker/>`_ repository.

#. Pull from docker hub using the wanted tag::

    $ docker pull wradlib/wradlib-docker:master-min

#. Build from scratch::

    $ git clone https://github.com/wradlib/wradlib-docker.git
    $ cd wradlib-docker
    $ export WRADLIB_VER=master
    $ export WRADLIB_DOCKER_TAG=min
    $ export DOCKER_REPO=wradlib-docker
    $ docker build --build-arg WRADLIB_VER --build-arg WRADLIB_DOCKER_TAG --build-arg DOCKER_REPO -t wradlib_min .

The only difference is then in the `docker run` command, where `wradlib/wradlib-docker:master-min` is used in the first and `wradlib_min` in the second case.

Running docker images
---------------------

Which docker image you need to use depends strongly on your preferences. Here only some applications are shown.

Minimal wradlib
^^^^^^^^^^^^^^^

Here 5 different approaches for running containers are shown.

#. Start container directly into bash::

    $ docker run -ti --name wradlib_min wradlib/wradlib-docker:master-min /bin/bash
    Container USER_ID : 9001
    Container GROUP_ID : 100
    Container USER_NAME : wradlib
    (wradlib) [wradlib@a837e1946bf2 /]$ python
    Python 3.8.5 | packaged by conda-forge | (default, Aug 29 2020, 01:22:49)
    [GCC 7.5.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import wradlib
    >>> wradlib.version.full_version
    '1.8.0-dev14+gc4345d1'
    >>>

#. Start container directly into python (wradlib env)::

    $ docker run -ti --name wradlib_min wradlib/wradlib-docker:master-min /opt/conda/envs/wradlib/bin/python
    Container USER_ID : 9001
    Container GROUP_ID : 100
    Container USER_NAME : wradlib
    Python 3.8.5 | packaged by conda-forge | (default, Aug 29 2020, 01:22:49)
    [GCC 7.5.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

#. Initialize *wradlib* user with your users id::

    $ docker run -ti --name wradlib_min -e LOCAL_USER_ID=$UID wradlib/wradlib-docker:master-min /bin/bash
    Container USER_ID : 701
    Container GROUP_ID : 100
    Container USER_NAME : wradlib
    (wradlib) [wradlib@0f994a690230 /]$

#. Mount host-folder into container (rw, assuming we are in current users /home-folder, replace user with your current user)::

    $ mkdir docker-test
    $ cd docker-test
    $ echo "Greetings from the host" > greets.txt
    $ docker run -ti --name wradlib_min -e LOCAL_USER_ID=$UID -v /home/user/docker-test:/home/docker-test wradlib/wradlib-docker:master-min /bin/bash
    Container USER_ID : 701
    Container GROUP_ID : 100
    Container USER_NAME : wradlib
    (wradlib) [wradlib@d6ffc3a7bbe5 /]$ cat /home/docker-test/greets.txt
    Greetings from the host
    $ (wradlib) [wradlib@d6ffc3a7bbe5 /]$ echo "Greetings from the container" >> /home/docker-test/greets.txt
    $ (wradlib) [wradlib@d6ffc3a7bbe5 /]$ exit
    $ cat greets.txt
    Greetings from the host
    Greetings from the container


Jupyter Notebook Server
^^^^^^^^^^^^^^^^^^^^^^^

You can run a jupyter notebook server with `master-full` using the following setup. You would need to download `wradlib-notebooks <https://github.com/wradlib/wradlib-notebooks>`_ and `wradlib-data <https://github.com/wradlib/wradlib-data>`_. The docker run command mounts the host folders containing `wradlib-notebooks` and `wradlib-data` into the container::

    $ docker run -ti --name wradlib_nb -p 8888:8888 -v /host/path/to/wradlib-notebooks:/home/notebooks -v /host/path/to/wradlib-data:/home/wradlib-data -e LOCAL_USER_ID=$UID -e WRADLIB_DATA=/home/wradlib-data wradlib/wradlib-docker:master-full /opt/conda/envs/wradlib/bin/jupyter notebook --notebook-dir=/home/notebooks --ip='*' --port=8888

    [I 08:07:35.865 NotebookApp] Writing notebook server cookie secret to /home/wradlib/.local/share/jupyter/runtime/notebook_cookie_secret
    [W 08:07:36.087 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
    [I 08:07:36.098 NotebookApp] Serving notebooks from local directory: /home/notebooks
    [I 08:07:36.098 NotebookApp] 0 active kernels
    [I 08:07:36.098 NotebookApp] The Jupyter Notebook is running at:
    [I 08:07:36.098 NotebookApp] http://[all ip addresses on your system]:8888/?token=6673cfb299fb93728c183be8a4590fc77608fb1312bce340
    [I 08:07:36.099 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [W 08:07:36.099 NotebookApp] No web browser found: could not locate runnable browser.
    [C 08:07:36.099 NotebookApp]

        Copy/paste this URL into your browser when you connect for the first time,
        to login with a token:
            http://localhost:8888/?token=6673cfb299fb93728c183be8a4590fc77608fb1312bce340

Copy/paste the given url into your local web browser and you are ready to explore the `wradlib-notebooks <https://github.com/wradlib/wradlib-notebooks>`_ together with `wradlib-data <https://github.com/wradlib/wradlib-data>`_.
