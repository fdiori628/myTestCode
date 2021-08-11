from string import Template


class TemplateHandle:

    def __init__(self, value, target_value):
        self._Value = value
        self._targetvalue = target_value

    def mytemp(self):
        t = Template(self._Value)
        result = t.substitute(self._targetvalue)
        return result


apiname = 'api1'

T = TemplateHandle('')