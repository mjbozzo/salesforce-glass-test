# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""RequestHandlers for starter project."""

__author__ = 'alainv@google.com (Alain Vongsouvanh)'


# Add the library location to the path
import sys
sys.path.insert(0, 'lib')

import webapp2
import beatbox
import xmltramp
import datetime
import ez_setup
import setstatus
import soql2atom



from attachmentproxy.handler import ATTACHMENT_PROXY_ROUTES
from main_handler import MAIN_ROUTES
from notify.handler import NOTIFY_ROUTES
from oauth.handler import OAUTH_ROUTES
from signout.handler import SIGNOUT_ROUTES


ROUTES = (
    ATTACHMENT_PROXY_ROUTES + MAIN_ROUTES + NOTIFY_ROUTES + OAUTH_ROUTES +
    SIGNOUT_ROUTES)


app = webapp2.WSGIApplication(ROUTES)
########################################

sf = beatbox._tPartnerNS
svc = beatbox.Client()
beatbox.gzipRequest=False

username = 'glass.test@rs.salesforce.com'
password = 'salesforce1XaFMMKO66yAOdVcwNQLZC9av'

loginResult = svc.login(username, password)

print "sid = " + str(loginResult[sf.sessionId])
print "welcome " + str(loginResult[sf.userInfo][sf.userFullName])

ImageFromGlass__c = {
    'ImageName__c':'Test Inserted!!'
}
res = svc.create(ImageFromGlass__c)
if not res[0]['errors']:
    contact_id = res[0]['id']
else:
    raise Exception('Contact creation failed {0}'.format(res[0]['errors']))

"""
svc = Client()
svc.login('glass.test@salesforce.com', 'salesforce1EAFIZ8b7PBqOfaEhWHPPIwNxq')

ImageFromGlass__c = {
    'ImageName__c':'Test Inserted!!'
}
res = svc.create(ImageFromGlass__c)
if not res[0]['errors']:
    contact_id = res[0]['id']
else:
    raise Exception('Contact creation failed {0}'.format(res[0]['errors']))
"""

########################################
