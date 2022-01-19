"""

"""

# TODO: logging

import collections

import ntc_templates.parse

import .base
import .cisco_ios
#import cisco_iosxr
#import cisco_iosxe

DISPATCHERS = {
    ('cisco_ios', 'show ip access-lists'): cisco_ios.cisco_ios_show_ip_access_lists,
}

def parse(platform, command, data):

    try:
        dispatcher = DISPATCHERS[(platform, command)]
    except KeyError:
        raise NotImplementedError(f"{platform}/{command} not supported")

    parsed = ntc_templates.parse.parse(platform=platform, command=command, data=data)

    acls = dict()
    acl = None

    for d in parsed:
        c = dispatcher(d)

        d.platform = platform
        d.command = command

        if isinstance(d, base.AccessList):
            acl = acls[d.name] = d
        elif isinstance(d, base.Entry):
            acl.entries.append(d)

    return acls

