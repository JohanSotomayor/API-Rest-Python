from flask import jsonify

class ErrorHandler:
    @staticmethod
    def not_found_error(error):
        response = jsonify({
                'error': 'Not found',
                'status':400
                })
        return response

    @staticmethod
    def unhandled_exception(error):
        response = jsonify({
                'error': str(error),
                'status':500
                })
        response.status_code = 500
        return response
    



