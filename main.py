#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from broable import isBroable
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render('templates/index.html',{}))

class BroableHandler(webapp.RequestHandler):
    def get (self):
        
        #isBroable = isBroable(self.request.get("q"))
        #        if (self.request.get("q") == None or isBroable(self.request.get("q")) is False):
        query = self.request.get("q")
        if query == "" or not isBroable(query):
            self.response.out.write("Nah, brah")
        else:
            self.response.out.write("Fuck yea")
            #        self.response.out.write(isBroable(self.request.get("q")))

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/broable', BroableHandler)
                                          ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
