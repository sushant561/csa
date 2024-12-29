#  Buld a bash machine
# >Register
      # name  width  initial_value read-only
      # PC    12    0                 Not tick
      # AR    12    ,,                ,,
      # IR    16
      # AC    16
      # DR    16
      # E     1
      # S     1
      # I     1

# >ConditionBit
      # Name  register  bit   halt 
      # CARRY-BIT E      0     Not tick
      # HALT-BIT  S      0     TICKED 

# >microinstruction
#TransferRtoR
      # name         source    srcStartBit    dest    destStatBit  numBit
      # AR<-PC         PC           0           AR        0            12
      # AR<-IR(4-15)   IR           4           AR        0            12

# MemoryAccess
      # name         direction  memory   data    address
      # IR<-MAIN[AR]   read       MAIN    IR       AR
      # MAIN[AR]<-AC   write       MAIN    AC       AR
      # DR<-MAIN[AR]   read       MAIN    DR       AR

# RAM
      # name    length    cellsize
      # MAIN     4096        16

# increment
      # name    register   overflowBit     carryBit     data 
      # INCR-PC    PC       (none)            (none)      1
      # INCR-AC    AC          ,,               ,,        1

# DECODE 
      # name        ir 
      # DECODE-IR   IR

# NOW  > Fetch sequence
      #   AR<-PC
      #   IR<-MAIN[AR]
      #   INCR-PC
      #   AR<-IR(4-15)
      #   DECODE-IR


# NOW make field
      # name      Type        NumBits    DefaultVal     Relatively     Signed
      # REGISTER   required    16              0            absolute     untick
      # ADDR           ,,       12             ,,               ,,        ,,
      # OP                      4

# +++++++++++++++++++++ add operation ++++++++++++++++++++++++++++++++
# code:
      # START: INP
      # STA NUM  -> OP,ADDR  (MAIN[AR]<-AC, END)
      # INP   -> REG (INPUT, END)
      # ADD SUM  -> OP,ADD  (DR<-MAIN[AR], AC<- AC+DR, END)
      # OUT -> REG (OUTPUT, END)
      # HLT  -> REG (HALT, END)
      # NUM: .data 1 0

# >io
      # name    type    buffer    direction
      # OUTPUT  integer   AC         output
      # INPUT  integer   AC         input 

# >setConditionBit
      # name     bit      value 
      # HALT     HALT-BIT   1

# >Arithmetic  
      # name    type   source1   sourse2   destionation    carryBit   overflow 
      # AC<-AC+DR   ADD   AC         DR        AC               (none)    CARRY-BIT 


# -------------------------- Subtraction operation -----------------------------
# import all form add operation 

# code:
      # START: INP
      # STA NUM  -> OP,ADDR  (MAIN[AR]<-AC, END)
      # INP   -> REG (INPUT, END)
# >     # CMA   -> REG (AC<-AC',  END)
# >     # INC   -> REG (INCR-AC,  END)
      # ADD SUM  -> OP,ADD  (DR<-MAIN[AR], AC<- AC+DR, END)
      # OUT -> REG (OUTPUT, END)
      # HLT  -> REG (HALT, END)
      # NUM: .data 1 0

# >logical
      # name          type        source1          source2             destination
      # AC<-AC'         NOT         AC                 AC              AC