from connexion.problem import problem
from connexion.decorators import validation
from connexion.utils import is_null
from jsonschema import ValidationError


class ParameterValidator(validation.ParameterValidator):
    def validate_formdata_parameter(self, param, request):
        print("param", param)
        print("request", request)

        try:
            if param.get('type') == 'file':
                val = request.files.get(param['name'])
            else:
                val = request.form.get(param['name'])
            res = self.validate_parameter('formdata', val, param)
            print(res)
            return res
        except ValidationError as e:
            print(e)
            return problem(400, "Bad Request", str(e))


class RequestBodyValidator(validation.RequestBodyValidator):
    """
    This class overrides the default connexion RequestBodyValidator
    so that it returns the complete string representation of the
    error, rather than just returning the error message.

    For more information:
        - https://github.com/zalando/connexion/issues/558
        - https://connexion.readthedocs.io/en/latest/request.html
    """
    def validate_schema(self, data, url):
        if self.is_null_value_valid and is_null(data):
            return None

        try:
            print(data)
            self.validator.validate(data)
        except ValidationError as exception:
            print(
                "{url} validation error: {error}".format(url=url, error=exception)
            )
            return problem(400, "Bad Request", str(exception))

        return None


def attach_to(app):
    # Specifies configurations for ReST API endpoints
    # routes and callbacks see 'routes' package
    app.add_api('swagger.yml')
