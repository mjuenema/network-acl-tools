

class CiscoAccessList(base.AccessList):
    def __init__(self, data):
        super().__init__(data)
        self.acl_name = data.get('acl_name')
        self.acl_type = data.get('acl_type')

class CiscoEntry(base.Entry):
    def __init__(self, data):
        super().__init__(data)
        self.acl_name = data.get('acl_name')
        self.acl_type = data.get('acl_type')
        self.action = data.get('action')
        try:
            self.line_num = int(data.get('line_num'))
        except TypeError:
            self.line_num = None