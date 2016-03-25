import httplib2
import json

from onadata.apps.restservice.RestServiceInterface import RestServiceInterface


class ServiceDefinition(RestServiceInterface):
    id = u'json'
    verbose_name = u'JSON POST'

    def send(self, url, submission_instance):
        post_data = json.dumps(submission_instance.json)
        headers = {"Content-Type": "application/json"}
        http = httplib2.Http()
        resp, content = http.request(uri=url, method='POST',
                                     headers=headers,
                                     body=post_data)
