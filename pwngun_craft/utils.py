def describe_file_flags(flags):
    res = []
    for i in list_file_flags():
        mask = flags & i[1]
        to_append = mask
        if bin(mask).count('1') == 1:
            to_append = True
        elif bin(mask).count('1') == 0:
            to_append = False
        res.append((i[0], to_append))
    return res

def pdescribe_file_flags(flags):
    f = list_file_flags()
    mx = len(f[0][0])
    for i in f:
        mx = max(mx, len(i[0]))
    for i in describe_file_flags(flags):
        print(f"{i[0].ljust(mx)} {i[1] if i[1] in [False, True] else hex(i[1])}")
    print()

def list_file_flags():
    return [
        ('_IO_MAGIC',             0xFBAD0000),
        ('_IO_USER_BUF',          0x1       ),
        ('_IO_UNBUFFERED',        0x2       ),
        ('_IO_NO_READS',          0x4       ),
        ('_IO_NO_WRITES',         0x8       ),
        ('_IO_EOF_SEEN',          0x10      ),
        ('_IO_ERR_SEEN',          0x20      ),
        ('_IO_DELETE_DONT_CLOSE', 0x40      ),
        ('_IO_LINKED',            0x80      ),
        ('_IO_IN_BACKUP',         0x100     ),
        ('_IO_LINE_BUF',          0x200     ),
        ('_IO_TIED_PUT_GET',      0x400     ),
        ('_IO_CURRENTLY_PUTTING', 0x800     ),
        ('_IO_IS_APPENDING',      0x1000    ),
        ('_IO_IS_FILEBUF',        0x2000    ),
        ('_IO_BAD_SEEN',          0x4000    ),
        ('_IO_USER_LOCK',         0x8000    ),
    ]

def plist_file_flags():
    f = list_file_flags()
    mx = len(f[0][0])
    for i in f:
        mx = max(mx, len(i[0]))
    for i in f:
        print(f"{i[0].ljust(mx)} {i[1] if i[1] in [False, True] else hex(i[1])}")
    print()

def get_flag_mask(name):
    for i in list_file_flags():
        if i[0] == name:
            return i[1]
    raise ValueError('no such flag')
