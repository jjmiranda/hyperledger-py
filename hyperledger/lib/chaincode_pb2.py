# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chaincode.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import chaincodeevent_pb2 as chaincodeevent__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chaincode.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x63haincode.proto\x12\x06protos\x1a\x14\x63haincodeevent.proto\x1a\x1fgoogle/protobuf/timestamp.proto\")\n\x0b\x43haincodeID\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1e\n\x0e\x43haincodeInput\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\x0c\"\xd6\x02\n\rChaincodeSpec\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.protos.ChaincodeSpec.Type\x12(\n\x0b\x63haincodeID\x18\x02 \x01(\x0b\x32\x13.protos.ChaincodeID\x12\'\n\x07\x63torMsg\x18\x03 \x01(\x0b\x32\x16.protos.ChaincodeInput\x12\x0f\n\x07timeout\x18\x04 \x01(\x05\x12\x15\n\rsecureContext\x18\x05 \x01(\t\x12:\n\x14\x63onfidentialityLevel\x18\x06 \x01(\x0e\x32\x1c.protos.ConfidentialityLevel\x12\x10\n\x08metadata\x18\x07 \x01(\x0c\x12\x12\n\nattributes\x18\x08 \x03(\t\">\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06GOLANG\x10\x01\x12\x08\n\x04NODE\x10\x02\x12\x07\n\x03\x43\x41R\x10\x03\x12\x08\n\x04JAVA\x10\x04\"\x86\x02\n\x17\x43haincodeDeploymentSpec\x12,\n\rchaincodeSpec\x18\x01 \x01(\x0b\x32\x15.protos.ChaincodeSpec\x12\x31\n\reffectiveDate\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x63odePackage\x18\x03 \x01(\x0c\x12\x45\n\x07\x65xecEnv\x18\x04 \x01(\x0e\x32\x34.protos.ChaincodeDeploymentSpec.ExecutionEnvironment\".\n\x14\x45xecutionEnvironment\x12\n\n\x06\x44OCKER\x10\x00\x12\n\n\x06SYSTEM\x10\x01\"`\n\x17\x43haincodeInvocationSpec\x12,\n\rchaincodeSpec\x18\x01 \x01(\x0b\x32\x15.protos.ChaincodeSpec\x12\x17\n\x0fidGenerationAlg\x18\x02 \x01(\t\"\xbf\x01\n\x18\x43haincodeSecurityContext\x12\x12\n\ncallerCert\x18\x01 \x01(\x0c\x12\x12\n\ncallerSign\x18\x02 \x01(\x0c\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x0f\n\x07\x62inding\x18\x04 \x01(\x0c\x12\x10\n\x08metadata\x18\x05 \x01(\x0c\x12\x16\n\x0eparentMetadata\x18\x06 \x01(\x0c\x12/\n\x0btxTimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xe1\x04\n\x10\x43haincodeMessage\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.protos.ChaincodeMessage.Type\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x0c\n\x04txid\x18\x04 \x01(\t\x12\x39\n\x0fsecurityContext\x18\x05 \x01(\x0b\x32 .protos.ChaincodeSecurityContext\x12.\n\x0e\x63haincodeEvent\x18\x06 \x01(\x0b\x32\x16.protos.ChaincodeEvent\"\xe6\x02\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\x0c\n\x08REGISTER\x10\x01\x12\x0e\n\nREGISTERED\x10\x02\x12\x08\n\x04INIT\x10\x03\x12\t\n\x05READY\x10\x04\x12\x0f\n\x0bTRANSACTION\x10\x05\x12\r\n\tCOMPLETED\x10\x06\x12\t\n\x05\x45RROR\x10\x07\x12\r\n\tGET_STATE\x10\x08\x12\r\n\tPUT_STATE\x10\t\x12\r\n\tDEL_STATE\x10\n\x12\x14\n\x10INVOKE_CHAINCODE\x10\x0b\x12\x10\n\x0cINVOKE_QUERY\x10\x0c\x12\x0c\n\x08RESPONSE\x10\r\x12\t\n\x05QUERY\x10\x0e\x12\x13\n\x0fQUERY_COMPLETED\x10\x0f\x12\x0f\n\x0bQUERY_ERROR\x10\x10\x12\x15\n\x11RANGE_QUERY_STATE\x10\x11\x12\x1a\n\x16RANGE_QUERY_STATE_NEXT\x10\x12\x12\x1b\n\x17RANGE_QUERY_STATE_CLOSE\x10\x13\x12\r\n\tKEEPALIVE\x10\x14\"*\n\x0cPutStateInfo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"3\n\x0fRangeQueryState\x12\x10\n\x08startKey\x18\x01 \x01(\t\x12\x0e\n\x06\x65ndKey\x18\x02 \x01(\t\"!\n\x13RangeQueryStateNext\x12\n\n\x02ID\x18\x01 \x01(\t\"\"\n\x14RangeQueryStateClose\x12\n\n\x02ID\x18\x01 \x01(\t\"5\n\x17RangeQueryStateKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"n\n\x17RangeQueryStateResponse\x12\x36\n\rkeysAndValues\x18\x01 \x03(\x0b\x32\x1f.protos.RangeQueryStateKeyValue\x12\x0f\n\x07hasMore\x18\x02 \x01(\x08\x12\n\n\x02ID\x18\x03 \x01(\t*4\n\x14\x43onfidentialityLevel\x12\n\n\x06PUBLIC\x10\x00\x12\x10\n\x0c\x43ONFIDENTIAL\x10\x01\x32X\n\x10\x43haincodeSupport\x12\x44\n\x08Register\x12\x18.protos.ChaincodeMessage\x1a\x18.protos.ChaincodeMessage\"\x00(\x01\x30\x01\x62\x06proto3')
  ,
  dependencies=[chaincodeevent__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CONFIDENTIALITYLEVEL = _descriptor.EnumDescriptor(
  name='ConfidentialityLevel',
  full_name='protos.ConfidentialityLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PUBLIC', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIDENTIAL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2006,
  serialized_end=2058,
)
_sym_db.RegisterEnumDescriptor(_CONFIDENTIALITYLEVEL)

ConfidentialityLevel = enum_type_wrapper.EnumTypeWrapper(_CONFIDENTIALITYLEVEL)
PUBLIC = 0
CONFIDENTIAL = 1


_CHAINCODESPEC_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='protos.ChaincodeSpec.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOLANG', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NODE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JAVA', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=438,
  serialized_end=500,
)
_sym_db.RegisterEnumDescriptor(_CHAINCODESPEC_TYPE)

