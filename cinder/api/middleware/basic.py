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
from six.moves import http_client
import webob.dec

from cinder.i18n import _
from cinder import context
from cinder.wsgi import common as base_wsgi

CONF = cfg.CONF
LOG = logging.getLogger(__name__)

class IAMMiddleware(base_wsgi.Middleware):

    @webob.dec.wsgify(RequestClass=base_wsgi.Request)
    def __call__(self, req):
        LOG.debug("CBAKE: THIS IS A TEST IN IAM MIDDLEWARE")
        if 'X-Auth-Token' not in req.headers:
            user_id = req.headers.get('X-Auth-User', 'admin')
            project_id = req.headers.get('X-Auth-Project-Id', 'admin')
            os_url = os.path.join(req.url, project_id)
            res = webob.Response()
            # NOTE(vish): This is expecting and returning Auth(1.1), whereas
            #             keystone uses 2.0 auth.  We should probably allow
            #             2.0 auth here as well.
            res.headers['X-Auth-Token'] = '%s:%s' % (user_id, project_id)
            res.headers['X-Server-Management-Url'] = os_url
            res.content_type = 'text/plain'
            res.status_int = http_client.NO_CONTENT
            return res

        token = req.headers['X-Auth-Token']
        user_id, _sep, project_id = token.partition(':')
        project_id = project_id or user_id
        remote_address = getattr(req, 'remote_address', '127.0.0.1')
        LOG.debug("REMOTE_ADDR: " + remote_address)
        if CONF.use_forwarded_for:
            remote_address = req.headers.get('X-Forwarded-For', remote_address)
        ctx = context.RequestContext(user_id,
                                     project_id,
                                     is_admin=True,
                                     remote_address=remote_address)

        req.environ['cinder.context'] = ctx
        LOG.debug("CBAKE: EXITING IAM MIDDLEWARE")
        return self.application



def iam_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    def iam_filter(app, conf):
        return IAMMiddleware(app)
    return iam_filter
