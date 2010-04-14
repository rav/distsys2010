import struct

class Packer:

   def __init__(self, msgtype, message):
      msglen = len(message)
      
      self.msg = struct.pack('!HH'+str(msglen)+'s', msglen + 4, msgtype, message)
   
   def get(self):
      return self.msg
   
class Unpacker:
   def __init__(self, packed):
      msglen = len(packed)
      print "unpacking length = %d" % msglen
      self.msg = struct.unpack('!HH'+str(msglen - 4)+'s', packed)
   
   def get(self):
      return self.msg

