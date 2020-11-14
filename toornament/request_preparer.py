from .functions_dictionary_helper import ParameterType
from .api_functions_doc import FUNCTIONS


def prepare_request(function_name, request_arguments, **parameter):
    required_parameters = FUNCTIONS[function_name]['parameters']

    parameters = [{}, {}, {}, {}]

    for parameter_name, parameter_value in parameter.items():
        parameter_attributes = required_parameters[parameter_name]

        if not parameter_attributes['optional'] or parameter_value is not None:

            if parameter_attributes['list']:
                new_parameter_value = [parameter_attributes['converter'](element) for element in parameter_value]
            else:
                new_parameter_value = parameter_attributes['converter'](parameter_value)

            if parameter_attributes['type'] == ParameterType.HEADER:
                parameters[ParameterType.HEADER][parameter_name.capitalize()] = '{}={}'.format(FUNCTIONS[function_name]['range'], new_parameter_value)
            else:
                parameters[parameter_attributes['type']][parameter_name] = new_parameter_value

    access_arguments = {
        'request_arguments': request_arguments,
        'method': FUNCTIONS[function_name]['method'],
        'path': FUNCTIONS[function_name]['path'],
        'headers': parameters[ParameterType.HEADER],
        'path_parameters': parameters[ParameterType.PATH],
        'query_parameters': parameters[ParameterType.QUERY]
    }

    if parameters[ParameterType.JSON]:
        access_arguments['json'] = parameters[ParameterType.JSON]

    return access_arguments
