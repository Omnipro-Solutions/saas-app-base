import json
from json.decoder import JSONDecodeError

import requests
from requests.models import Response


class OmniRequest:
    @staticmethod
    def call_api(url, http_method, body: dict = {}, params={}, headers={}, **kwargs):
        request_params = {
            "method": http_method,
            "url": url,
            "headers": headers,
            "params": params,
        }
        if body:
            request_params["data"] = json.dumps(body).encode("utf-8")
            request_params["headers"]["Content-Type"] = "application/json"
            request_params["headers"]["charset"] = "utf-8"
        return requests.request(**request_params | kwargs)

    @staticmethod
    def get_response(response: Response):

        if not isinstance(response, Response):
            raise Exception("Param 'response' not atribute 'Response' class")

        def strftimedelta(t):
            mm, ss = divmod(t.seconds, 60)
            hh, mm = divmod(mm, 60)
            s = "%d:%d:%02d:%02d.%06d" % (t.days, hh, mm, ss, t.microseconds)
            return s

        response_object = dict(
            success=response.ok,
            status_code=response.status_code,
            decode=False,
            json_data={},
            content_type="json",
            elapsed=strftimedelta(response.elapsed),
            reason=response.reason,
            method=response.request.method,
            path_url=response.request.path_url,
            url=response.request.url,
            request_header=dict(response.request.headers),
            response_header=dict(response.headers),
        )

        try:
            json_data = response.json()
            decode = True
        except JSONDecodeError:
            json_data = response.text
            decode = False

        response_object["json_data"] = json_data
        response_object["decode"] = decode
        return response_object
