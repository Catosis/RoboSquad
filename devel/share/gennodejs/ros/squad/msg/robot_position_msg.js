// Auto-generated. Do not edit!

// (in-package squad.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class robot_position_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.frontx = null;
      this.fronty = null;
      this.angle = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0;
      }
      if (initObj.hasOwnProperty('frontx')) {
        this.frontx = initObj.frontx
      }
      else {
        this.frontx = 0;
      }
      if (initObj.hasOwnProperty('fronty')) {
        this.fronty = initObj.fronty
      }
      else {
        this.fronty = 0;
      }
      if (initObj.hasOwnProperty('angle')) {
        this.angle = initObj.angle
      }
      else {
        this.angle = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type robot_position_msg
    // Serialize message field [x]
    bufferOffset = _serializer.int32(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.int32(obj.y, buffer, bufferOffset);
    // Serialize message field [frontx]
    bufferOffset = _serializer.int32(obj.frontx, buffer, bufferOffset);
    // Serialize message field [fronty]
    bufferOffset = _serializer.int32(obj.fronty, buffer, bufferOffset);
    // Serialize message field [angle]
    bufferOffset = _serializer.float32(obj.angle, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type robot_position_msg
    let len;
    let data = new robot_position_msg(null);
    // Deserialize message field [x]
    data.x = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [frontx]
    data.frontx = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [fronty]
    data.fronty = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [angle]
    data.angle = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'squad/robot_position_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '28ee68e7cd1a8a51c576061a459afeaa';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 x
    int32 y
    int32 frontx
    int32 fronty
    float32 angle
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new robot_position_msg(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0
    }

    if (msg.frontx !== undefined) {
      resolved.frontx = msg.frontx;
    }
    else {
      resolved.frontx = 0
    }

    if (msg.fronty !== undefined) {
      resolved.fronty = msg.fronty;
    }
    else {
      resolved.fronty = 0
    }

    if (msg.angle !== undefined) {
      resolved.angle = msg.angle;
    }
    else {
      resolved.angle = 0.0
    }

    return resolved;
    }
};

module.exports = robot_position_msg;
