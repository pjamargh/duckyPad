SHIFT = 0x100
ALT_GR = 0x200


keymap_azerty_fr = [
  0x00,             # NUL
  0x00,             # SOH
  0x00,             # STX
  0x00,             # ETX
  0x00,             # EOT
  0x00,             # ENQ
  0x00,             # ACK  
  0x00,             # BEL
  0x2a,     # BS Backspace
  0x2b,     # TAB  Tab
  0x28,     # LF Enter
  0x00,             # VT 
  0x00,             # FF 
  0x00,             # CR 
  0x00,             # SO 
  0x00,             # SI 
  0x00,             # DEL
  0x00,             # DC1
  0x00,             # DC2
  0x00,             # DC3
  0x00,             # DC4
  0x00,             # NAK
  0x00,             # SYN
  0x00,             # ETB
  0x00,             # CAN
  0x00,             # EM 
  0x00,             # SUB
  0x00,             # ESC
  0x00,             # FS 
  0x00,             # GS 
  0x00,             # RS 
  0x00,             # US 

  0x2c,      #  ' '
  0x38,    # !
  0x20,    # "
  0x20|ALT_GR,    # #
  0x30,    # $
  0x34|SHIFT,    # %
  0x1e,    # &
  0x21,          # '
  0x22,    # (
  0x2d,    # )
  0x32,    # *
  0x2e|SHIFT,    # +
  0x10,          # ,
  0x23,          # -
  0x36|SHIFT,          # .
  0x37|SHIFT,          # /
  0x27|SHIFT,          # 0
  0x1e|SHIFT,          # 1
  0x1f|SHIFT,          # 2
  0x20|SHIFT,          # 3
  0x21|SHIFT,          # 4
  0x22|SHIFT,          # 5
  0x23|SHIFT,          # 6
  0x24|SHIFT,          # 7
  0x25|SHIFT,          # 8
  0x26|SHIFT,          # 9
  0x37,      # :
  0x36,          # ;
  0x64,      # <
  0x2e,          # =
  0x64|SHIFT,      # >
  0x10|SHIFT,      # ?
  0x27|ALT_GR,      # @
  0x14|SHIFT,      # A
  0x05|SHIFT,      # B
  0x06|SHIFT,      # C
  0x07|SHIFT,      # D
  0x08|SHIFT,      # E
  0x09|SHIFT,      # F
  0x0a|SHIFT,      # G
  0x0b|SHIFT,      # H
  0x0c|SHIFT,      # I
  0x0d|SHIFT,      # J
  0x0e|SHIFT,      # K
  0x0f|SHIFT,      # L
  0x33|SHIFT,      # M
  0x11|SHIFT,      # N
  0x12|SHIFT,      # O
  0x13|SHIFT,      # P
  0x04|SHIFT,      # Q
  0x15|SHIFT,      # R
  0x16|SHIFT,      # S
  0x17|SHIFT,      # T
  0x18|SHIFT,      # U
  0x19|SHIFT,      # V
  0x1d|SHIFT,      # W
  0x1b|SHIFT,      # X
  0x1c|SHIFT,      # Y
  0x1a|SHIFT,      # Z
  0x22|ALT_GR,          # [
  0x25|ALT_GR,          # bslash
  0x2d|ALT_GR,          # ]
  0x26|ALT_GR,    # ^
  0x25,    # _
  0x24|ALT_GR,          # `
  0x14,      # a
  0x05,      # b
  0x06,      # c
  0x07,      # d
  0x08,      # e
  0x09,      # f
  0x0a,      # g
  0x0b,      # h
  0x0c,      # i
  0x0d,      # j
  0x0e,      # k
  0x0f,      # l
  0x33,      # m
  0x11,      # n
  0x12,      # o
  0x13,      # p
  0x04,      # q
  0x15,      # r
  0x16,      # s
  0x17,      # t
  0x18,      # u
  0x19,      # v
  0x1d,      # w
  0x1b,      # x
  0x1c,      # y
  0x1a,      # z
  0x21|ALT_GR,    # {
  0x23|ALT_GR,    # |
  0x2e|ALT_GR,    # }
  0x1f|ALT_GR,    # ~
  0       # DEL
]

