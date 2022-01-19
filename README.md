# network-acl-tools

*This project is currently in the planning stage and the content of this file describes my ideas, none of which have actually been implemented yet!*

**netacltools** is Python module for processing network access lists from various vendors.

* Parse network access lists from various vendors into a normalised format. 
* The initial focus will be on Cisco IOS, IOS-XE and IOS-XR platforms as this is my immediate need. Other platforms may be added later.
* The actual parsing is done through the [NTC Templates](https://github.com/networktocode/ntc-templates) and [jc](https://github.com/kellyjonbrazil/jc) packages.
* The output of the parser is a nested structure of Python classes that represent the individual components of access lists, e.g. ``protocol``, ``source``, 
  ``destination``, etc.
* The Python classes are based on existing classes as appropriate for the contained information. For example, ``source`` and ``destination`` are 
  based on the [netaddr](https://pypi.org/project/netaddr/) library.
* Access lists traversal can be simulated through test a ``Packet``.

Below is an example of what it may look like.

```python
>>> import netacltools
```

The parser is modelled after the ``ntc_templates.parse.parse_output()`` function.

```python
>>> parsed = netacltools.parse(platform="cisco_ios", 
...                            command="show ip access-lists", 
...                            data=open("show-ip-access-lists.txt", "rt").read())
```

Only a subset of commands are supported.

| Platform  | Command                    | Notes                                    |
|-----------|----------------------------|------------------------------------------|
| cisco_ios | show ip access-lists       | Not implemented                          |

The parser returns a dictionary with the names of the access lists serving as keys.

```python
>>> type(parsed)
<class 'dict'>

>>> parsed.keys()
dict_keys(['99', 'main-acl'])

>>> type(parsed['99'])
netacltools.CiscoIosStandardAccessList

>>> parsed['99'].name
'99'

>>> parsed['99'].type
'standard'

>>> parsed['99'].platform
'cisco_ios'

>>> parsed['99'].default_action
'deny'
```

Each access list contains a list of entries and each entry has attributes for at least ``.action``, ``.proto``, ``.src``, ``.dst``, ``.sport``, ``.dport``.
Additional attributes are platform specific.

```python
>>> parsed['main-acl'].entries
[netacltools.CiscoIosStandardEntry, netacltools.CiscoIosStandardEntry, ...]

>>> entry = parsed['main-acl'].entries[0]

>>> entry
'10 permit tcp any host 192.168.1.2 eq www'

>>> entry.action
'permit'

>>> entry.proto
'tcp'
>>> int(entry.proto)
6

>>> entry.dst
netaddr.IPAddress('192.168.1.2')

>>> entry.dport
'http'

>>> int(entry.dport)
80

>>> str(entry.dport)
'http'

>>> entry.sport
any   

>>> entry.src
any
```

The ``Packet`` class can be used to simulate access list traversal. 

```python
>>> packet = netacltools.Packet(dst='192.168.1.2', dport=80)
>>> packet
netacltools.Packet(proto=tcp, src=any, sport=any, dst=192.168.1.2, dport=80)

>>> main_acl = parsed['main-acl']
>>> main_acl.match_first(packet)
'10 permit tcp any host 192.168.1.2 eq www'

>>> type(main_acl.match_first(packet))
netacltools.CiscoIosStandardEntry

>>> main_acl.match_all(packet)
['10 permit tcp any host 192.168.1.2 eq www'
 '90 deny tcp any any any']
 
>>> main_acl.match_action(packet)
'permit'
```


19-Jan-2022