_CHAINCODEDEPLOYMENTSPEC_EXECUTIONENVIRONMENT = _descriptor.EnumDescriptor(
  name='ExecutionEnvironment',
  full_name='protos.ChaincodeDeploymentSpec.ExecutionEnvironment',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOCKER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=719,
  serialized_end=765,
)
_sym_db.RegisterEnumDescriptor(_CHAINCODEDEPLOYMENTSPEC_EXECUTIONENVIRONMENT)

_CHAINCODEMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='protos.ChaincodeMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTERED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INIT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACTION', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_STATE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT_STATE', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEL_STATE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVOKE_CHAINCODE', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVOKE_QUERY', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_COMPLETED', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_ERROR', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANGE_QUERY_STATE', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANGE_QUERY_STATE_NEXT', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANGE_QUERY_STATE_CLOSE', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEEPALIVE', index=20, number=20,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1311,
  serialized_end=1669,
)
_sym_db.RegisterEnumDescriptor(_CHAINCODEMESSAGE_TYPE)


_CHAINCODEID = _descriptor.Descriptor(
  name='ChaincodeID',
  full_name='protos.ChaincodeID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='protos.ChaincodeID.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='protos.ChaincodeID.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=123,
)


_CHAINCODEINPUT = _descriptor.Descriptor(
  name='ChaincodeInput',
  full_name='protos.ChaincodeInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='args', full_name='protos.ChaincodeInput.args', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=155,
)


_CHAINCODESPEC = _descriptor.Descriptor(
  name='ChaincodeSpec',
  full_name='protos.ChaincodeSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.ChaincodeSpec.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chaincodeID', full_name='protos.ChaincodeSpec.chaincodeID', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ctorMsg', full_name='protos.ChaincodeSpec.ctorMsg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='protos.ChaincodeSpec.timeout', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secureContext', full_name='protos.ChaincodeSpec.secureContext', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidentialityLevel', full_name='protos.ChaincodeSpec.confidentialityLevel', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='protos.ChaincodeSpec.metadata', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='protos.ChaincodeSpec.attributes', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHAINCODESPEC_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=500,
)


