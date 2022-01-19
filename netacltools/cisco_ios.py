
import .base
import .cisco

   
class CiscoIosAccessList(cisco.CiscoAccessList):
    def __init__(self, data):
        super().__init__(data)


class CiscoIosEntry(cisco.CiscoEntry):
    """
    
       :param data: Dictionary with the following keys and example values.
        - acl_type: "Standard"
        - acl_name: "99"
        - line_num: "10"
        - action: "permit"
        - src_any: "any"
        - src_host: "172.16.191.199"
        - src_network: "10.0.10.0"
        - src_wildcard: "0.0.0.255"
        - log: "log"
        - matches: "20"

    """

    def __init__(self, data):
        super().__init__(data)

        # self.src
        if data.get('src_any'):
            self.src = base.Src('any')
        elif data.get('src_host'):
            self.src = base.Src(data['src_host'])
        elif data.get('src_network') and data.get('src_wildcard'):
            self.src = base.Src(f"{data['src_host']}/{data['src_wildcard']}")
        else:
            raise ValueError(data)

        # self.dst


class CiscoIosStandardAccessList(CiscoIosAccessList):
    def __init__(self, data):
        super().__init__(data)


class CiscoIosExtendedAccessList(CiscoIosAccessList):
    def __init__(self, data):
        super().__init__(data)


class CiscoIosStandardEntry(CiscoIosEntry):
    """
    


    """

    def __init__(self, data):
        super().__init__(data)


    

class CiscoIosExtendedEntry(CiscoIosEntry):
    def __init__(self, data):
        super().__init__(data)


def cisco_ios_show_ip_access_lists(data)
    """Return the right class for the output of the Cisco IOS command "show ip access-lists".

    :param data: Dictionary with the following superset of keys and example values.
        - acl_type: "Standard"
        - acl_name: "99"
        - line_num: ""
        - action: ""
        - protocol: ""
        - src_host: ""
        - src_any: ""
        - src_network: ""
        - src_wildcard: ""
        - src_port_match: ""
        - src_port: ""
        - src_port_range_start: ""
        - src_port_range_end: ""
        - dst_host: ""
        - dst_any: ""
        - dst_network: ""
        - dst_wildcard: ""
        - dst_port_match: ""
        - dst_port: ""
        - dst_port_range_start: ""
        - dst_port_range_end: ""
        - flags_match: ""
        - tcp_flag: ""
        - log: ""
        - log_tag: ""
        - icmp_type: ""
        - time: ""
        - state: ""
        - matches: ""

    """

    if data.get('acl_type') == 'Standard' and data.get('line_num') is None:
        return CiscoIosStandardAccessList(data)
    elif data.get('acl_type') == 'Extended' and data.get('line_num') is None:
        return CiscoIosExtendedAccessList(data)
    elif data.get('acl_type') == 'Standard' and data.get('line_num') is not None:
        return CiscoIosStandardEntry(data)
    elif data.get('acl_type') == 'Extended' and data.get('line_num') is not None:
        return CiscoIosExtendedEntry(data)
    else:
        raise ValueError(data)
