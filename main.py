from pymodbus.client import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder



class User:
    def __init__(self, wo, bo, host, port):
        super(User, self).__init__()
        self.host = host
        self.port = port
        self.wo = wo
        self.bo = bo
        self.client = ModbusTcpClient(host, port)
        self.builder = BinaryPayloadBuilder(byteorder=bo,
                                            wordorder=wo)
        self.connecting()

    def wobo(value):
        match value:
            case "1234":
                wo = Endian.Big
                bo = Endian.Big
            case "3412":
                wo = Endian.Big
                bo = Endian.Little
            case "4321":
                wo = Endian.Little
                bo = Endian.Little
            case "2143":
                wo = Endian.Little
                bo = Endian.Big
        return [wo, bo]

    def connecting(self):
        try:
            self.client.connect()
        except:
            print("неудалось подключиться")

    def disconnect(self):
        self.client.close()

    def write_16int(self, peremennaya, address):
        self.builder.add_16bit_int(peremennaya)
        payload = self.builder.build()
        z = [payload[-1]]
        print(payload)
        self.client.write_registers(address, z, skip_encode=True, slave=1)

    def read_16int(self, address):
        result = self.client.read_holding_registers(address, 1, slave=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                     byteorder=self.bo,
                                                     wordorder=self.wo)

        decoded = ('16int', decoder.decode_16bit_int())
        return decoded[1]

    def write_64int(self, peremennaya, address):
        # завписывается в 1ые 4 поля
        self.builder.add_64bit_int(peremennaya)
        payload = self.builder.build()
        z = [payload[-4], payload[-3], payload[-2], payload[-1]]
        print(payload)
        self.client.write_registers(address, z, skip_encode=True, slave=1)

    def read_64int(self, address):
        result = self.client.read_holding_registers(address, 4, slave=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                     byteorder=self.bo,
                                                     wordorder=self.wo)

        decoded = ('64int', decoder.decode_64bit_int())
        return decoded[1]

    def write_float(self, peremennaya, address):
        self.builder.add_32bit_float(peremennaya)
        payload = self.builder.build()
        z = [payload[-2], payload[-1]]
        self.client.write_registers(address, z, skip_encode=True, slave=1)

    def read_float(self, address):
        result = self.client.read_holding_registers(address, 2, slave=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                     byteorder=self.bo,
                                                     wordorder=self.wo)
        decoded = ('32float', decoder.decode_32bit_float())
        return decoded[1]

    def read_dint(self, client, address):
        result = client.read_holding_registers(address, 2, slave=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                     byteorder=self.bo,
                                                     wordorder=self.wo)
        decoded = ('32dint', decoder.decode_32bit_uint())
        return decoded[1]

    def write_dint(self, peremennaya, address):
        self.builder.add_32bit_uint(peremennaya)
        payload = self.builder.build()
        z = [payload[-2], payload[-1]]
        self.client.write_registers(address, z, skip_encode=True, slave=1)

    def read_uint(self, address):
        result = self.client.read_holding_registers(address, 1, slave=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                     byteorder=self.bo,
                                                     wordorder=self.wo)

        decoded = ('16uint', decoder.decode_16bit_uint())
        return decoded[1]

    def write_uint(self, peremennaya, address):
        self.builder.add_16bit_uint(peremennaya)
        payload = self.builder.build()
        z = [payload[-1]]
        self.client.write_registers(address, z, skip_encode=True, slave=1)

    def read_64uint(self, address):
        result = self.client.read_holding_registers(address, 4, slave=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                     byteorder=self.bo,
                                                     wordorder=self.wo)

        decoded = ('64uint', decoder.decode_64bit_uint())
        print(decoded)
        return decoded[1]

    def write_64uint(self, peremennaya, address):
        self.builder.add_64bit_uint(peremennaya)
        payload = self.builder.build()
        z = [payload[-4], payload[-3], payload[-2], payload[-1]]
        self.client.write_registers(address, z, skip_encode=True, slave=1)

    def read_udint(self, address):
        result = self.client.read_holding_registers(address, 2, slave=1)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                     byteorder=self.bo,
                                                     wordorder=self.wo)

        decoded = ('32udint', decoder.decode_32bit_uint())
        return decoded[1]

    def write_udint(self, peremennaya, address):
        self.builder.add_32bit_uint(peremennaya)
        payload = self.builder.build()
        z = [payload[-2], payload[-1]]
        self.client.write_registers(address, z, skip_encode=True, slave=1)

    def read_double(self, address):
        result = self.client.read_holding_registers(address, 4, slave=1)

        decoder = BinaryPayloadDecoder.fromRegisters(result.registers,
                                                     byteorder=self.bo,
                                                     wordorder=self.wo)
        decoded = ('64float', decoder.decode_64bit_float())
        return decoded[1]

    def write_double(self, peremennaya, address):
        self.builder.add_64bit_float(peremennaya)
        payload = self.builder.build()
        z = [payload[-4], payload[-3], payload[-2], payload[-1]]
        self.client.write_registers(address, z, skip_encode=True, slave=1)

