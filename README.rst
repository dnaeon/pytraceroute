pytraceroute - A simple traceroute(8) implementation in Python
===============================================================

pytraceroute is a simple `traceroute(8)` implementation written in
Python.

Its purpose is mainly educational, rather than something
feature-rich as is `traceroute(8)` for example.

Requirements
============

* Python 2.7.x or 3.x
* docopt

Installation
============

Clone the Git repository and install:

.. code-block:: bash

   $ git clone https://github.com/pytraceroute
   $ cd pytraceroute && python setup.py install

Or via `pip`:

.. code-block:: bash

   $ pip install pytraceroute

Usage
=====

pytraceroute requires root permissions due to the use
of raw (`socket.SOCK_RAW`) sockets.

Example usage:

.. code-block:: bash

   $ sudo py-traceroute google.com

Contributions
=============

pytraceroute is hosted on `Github`_. Please contribute by
reporting issues, suggesting features or by sending patches using
pull requests.

Bugs
====

Probably. If you experience a bug issue, please report it to the
pytraceroute issue tracker on `Github`_.

.. _`Github`: https://github.com/dnaeon/pytraceroute
