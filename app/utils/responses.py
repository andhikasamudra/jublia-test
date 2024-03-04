from flask import jsonify
from .constants import ErrorCode


def create_response(data=None, error_key=None):
    response = {
        'data': data,
        'message': error_key['message'] if error_key else 'Success',
        'code': error_key['code'] if error_key else 200
    }

    return jsonify(response), response['code']
