# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from squad/robot_position_msg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class robot_position_msg(genpy.Message):
  _md5sum = "28ee68e7cd1a8a51c576061a459afeaa"
  _type = "squad/robot_position_msg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 x
int32 y
int32 frontx
int32 fronty
float32 angle
"""
  __slots__ = ['x','y','frontx','fronty','angle']
  _slot_types = ['int32','int32','int32','int32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x,y,frontx,fronty,angle

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(robot_position_msg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x is None:
        self.x = 0
      if self.y is None:
        self.y = 0
      if self.frontx is None:
        self.frontx = 0
      if self.fronty is None:
        self.fronty = 0
      if self.angle is None:
        self.angle = 0.
    else:
      self.x = 0
      self.y = 0
      self.frontx = 0
      self.fronty = 0
      self.angle = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4if().pack(_x.x, _x.y, _x.frontx, _x.fronty, _x.angle))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 20
      (_x.x, _x.y, _x.frontx, _x.fronty, _x.angle,) = _get_struct_4if().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4if().pack(_x.x, _x.y, _x.frontx, _x.fronty, _x.angle))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 20
      (_x.x, _x.y, _x.frontx, _x.fronty, _x.angle,) = _get_struct_4if().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4if = None
def _get_struct_4if():
    global _struct_4if
    if _struct_4if is None:
        _struct_4if = struct.Struct("<4if")
    return _struct_4if
