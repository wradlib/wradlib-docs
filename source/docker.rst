Using Docker
============

Overview
--------

Especially for easy integration with servers we setup the `wradlib-docker <https://github.com/wradlib/wradlib-docker/>`_ repository. There we provide the Dockerfiles for five different docker images in feature branches. Those docker images are build automatically and are available on `docker-hub <https://hub.docker.com/r/wradlib/wradlib-docker/tags/>`_.

The **branch** names are the docker **tag** names:

#. base

   * based on *centos7*
   * plain miniconda installation

#. min

   * based on *base*
   * conda *wradlib* environment with latest wradlib release including all runtime dependencies

#. notebook

   * based on *min*
   * added notebook packages to conda *wradlib* environment

#. full

   * based on *notebook*
   * added wradlib build dependencies to conda *wradlib* environment

#. training

   * based on *full*
   * added additional scientific python packages to conda *wradlib* environment

Installation
------------

In order to run these docker images as containers, you need to have *docker* installed on your local computer or server. Please refer to the `docker documentation <https://docs.docker.com/install/>`_ for installation guidance. Once you have docker installed and running you can use the provided *wradlib-docker* images. You can either pull them directly from docker hub or create them locally from the `wradlib-docker <https://github.com/wradlib/wradlib-docker/>`_ repository.

#. Pull from docker hub using the wanted tag::

    $ docker pull wradlib/wradlib-docker:min

#. Build from scratch::

    $ git clone https://github.com/wradlib/wradlib-docker.git
    $ cd wradlib-docker
    $ git checkout min
    $ docker build -t wradlib_min .

The only difference is then in the `docker run` command, where `wradlib/wradlib-docker:min` is used in the first and `wradlib_min` in the second case.

Running docker images
---------------------

Which docker image you need to use depends strongly on your preferences. Here only some applications are shown.

Minimal wradlib
^^^^^^^^^^^^^^^

Here 5 different approaches for running containers are shown.

#. Start container directly into bash::

    $ docker run -ti --name wradlib_min wradlib/wradlib-docker:min /bin/bash
    [wradlib@0f994a690230 /]$ source activate wradlib
    (wradlib) [wradlib@0f994a690230 /]$ python
    Python 3.6.5 | packaged by conda-forge | (default, Apr  6 2018, 13:39:56)
    [GCC 4.8.2 20140120 (Red Hat 4.8.2-15)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> wradlib.version.full_version
    '1.0.0'
    >>>

#. Start container directly into python (wradlib env)::

    $ docker run -ti --name wradlib_min wradlib/wradlib-docker:min /opt/conda/envs/wradlib/bin/python
    Python 3.6.5 | packaged by conda-forge | (default, Apr  6 2018, 13:39:56)
    [GCC 4.8.2 20140120 (Red Hat 4.8.2-15)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

#. Initialize *wradlib* user with your users id::

    $ docker run -ti --name wradlib_min -e LOCAL_USER_ID=$UID wradlib/wradlib-docker:min /bin/bash
    (wradlib) [wradlib@0f994a690230 /]$

#. Mount host-folder into container (rw, assuming we are in current users /home-folder, replace user with your current user)::

    $ mkdir docker-test
    $ cd docker-test
    $ echo "Greetings from the host" > greets.txt
    $ docker run -ti --name wradlib_min -e LOCAL_USER_ID=$UID -v /home/user/docker-test:/home/docker-test wradlib/wradlib-docker:min /bin/bash
    [wradlib@d6ffc3a7bbe5 /]$ cat /home/docker-test/greets.txt
    Greetings from the host
    $ [wradlib@d6ffc3a7bbe5 /]$ echo "Greetings from the container" >> /home/docker-test/greets.txt
    $ [wradlib@d6ffc3a7bbe5 /]$ exit
    $ cat greets.txt
    Greetings from the host
    Greetings from the container

#. Start container with X11 capabilities (eg. for use of matplotlib)::

    $ XSOCK=/tmp/.X11-unix/
    $ XAUTH=/tmp/.docker.xauth
    $ touch $XAUTH
    $ xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -
    $ GID=`id -g $USER`
    $ docker run -ti --name wradlib_min_x11 -e LOCAL_GROUP_ID=$GID -e LOCAL_USER_ID=$UID -e LOCAL_USER_NAME=$USER -v $XSOCK:$XSOCK:rw -v $XAUTH:$XAUTH:rw -e XAUTHORITY=${XAUTH} -e DISPLAY wradlib/wradlib-docker:min /bin/bash
    [user@7324bddd3b81 /]$ source activate wradlib
    (wradlib) [user@7324bddd3b81 /]$ python
    Python 3.6.5 | packaged by conda-forge | (default, Apr  6 2018, 13:39:56)
    [GCC 4.8.2 20140120 (Red Hat 4.8.2-15)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import wradlib as wrl
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> data = np.random.random((360,1000))
    >>> fig = plt.figure()
    >>> wrl.vis.plot_ppi(data, fig=fig)
    >>> plt.show()

This will open a matplotlib figure on your current $DISPLAY.

Jupyter Notebook Server
^^^^^^^^^^^^^^^^^^^^^^^

You can run a jupyter notebook server using the `notebook` using the following setup. You would need to download `wradlib-notebooks <https://github.com/wradlib/wradlib-notebooks>`_ and `wradlib-data <https://github.com/wradlib/wradlib-data>`_. The docker run command mounts the host folders containing `wradlib-notebooks` and `wradlib-data` into the container::

    $ docker run -ti --name wradlib_nb -p 8888:8888 -v /host/path/to/wradlib-notebooks:/home/notebooks -v /host/path/to/wradlib-data:/home/wradlib-data -e LOCAL_USER_ID=$UID -e WRADLIB_DATA=/home/wradlib-data wradlib/wradlib-docker:notebook /opt/conda/envs/wradlib/bin/jupyter notebook --notebook-dir=/home/notebooks --ip='*' --port=8888

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