_CHAINCODEDEPLOYMENTSPEC = _descriptor.Descriptor(
  name='ChaincodeDeploymentSpec',
  full_name='protos.ChaincodeDeploymentSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincodeSpec', full_name='protos.ChaincodeDeploymentSpec.chaincodeSpec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effectiveDate', full_name='protos.ChaincodeDeploymentSpec.effectiveDate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='codePackage', full_name='protos.ChaincodeDeploymentSpec.codePackage', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='execEnv', full_name='protos.ChaincodeDeploymentSpec.execEnv', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHAINCODEDEPLOYMENTSPEC_EXECUTIONENVIRONMENT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=765,
)


_CHAINCODEINVOCATIONSPEC = _descriptor.Descriptor(
  name='ChaincodeInvocationSpec',
  full_name='protos.ChaincodeInvocationSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincodeSpec', full_name='protos.ChaincodeInvocationSpec.chaincodeSpec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='idGenerationAlg', full_name='protos.ChaincodeInvocationSpec.idGenerationAlg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=767,
  serialized_end=863,
)


_CHAINCODESECURITYCONTEXT = _descriptor.Descriptor(
  name='ChaincodeSecurityContext',
  full_name='protos.ChaincodeSecurityContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='callerCert', full_name='protos.ChaincodeSecurityContext.callerCert', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='callerSign', full_name='protos.ChaincodeSecurityContext.callerSign', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protos.ChaincodeSecurityContext.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binding', full_name='protos.ChaincodeSecurityContext.binding', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='protos.ChaincodeSecurityContext.metadata', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parentMetadata', full_name='protos.ChaincodeSecurityContext.parentMetadata', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='txTimestamp', full_name='protos.ChaincodeSecurityContext.txTimestamp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=866,
  serialized_end=1057,
)


_CHAINCODEMESSAGE = _descriptor.Descriptor(
  name='ChaincodeMessage',
  full_name='protos.ChaincodeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.ChaincodeMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protos.ChaincodeMessage.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protos.ChaincodeMessage.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='txid', full_name='protos.ChaincodeMessage.txid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='securityContext', full_name='protos.ChaincodeMessage.securityContext', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chaincodeEvent', full_name='protos.ChaincodeMessage.chaincodeEvent', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHAINCODEMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1060,
  serialized_end=1669,
)


_PUTSTATEINFO = _descriptor.Descriptor(
  name='PutStateInfo',
  full_name='protos.PutStateInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protos.PutStateInfo.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.PutStateInfo.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1671,
  serialized_end=1713,
)


_RANGEQUERYSTATE = _descriptor.Descriptor(
  name='RangeQueryState',
  full_name='protos.RangeQueryState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startKey', full_name='protos.RangeQueryState.startKey', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endKey', full_name='protos.RangeQueryState.endKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1715,
  serialized_end=1766,
)


_RANGEQUERYSTATENEXT = _descriptor.Descriptor(
  name='RangeQueryStateNext',
  full_name='protos.RangeQueryStateNext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='protos.RangeQueryStateNext.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1768,
  serialized_end=1801,
)


_RANGEQUERYSTATECLOSE = _descriptor.Descriptor(
  name='RangeQueryStateClose',
  full_name='protos.RangeQueryStateClose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='protos.RangeQueryStateClose.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1803,
  serialized_end=1837,
)


_RANGEQUERYSTATEKEYVALUE = _descriptor.Descriptor(
  name='RangeQueryStateKeyValue',
  full_name='protos.RangeQueryStateKeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protos.RangeQueryStateKeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.RangeQueryStateKeyValue.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1839,
  serialized_end=1892,
)


_RANGEQUERYSTATERESPONSE = _descriptor.Descriptor(
  name='RangeQueryStateResponse',
  full_name='protos.RangeQueryStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keysAndValues', full_name='protos.RangeQueryStateResponse.keysAndValues', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasMore', full_name='protos.RangeQueryStateResponse.hasMore', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ID', full_name='protos.RangeQueryStateResponse.ID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1894,
  serialized_end=2004,
)

