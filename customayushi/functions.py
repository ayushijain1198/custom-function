import logging

from iotfunctions import ui
from iotfunctions.base import BaseTransformer

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install

PACKAGE_URL = 'git@github.com:ayushijain1198/custom-function.git'


class Resistance(BaseTransformer):
    '''
    The docstring of the function will show as the function description in the UI.
    '''

    def __init__(self, voltage, current, resistance):
        # a function is expected to have at least one parameter that acts
        # as an input argument, e.g. "name" is an argument that represents the
        # name to be used in the greeting. It is an "input" as it is something
        # that the function needs to execute.

        # a function is expected to have at lease one parameter that describes
        # the output data items produced by the function, e.g. "greeting_col"
        # is the argument that asks what data item name should be used to
        # deliver the functions outputs

        # always create an instance variable with the same name as your arguments

        self.voltage = voltage
        self.current = current
        self.resistance = resistance
        super().__init__()

        # do not place any business logic in the __init__ method
        # All business logic goes into the execute() method or methods called by the
        # execute() method

    def execute(self, df):
        # the execute() method accepts a dataframe as input and returns a dataframe as output
        # the output dataframe is expected to produce at least one new output column

        df[self.resistance] = self.voltage / self.current

        # If the function has no new output data, output a status_flag instead
        # e.g. df[<self.output_col_arg>> = True

        return df

    @classmethod
    def build_ui(cls):
        # Your function will UI built automatically for configuring it
        # This method describes the contents of the dialog that will be built
        # Account for each argument - specifying it as a ui object in the "inputs" or "outputs" list

        inputs = [ui.UISingle(name='voltage', datatype=float, description='Voltage'),
                  ui.UISingle(name='current', datatype=float, description='Current')]
        outputs = [
            ui.UIFunctionOutSingle(name='resistance', datatype=float, description='Resistance')]
        return inputs, outputs
