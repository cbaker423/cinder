..
      Copyright 2010-2012 United States Government as represented by the
      Administrator of the National Aeronautics and Space Administration.
      All Rights Reserved.

      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

===========================================
Cinder, the OpenStack Block Storage Service
===========================================

Cinder is an OpenStack project to provide "block storage as a service".

* **Component based architecture**: Quickly add new behaviors
* **Highly available**: Scale to very serious workloads
* **Fault-Tolerant**: Isolated processes avoid cascading failures
* **Recoverable**: Failures should be easy to diagnose, debug, and rectify
* **Open Standards**: Be a reference implementation for a community-driven api

This documentation is generated by the Sphinx toolkit and lives in the source
tree. Additional draft and project documentation on Cinder and other components
of OpenStack can be found on the `OpenStack wiki`_. Cloud administrators, refer
to `docs.openstack.org`_.

.. _`OpenStack wiki`: https://wiki.openstack.org/wiki/Main_Page
.. _`docs.openstack.org`: https://docs.openstack.org


Installation Guide
~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   Installation Guide <install/index>
   Upgrade Process <upgrade>

Administration Guide
~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   admin/index

Configuration Reference
~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
    :maxdepth: 2

    configuration/index

    Sample Configuration File <sample_config>

    Sample Policy File <sample_policy>

    drivers

CLI Reference
~~~~~~~~~~~~~

Information on the commands available through Cinder's Command Line
Interface (CLI) can be found in this section of documentation.

Full documentation on the python-cinderclient is in the
`python-cinderclient documentation`_.

.. _`python-cinderclient documentation`: https://docs.openstack.org/python-cinderclient/latest

.. toctree::
   :maxdepth: 2

   cli/index
   cinder-manage Usage <man/cinder-manage>

Contributor/Developer Docs
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   contributor/index


API Extensions
~~~~~~~~~~~~~~

Go to https://developer.openstack.org/api-ref/block-storage/ for information
about Cinder API extensions.

:doc:`Block Storage v3 API Microversion History </contributor/api_microversion_history>`:
The block storage v3 API evolves over time through
:doc:`API Microversions </contributor/api_microversion_dev/>`. This
provides the history of all those changes. Consider it a "what's new" in the
block storage v3 API.

Indices and tables
~~~~~~~~~~~~~~~~~~

* :ref:`genindex`
* :ref:`search`

Glossary
~~~~~~~~

.. toctree::
   :maxdepth: 1

   common/glossary.rst
