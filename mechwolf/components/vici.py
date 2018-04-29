# NOTE: When changing this file, be sure to update new_components.rst
# because it references specific line numbers here.
try:
    import serial
except ImportError:
    pass

from .valve import Valve

class ViciValve(Valve):
    '''Controls a VICI Valco Valve'''

    def __init__(self, name, mapping, serial_port=None):
        super().__init__(name=name, mapping=mapping)
        self.serial_port = serial_port

    def __enter__(self):
        # create the serial connection
        self.ser = serial.Serial(self.serial_port,
                                 115200,
                                 parity=serial.PARITY_NONE,
                                 stopbits=1,
                                 timeout=0.1,
                                 write_timeout=0.1)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # close the serial connection
        self.ser.close()
        return self

    def get_position(self):
        '''Returns the position of the valve.

        Note:
            This method was used for introspection and debugging.
            It is preserved but not currently used by any MechWolf function.

        Returns:
            int: The position of the valve.
        '''
        self.ser.write(b'CP\r')
        response = self.ser.readline()
        if response:
            position = int(response[2:4])  # Response is in the form 'CPXX\r'
            return position
        return False

    def config(self):
        return {"serial_port": (str, None)}

    def update(self):
        message = f'GO{self.setting}\r'
        self.ser.write(message.encode()) # send the message to the valve
        print(self.setting) # for introspection
