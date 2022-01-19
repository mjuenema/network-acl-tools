
import socket
import netaddr

MIN_PORT = 1
MAX_PORT = 65535

ANY_ADDRESS = netaddr.IPNetwork('0.0.0.0/0')
ANY_PORT = range(MIN_PORT, MAX_PORT+1)



class Address:
    """IP Address, Network or Address Range.

       :param aspec: Address specification in one of the following formats.
            'any'                   - Any address
            <ipaddress>             - A single IP Address.
            'host' <ipaddress>      - A single IP Address.
            <network>/<netmask>     - A network specification.
            <network>/<wildcard>    - A network specification.
            <ipaddress> <ipaddress> - A range of IP Addresses.

    """

    def __init__(self, aspec):
        assert isinstance(aspec, str)
        self.aspec = aspec

        a = spec.split()

        if len(a) == 1:
            if a[0].lower() == 'any':
                # 'any'
                self.value = ANY_ADDRESS
            elif '/' in a[0]:
                # <network>/<netmask> | <network>/<wildcard>
                self.value = netaddr.IPNetwork(a[0])
            else:
                # <ipaddress>
                self.value = netaddr.IPAddress(a[0])
        elif len(a) == 2:
            if a[0] == 'host':
                # 'host' <ipaddress>
                self.value = netaddr.IPAddress(a[1])
            else:
                # <ipaddress> <ipaddress>
                self.value = netaddr.IPRange(a[0], a[1])
        else:
            raise ValueError(f"address={address}, mask={mask}, range={range}")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.aspec}"



class MacAddress:
    raise NotImplementedError


class Port:
    """TCP/UDP Port

       :param pspec: Port specification in one of the following formats.
            'any'       - Any port.
            <int>       - Port number which can possibly be converted by ``socket.getservbyport()``.
            <name>      - Port name which can be converted by ``socket.getservbyname()``.
            <cmp> <int> - Comparator ('gt', 'ge', 'eq', 'le', 'lt') and port number.
            <int> <int> - Range of port numbers.

    """

    def __init__(self, pspec):
        assert isinstance(pspec, str)
        self.pspec = pspec

        p = pspec.split()

        if len(p) == 1:
            try:
                self.value = int(p)
            except ValueError:
                if p.lower() == 'any'
                    self.value = ANY_PORT
                else:
                    self.value = socket.getservbyname(p)
        elif len(p) == 2:
            try:
                self.value = range(int(p[0]), int(p[1])+1)
            except ValueError:
                if p[0] == 'gt':
                    self.value = range(int(p[1])+1, MAX_PORT+1)
                elif p[0] == 'ge':
                    self.value = range(int(p[1]), MAX_PORT+1)
                elif p[0] == 'eq':
                    self.value = int(p[1])
                elif p[0] == 'le':
                    self.value = range(MIN_PORT, int(p[1]))
                elif p[0] == 'lt':
                    self.value = range(MIN_PORT, int(p[1])-1)
                else:
                    raise ValueError(str(portspec))        
        else:
            raise ValueError(str(portspec))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.pspec}"

    def is_match(self, port):
        """Test whether `port` matches this `Port`.

           :param port: Either a string that can be resolved through ``socket.getservbyname()``,
                an integer, or a Python ``range`` type.

        """

        if isinstance(port, str):
            port = socket.getservbyname()

        if isinstance(port, int) and isinstance(self.value, int):
            return port == self.value
        elif isinstance(port, int) and isinstance(self.value, range):
            return port in self.value
        elif isinstance(port, range) and isinstance(self.value, int):
            return min(port) == self.value and max(port) == self.value
        elif isinstance(port, range) and isinstance(self.value, range):
            return min(port) >= min(self.value) and max(port) <= max(self.value)
        else:
            raise ValueError(port)    
        

Src = Dst = Address
SPort = DPort = Port
MacSrc = MacDst = MacAddress


class Base:
    platform = None
    command = None
    acl_name = None
    acl_type = None
    def __init__(self, data):
        self._data = data


class AccessList(Base):
    def __init__(self, data):
        Base.__init__(data)


class Entry(Base):
    action = None
    src = Src('any')
    dst = Dst('any')
    sport = SPort('any')
    dport = DPort('any')

    def __init__(self, data):
        Base.__init__(data)



