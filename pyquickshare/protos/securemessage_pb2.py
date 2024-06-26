# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: securemessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13securemessage.proto\x12\rsecuremessage\";\n\rSecureMessage\x12\x17\n\x0fheader_and_body\x18\x01 \x02(\x0c\x12\x11\n\tsignature\x18\x02 \x02(\x0c\"\xf1\x01\n\x06Header\x12\x32\n\x10signature_scheme\x18\x01 \x02(\x0e\x32\x18.securemessage.SigScheme\x12\x33\n\x11\x65ncryption_scheme\x18\x02 \x02(\x0e\x32\x18.securemessage.EncScheme\x12\x1b\n\x13verification_key_id\x18\x03 \x01(\x0c\x12\x19\n\x11\x64\x65\x63ryption_key_id\x18\x04 \x01(\x0c\x12\n\n\x02iv\x18\x05 \x01(\x0c\x12\x17\n\x0fpublic_metadata\x18\x06 \x01(\x0c\x12!\n\x16\x61ssociated_data_length\x18\x07 \x01(\r:\x01\x30\"D\n\rHeaderAndBody\x12%\n\x06header\x18\x01 \x02(\x0b\x32\x15.securemessage.Header\x12\x0c\n\x04\x62ody\x18\x02 \x02(\x0c\"5\n\x15HeaderAndBodyInternal\x12\x0e\n\x06header\x18\x01 \x02(\x0c\x12\x0c\n\x04\x62ody\x18\x02 \x02(\x0c\"\'\n\x0f\x45\x63P256PublicKey\x12\t\n\x01x\x18\x01 \x02(\x0c\x12\t\n\x01y\x18\x02 \x02(\x0c\"1\n\x12SimpleRsaPublicKey\x12\t\n\x01n\x18\x01 \x02(\x0c\x12\x10\n\x01\x65\x18\x02 \x01(\x05:\x05\x36\x35\x35\x33\x37\"\x18\n\x0b\x44hPublicKey\x12\t\n\x01y\x18\x01 \x02(\x0c\"\xf0\x01\n\x10GenericPublicKey\x12*\n\x04type\x18\x01 \x02(\x0e\x32\x1c.securemessage.PublicKeyType\x12:\n\x12\x65\x63_p256_public_key\x18\x02 \x01(\x0b\x32\x1e.securemessage.EcP256PublicKey\x12=\n\x12rsa2048_public_key\x18\x03 \x01(\x0b\x32!.securemessage.SimpleRsaPublicKey\x12\x35\n\x11\x64h2048_public_key\x18\x04 \x01(\x0b\x32\x1a.securemessage.DhPublicKey*G\n\tSigScheme\x12\x0f\n\x0bHMAC_SHA256\x10\x01\x12\x15\n\x11\x45\x43\x44SA_P256_SHA256\x10\x02\x12\x12\n\x0eRSA2048_SHA256\x10\x03*&\n\tEncScheme\x12\x08\n\x04NONE\x10\x01\x12\x0f\n\x0b\x41\x45S_256_CBC\x10\x02*:\n\rPublicKeyType\x12\x0b\n\x07\x45\x43_P256\x10\x01\x12\x0b\n\x07RSA2048\x10\x02\x12\x0f\n\x0b\x44H2048_MODP\x10\x03\x42N\n/com.google.security.cryptauth.lib.securemessageB\x12SecureMessageProtoH\x03\xa2\x02\x04SMSG')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'securemessage_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n/com.google.security.cryptauth.lib.securemessageB\022SecureMessageProtoH\003\242\002\004SMSG'
  _SIGSCHEME._serialized_start=829
  _SIGSCHEME._serialized_end=900
  _ENCSCHEME._serialized_start=902
  _ENCSCHEME._serialized_end=940
  _PUBLICKEYTYPE._serialized_start=942
  _PUBLICKEYTYPE._serialized_end=1000
  _SECUREMESSAGE._serialized_start=38
  _SECUREMESSAGE._serialized_end=97
  _HEADER._serialized_start=100
  _HEADER._serialized_end=341
  _HEADERANDBODY._serialized_start=343
  _HEADERANDBODY._serialized_end=411
  _HEADERANDBODYINTERNAL._serialized_start=413
  _HEADERANDBODYINTERNAL._serialized_end=466
  _ECP256PUBLICKEY._serialized_start=468
  _ECP256PUBLICKEY._serialized_end=507
  _SIMPLERSAPUBLICKEY._serialized_start=509
  _SIMPLERSAPUBLICKEY._serialized_end=558
  _DHPUBLICKEY._serialized_start=560
  _DHPUBLICKEY._serialized_end=584
  _GENERICPUBLICKEY._serialized_start=587
  _GENERICPUBLICKEY._serialized_end=827
# @@protoc_insertion_point(module_scope)
