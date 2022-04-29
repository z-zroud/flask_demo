from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

class Response():
    def __init__(self, data={}, status_code=200, msg="Success"):
        self.status_code = status_code
        self.msg = ''
        if isinstance(msg, dict):
            for k, v in msg.items():
                self.msg += f"{k}:{v}. "
        else:
            self.msg = msg
        self.data = data

    
    def _to_dict(self):
        data = {'status_code': HTTP_STATUS_CODES.get(self.status_code, 'Unknown error'), 'msg': self.msg}
        if self.data:
            data['data'] = self.data
        return data

    def json(self):
        response = jsonify(self._to_dict())
        response.status_code = self.status_code
        return response