_CHAINCODESPEC.fields_by_name['type'].enum_type = _CHAINCODESPEC_TYPE
_CHAINCODESPEC.fields_by_name['chaincodeID'].message_type = _CHAINCODEID
_CHAINCODESPEC.fields_by_name['ctorMsg'].message_type = _CHAINCODEINPUT
_CHAINCODESPEC.fields_by_name['confidentialityLevel'].enum_type = _CONFIDENTIALITYLEVEL
_CHAINCODESPEC_TYPE.containing_type = _CHAINCODESPEC
_CHAINCODEDEPLOYMENTSPEC.fields_by_name['chaincodeSpec'].message_type = _CHAINCODESPEC
_CHAINCODEDEPLOYMENTSPEC.fields_by_name['effectiveDate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHAINCODEDEPLOYMENTSPEC.fields_by_name['execEnv'].enum_type = _CHAINCODEDEPLOYMENTSPEC_EXECUTIONENVIRONMENT
_CHAINCODEDEPLOYMENTSPEC_EXECUTIONENVIRONMENT.containing_type = _CHAINCODEDEPLOYMENTSPEC
_CHAINCODEINVOCATIONSPEC.fields_by_name['chaincodeSpec'].message_type = _CHAINCODESPEC
_CHAINCODESECURITYCONTEXT.fields_by_name['txTimestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHAINCODEMESSAGE.fields_by_name['type'].enum_type = _CHAINCODEMESSAGE_TYPE
_CHAINCODEMESSAGE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHAINCODEMESSAGE.fields_by_name['securityContext'].message_type = _CHAINCODESECURITYCONTEXT
_CHAINCODEMESSAGE.fields_by_name['chaincodeEvent'].message_type = chaincodeevent__pb2._CHAINCODEEVENT
_CHAINCODEMESSAGE_TYPE.containing_type = _CHAINCODEMESSAGE
_RANGEQUERYSTATERESPONSE.fields_by_name['keysAndValues'].message_type = _RANGEQUERYSTATEKEYVALUE
DESCRIPTOR.message_types_by_name['ChaincodeID'] = _CHAINCODEID
DESCRIPTOR.message_types_by_name['ChaincodeInput'] = _CHAINCODEINPUT
DESCRIPTOR.message_types_by_name['ChaincodeSpec'] = _CHAINCODESPEC
DESCRIPTOR.message_types_by_name['ChaincodeDeploymentSpec'] = _CHAINCODEDEPLOYMENTSPEC
DESCRIPTOR.message_types_by_name['ChaincodeInvocationSpec'] = _CHAINCODEINVOCATIONSPEC
DESCRIPTOR.message_types_by_name['ChaincodeSecurityContext'] = _CHAINCODESECURITYCONTEXT
DESCRIPTOR.message_types_by_name['ChaincodeMessage'] = _CHAINCODEMESSAGE
DESCRIPTOR.message_types_by_name['PutStateInfo'] = _PUTSTATEINFO
DESCRIPTOR.message_types_by_name['RangeQueryState'] = _RANGEQUERYSTATE
DESCRIPTOR.message_types_by_name['RangeQueryStateNext'] = _RANGEQUERYSTATENEXT
DESCRIPTOR.message_types_by_name['RangeQueryStateClose'] = _RANGEQUERYSTATECLOSE
DESCRIPTOR.message_types_by_name['RangeQueryStateKeyValue'] = _RANGEQUERYSTATEKEYVALUE
DESCRIPTOR.message_types_by_name['RangeQueryStateResponse'] = _RANGEQUERYSTATERESPONSE
DESCRIPTOR.enum_types_by_name['ConfidentialityLevel'] = _CONFIDENTIALITYLEVEL

ChaincodeID = _reflection.GeneratedProtocolMessageType('ChaincodeID', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEID,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeID)
  ))
_sym_db.RegisterMessage(ChaincodeID)

ChaincodeInput = _reflection.GeneratedProtocolMessageType('ChaincodeInput', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEINPUT,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeInput)
  ))
_sym_db.RegisterMessage(ChaincodeInput)

ChaincodeSpec = _reflection.GeneratedProtocolMessageType('ChaincodeSpec', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODESPEC,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeSpec)
  ))
_sym_db.RegisterMessage(ChaincodeSpec)

ChaincodeDeploymentSpec = _reflection.GeneratedProtocolMessageType('ChaincodeDeploymentSpec', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEDEPLOYMENTSPEC,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeDeploymentSpec)
  ))
_sym_db.RegisterMessage(ChaincodeDeploymentSpec)

ChaincodeInvocationSpec = _reflection.GeneratedProtocolMessageType('ChaincodeInvocationSpec', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEINVOCATIONSPEC,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeInvocationSpec)
  ))
_sym_db.RegisterMessage(ChaincodeInvocationSpec)

