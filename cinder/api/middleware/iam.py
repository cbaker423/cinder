# Copyright 2010 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Common Auth Middleware.

"""


import os

from oslo_config import cfg
from oslo_log import log as logging
import webob.dec

from cinder.i18n import _
from cinder.wsgi import common as base_wsgi

CONF = cfg.CONF
LOG = logging.getLogger(__name__)

class IAMMiddleware(object):

    def __init__(self, app, conf):
        self.app = app

    @webob.dec.wsgify(RequestClass=base_wsgi.Request)
    def __call__(self, req):
        LOG.debug("CBAKE: THIS IS A TEST")
        f = open("/tmp/cbake_IAM.txt", "w+")
        f.write("CBAKE IS COOL")
        f.close()
	return self.app


def iam_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    def iam_filter(app, conf):
        return IAMMiddleware(app)
    return iam_filter