keymap_dovark = [
  0x00,             # NUL
  0x00,             # SOH
  0x00,             # STX
  0x00,             # ETX
  0x00,             # EOT
  0x00,             # ENQ
  0x00,             # ACK  
  0x00,             # BEL
  0x2a,     # BS Backspace
  0x2b,     # TAB  Tab
  0x28,     # LF Enter
  0x00,             # VT 
  0x00,             # FF 
  0x00,             # CR 
  0x00,             # SO 
  0x00,             # SI 
  0x00,             # DEL
  0x00,             # DC1
  0x00,             # DC2
  0x00,             # DC3
  0x00,             # DC4
  0x00,             # NAK
  0x00,             # SYN
  0x00,             # ETB
  0x00,             # CAN
  0x00,             # EM 
  0x00,             # SUB
  0x00,             # ESC
  0x00,             # FS 
  0x00,             # GS 
  0x00,             # RS 
  0x00,             # US 

  0x2c,      #  ' '
  0x1e|SHIFT,    # !
  0x14|SHIFT,    # "
  0x20|SHIFT,    # #
  0x21|SHIFT,    # $
  0x22|SHIFT,    # %
  0x24|SHIFT,    # &
  0x14,          # '
  0x26|SHIFT,    # (
  0x27|SHIFT,    # )
  0x25|SHIFT,    # *
  0x30|SHIFT,    # +
  0x1a,          # ,
  0x34,          # -
  0x08,          # .
  0x2f,          # /
  0x27,          # 0
  0x1e,          # 1
  0x1f,          # 2
  0x20,          # 3
  0x21,          # 4
  0x22,          # 5
  0x23,          # 6
  0x24,          # 7
  0x25,          # 8
  0x26,          # 9
  0x1d|SHIFT,      # :
  0x1d,          # ;
  0x1a|SHIFT,      # <
  0x30,          # =
  0x08|SHIFT,      # >
  0x2f|SHIFT,      # ?
  0x1f|SHIFT,      # @
  0x04|SHIFT,      # A
  0x11|SHIFT,      # B
  0x0c|SHIFT,      # C
  0x0b|SHIFT,      # D
  0x07|SHIFT,      # E
  0x1c|SHIFT,      # F
  0x18|SHIFT,      # G
  0x0d|SHIFT,      # H
  0x0a|SHIFT,      # I
  0x06|SHIFT,      # J
  0x19|SHIFT,      # K
  0x13|SHIFT,      # L
  0x10|SHIFT,      # M
  0x0f|SHIFT,      # N
  0x16|SHIFT,      # O
  0x15|SHIFT,      # P
  0x1b|SHIFT,      # Q
  0x12|SHIFT,      # R
  0x33|SHIFT,      # S
  0x0e|SHIFT,      # T
  0x09|SHIFT,      # U
  0x37|SHIFT,      # V
  0x36|SHIFT,      # W
  0x05|SHIFT,      # X
  0x17|SHIFT,      # Y
  0x38|SHIFT,      # Z
  0x2d,          # [
  0x31,          # bslash
  0x2e,          # ]
  0x23|SHIFT,    # ^
  0x34|SHIFT,    # _
  0x35,          # `
  0x04,      # a
  0x11,      # b
  0x0c,      # c
  0x0b,      # d
  0x07,      # e
  0x1c,      # f
  0x18,      # g
  0x0d,      # h
  0x0a,      # i
  0x06,      # j
  0x19,      # k
  0x13,      # l
  0x10,      # m
  0x0f,      # n
  0x16,      # o
  0x15,      # p
  0x1b,      # q
  0x12,      # r
  0x33,      # s
  0x0e,      # t
  0x09,      # u
  0x37,      # v
  0x36,      # w
  0x05,      # x
  0x17,      # y
  0x38,      # z
  0x2d|SHIFT,    # {
  0x31|SHIFT,    # |
  0x2e|SHIFT,    # }
  0x35|SHIFT,    # ~
  0       # DEL
]