ChaincodeSecurityContext = _reflection.GeneratedProtocolMessageType('ChaincodeSecurityContext', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODESECURITYCONTEXT,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeSecurityContext)
  ))
_sym_db.RegisterMessage(ChaincodeSecurityContext)

ChaincodeMessage = _reflection.GeneratedProtocolMessageType('ChaincodeMessage', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEMESSAGE,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeMessage)
  ))
_sym_db.RegisterMessage(ChaincodeMessage)

PutStateInfo = _reflection.GeneratedProtocolMessageType('PutStateInfo', (_message.Message,), dict(
  DESCRIPTOR = _PUTSTATEINFO,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.PutStateInfo)
  ))
_sym_db.RegisterMessage(PutStateInfo)

RangeQueryState = _reflection.GeneratedProtocolMessageType('RangeQueryState', (_message.Message,), dict(
  DESCRIPTOR = _RANGEQUERYSTATE,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.RangeQueryState)
  ))
_sym_db.RegisterMessage(RangeQueryState)

RangeQueryStateNext = _reflection.GeneratedProtocolMessageType('RangeQueryStateNext', (_message.Message,), dict(
  DESCRIPTOR = _RANGEQUERYSTATENEXT,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.RangeQueryStateNext)
  ))
_sym_db.RegisterMessage(RangeQueryStateNext)

RangeQueryStateClose = _reflection.GeneratedProtocolMessageType('RangeQueryStateClose', (_message.Message,), dict(
  DESCRIPTOR = _RANGEQUERYSTATECLOSE,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.RangeQueryStateClose)
  ))
_sym_db.RegisterMessage(RangeQueryStateClose)

RangeQueryStateKeyValue = _reflection.GeneratedProtocolMessageType('RangeQueryStateKeyValue', (_message.Message,), dict(
  DESCRIPTOR = _RANGEQUERYSTATEKEYVALUE,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.RangeQueryStateKeyValue)
  ))
_sym_db.RegisterMessage(RangeQueryStateKeyValue)

RangeQueryStateResponse = _reflection.GeneratedProtocolMessageType('RangeQueryStateResponse', (_message.Message,), dict(
  DESCRIPTOR = _RANGEQUERYSTATERESPONSE,
  __module__ = 'chaincode_pb2'
  # @@protoc_insertion_point(class_scope:protos.RangeQueryStateResponse)
  ))
_sym_db.RegisterMessage(RangeQueryStateResponse)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class ChaincodeSupportStub(object):
  """Interface that provides support to chaincode execution. ChaincodeContext
  provides the context necessary for the server to respond appropriately.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Register = channel.stream_stream(
        '/protos.ChaincodeSupport/Register',
        request_serializer=ChaincodeMessage.SerializeToString,
        response_deserializer=ChaincodeMessage.FromString,
        )


class ChaincodeSupportServicer(object):
  """Interface that provides support to chaincode execution. ChaincodeContext
  provides the context necessary for the server to respond appropriately.
  """

  def Register(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChaincodeSupportServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Register': grpc.stream_stream_rpc_method_handler(
          servicer.Register,
          request_deserializer=ChaincodeMessage.FromString,
          response_serializer=ChaincodeMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protos.ChaincodeSupport', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaChaincodeSupportServicer(object):
  """Interface that provides support to chaincode execution. ChaincodeContext
  provides the context necessary for the server to respond appropriately.
  """
  def Register(self, request_iterator, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaChaincodeSupportStub(object):
  """Interface that provides support to chaincode execution. ChaincodeContext
  provides the context necessary for the server to respond appropriately.
  """
  def Register(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_ChaincodeSupport_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('protos.ChaincodeSupport', 'Register'): ChaincodeMessage.FromString,
  }
  response_serializers = {
    ('protos.ChaincodeSupport', 'Register'): ChaincodeMessage.SerializeToString,
  }
  method_implementations = {
    ('protos.ChaincodeSupport', 'Register'): face_utilities.stream_stream_inline(servicer.Register),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_ChaincodeSupport_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('protos.ChaincodeSupport', 'Register'): ChaincodeMessage.SerializeToString,
  }
  response_deserializers = {
    ('protos.ChaincodeSupport', 'Register'): ChaincodeMessage.FromString,
  }
  cardinalities = {
    'Register': cardinality.Cardinality.STREAM_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'protos.ChaincodeSupport', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
