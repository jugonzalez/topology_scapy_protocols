class Proto1(Packet):
    name = 'Protocol 1'
    fields_desc = [ShortField('field1', 1),
                   XByteField('field2', 2)]

class Proto2(Packet):
    name = 'Protocol 2'
    fields_desc = [ShortField('field1_p2', 1),
                   XByteField('field2_p2', 2)]
