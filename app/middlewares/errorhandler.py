from flask import jsonify

class ErrorHandler:
    @staticmethod
    def not_found_error(error):
        response = jsonify({
                'message': 'Not found',
                'status':404
                })
        return response

    @staticmethod
    def unhandled_exception(error):
        response = jsonify({
                'message': str(error),
                'status':500
                })
        response.status_code = 500
        return response
    