keymap_azerty_be = [
  0x00,             # NUL
  0x00,             # SOH
  0x00,             # STX
  0x00,             # ETX
  0x00,             # EOT
  0x00,             # ENQ
  0x00,             # ACK  
  0x00,             # BEL
  0x2a,     # BS Backspace
  0x2b,     # TAB  Tab
  0x28,     # LF Enter
  0x00,             # VT 
  0x00,             # FF 
  0x00,             # CR 
  0x00,             # SO 
  0x00,             # SI 
  0x00,             # DEL
  0x00,             # DC1
  0x00,             # DC2
  0x00,             # DC3
  0x00,             # DC4
  0x00,             # NAK
  0x00,             # SYN
  0x00,             # ETB
  0x00,             # CAN
  0x00,             # EM 
  0x00,             # SUB
  0x00,             # ESC
  0x00,             # FS 
  0x00,             # GS 
  0x00,             # RS 
  0x00,             # US 

  0x2c,      #  ' '
  0x25,    # !
  0x20,    # "
  0x20|ALT_GR,    # #
  0x30,    # $
  0x34|SHIFT,    # %
  0x1e,    # &
  0x21,          # '
  0x22,    # (
  0x2d,    # )
  0x30|SHIFT,    # *
  0x38|SHIFT,    # +
  0x10,          # ,
  0x2e,          # -
  0x36|SHIFT,          # .
  0x37|SHIFT,          # /
  0x27|SHIFT,          # 0
  0x1e|SHIFT,          # 1
  0x1f|SHIFT,          # 2
  0x20|SHIFT,          # 3
  0x21|SHIFT,          # 4
  0x22|SHIFT,          # 5
  0x23|SHIFT,          # 6
  0x24|SHIFT,          # 7
  0x25|SHIFT,          # 8
  0x26|SHIFT,          # 9
  0x37,      # :
  0x36,          # ;
  0x64,      # <
  0x38,          # =
  0x64|SHIFT,      # >
  0x10|SHIFT,      # ?
  0x1f|ALT_GR,      # @
  0x14|SHIFT,      # A
  0x05|SHIFT,      # B
  0x06|SHIFT,      # C
  0x07|SHIFT,      # D
  0x08|SHIFT,      # E
  0x09|SHIFT,      # F
  0x0a|SHIFT,      # G
  0x0b|SHIFT,      # H
  0x0c|SHIFT,      # I
  0x0d|SHIFT,      # J
  0x0e|SHIFT,      # K
  0x0f|SHIFT,      # L
  0x33|SHIFT,      # M
  0x11|SHIFT,      # N
  0x12|SHIFT,      # O
  0x13|SHIFT,      # P
  0x04|SHIFT,      # Q
  0x15|SHIFT,      # R
  0x16|SHIFT,      # S
  0x17|SHIFT,      # T
  0x18|SHIFT,      # U
  0x19|SHIFT,      # V
  0x1d|SHIFT,      # W
  0x1b|SHIFT,      # X
  0x1c|SHIFT,      # Y
  0x1a|SHIFT,      # Z
  0x2f|ALT_GR,          # [
  0x64|ALT_GR,          # bslash
  0x30|ALT_GR,          # ]
  0x23|ALT_GR,    # ^
  0x2e|SHIFT,    # _
  0x32|ALT_GR,          # `
  0x14,      # a
  0x05,      # b
  0x06,      # c
  0x07,      # d
  0x08,      # e
  0x09,      # f
  0x0a,      # g
  0x0b,      # h
  0x0c,      # i
  0x0d,      # j
  0x0e,      # k
  0x0f,      # l
  0x33,      # m
  0x11,      # n
  0x12,      # o
  0x13,      # p
  0x04,      # q
  0x15,      # r
  0x16,      # s
  0x17,      # t
  0x18,      # u
  0x19,      # v
  0x1d,      # w
  0x1b,      # x
  0x1c,      # y
  0x1a,      # z
  0x26|ALT_GR,    # {
  0x1e|ALT_GR,    # |
  0x27|ALT_GR,    # }
  0x38|ALT_GR,    # ~
  0       # DEL
]


for index, item in enumerate(keymap_dovark):
  padding = 4
  count = f"{index:#0{padding}x}"
  padding = 6
  value = f"{item:#0{padding}x}"
  comment = ''
  if chr(index).isprintable():
    comment = "// " + chr(index)
  print(count, value, comment)

for index in range(128, 256):
  item = 0
  padding = 4
  count = f"{index:#0{padding}x}"
  padding = 6
  value = f"{item:#0{padding}x}"
  comment = ''
  if chr(index).isprintable():
    comment = "// " + chr(index)
  print(count, value, comment)


# for x in range(128,256):
#   comment = ''
#   if chr(x).isprintable():
#     comment = "// " + chr(x)
#   print("0x00," + comment)