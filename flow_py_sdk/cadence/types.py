from __future__ import annotations

from distutils.util import strtobool
from typing import (
    List,
    Optional as pyOptional,
    Tuple,
    Type as pyType,
)

import flow_py_sdk.cadence.constants as c
from flow_py_sdk.cadence.address import Address
from flow_py_sdk.cadence.decode import decode, add_cadence_decoder
from flow_py_sdk.cadence.location import decode_location, Location
from flow_py_sdk.cadence.value import Value


class Void(Value):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self):
        return f"Void"

    def encode_value(self) -> dict:
        return {}

    @classmethod
    def decode(cls, value) -> "Value":
        return Void()

    @classmethod
    def type_str(cls) -> str:
        return c.voidTypeStr


class Optional(Value):
    def __init__(self, value: pyOptional[Value]) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return f"Optional[{str(self.value)}]"

    def encode_value(self) -> dict:
        return {c.valueKey: self.value.encode() if self.value is not None else None}

    @classmethod
    def decode(cls, value) -> "Value":
        if c.valueKey not in value or value[c.valueKey] is None:
            return Optional(None)
        return Optional(decode(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.optionalTypeStr


class Bool(Value):
    def __init__(self, value: bool) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: self.value}

    @classmethod
    def decode(cls, value) -> "Value":
        if isinstance(value[c.valueKey], bool):
            return Bool(value[c.valueKey])
        return Bool(bool(strtobool(value[c.valueKey])))

    @classmethod
    def type_str(cls) -> str:
        return c.boolTypeStr


class String(Value):
    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return self.value

    def encode_value(self) -> dict:
        return {c.valueKey: self.value}

    @classmethod
    def decode(cls, value) -> "Value":
        return String(str(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.stringTypeStr


class Int(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.intTypeStr


class Int8(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.int8TypeStr


class Int16(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.int16TypeStr


class Int32(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.int32TypeStr


class Int64(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.int64TypeStr


class Int128(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.int128TypeStr


class Int256(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.int256TypeStr


class UInt(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.uintTypeStr


class UInt8(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.uint8TypeStr


class UInt16(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.uint16TypeStr


class UInt32(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.uint32TypeStr


class UInt64(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.uint64TypeStr


class UInt128(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.uint128TypeStr


class UInt256(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        return {c.valueKey: str(self.value)}

    @classmethod
    def decode(cls, value) -> "Value":
        return Int(int(value[c.valueKey]))

    @classmethod
    def type_str(cls) -> str:
        return c.uint256TypeStr


class Word8(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def decode(cls, value) -> "Value":
        raise NotImplementedError()

    @classmethod
    def type_str(cls) -> str:
        return c.word8TypeStr


class Word16(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def decode(cls, value) -> "Value":
        raise NotImplementedError()

    @classmethod
    def type_str(cls) -> str:
        return c.word16TypeStr


class Word32(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def decode(cls, value) -> "Value":
        raise NotImplementedError()

    @classmethod
    def type_str(cls) -> str:
        return c.word32TypeStr


class Word64(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def encode_value(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def decode(cls, value) -> "Value":
        raise NotImplementedError()

    @classmethod
    def type_str(cls) -> str:
        return c.word64TypeStr


class Fix64(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value: int = value

    def __str__(self):
        integer = int(self.value / c.fix64_factor)
        fraction = int(abs(self.value) % c.fix64_factor)
        return f"{integer}.{fraction:08d}"

    def encode_value(self) -> dict:
        return {c.valueKey: str(self)}

    @classmethod
    def decode(cls, value) -> "Value":
        str_values = str(value[c.valueKey]).split(".")
        sign: int = -1 if int(str_values[0]) < 0 else 1
        return Fix64(
            sign * (abs(int(str_values[0])) * c.fix64_factor + int(str_values[1]))
        )

    @classmethod
    def type_str(cls) -> str:
        return c.fix64TypeStr


class UFix64(Value):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value: int = value

    def __str__(self):
        integer = int(self.value / c.fix64_factor)
        fraction = int(self.value % c.fix64_factor)
        return f"{integer}.{fraction:08d}"

    def encode_value(self) -> dict:
        return {c.valueKey: str(self)}

    @classmethod
    def decode(cls, value) -> "Value":
        str_values = str(value[c.valueKey]).split(".")
        return Fix64(int(str_values[0]) * c.fix64_factor + int(str_values[1]))

    @classmethod
    def type_str(cls) -> str:
        return c.ufix64TypeStr


class Array(Value):
    def __init__(self, value: List[Value]) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return f'[{",".join([str(item) for item in self.value])}]'

    def encode_value(self) -> dict:
        return {c.valueKey: [i.encode() for i in self.value]}

    @classmethod
    def decode(cls, value) -> "Value":
        obj = value[c.valueKey]
        return Array([decode(i) for i in obj])

    @classmethod
    def type_str(cls) -> str:
        return c.arrayTypeStr


class KeyValuePair(object):
    def __init__(self, key: Value, value: Value) -> None:
        self.key = key
        self.value = value


class Dictionary(Value):
    def __init__(self, value: List[KeyValuePair] = None) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        return (
            f'{{{",".join([f"{{{item.key}:{item.value}}}" for item in self.value])}}}'
        )

    def encode_value(self) -> dict:
        return {
            c.valueKey: [
                {
                    c.keyKey: i.key.encode(),
                    c.valueKey: i.value.encode(),
                }
                for i in self.value
            ]
            if self.value is not None
            else None
        }

    @classmethod
    def decode(cls, value) -> "Value":
        obj = value[c.valueKey]
        items = [
            KeyValuePair(decode(item[c.keyKey]), decode(item[c.valueKey]))
            for item in obj
        ]
        return Dictionary(items)

    @classmethod
    def type_str(cls) -> str:
        return c.dictionaryTypeStr


class Contract(Value):
    def __init__(self, value=None) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        raise NotImplementedError()

    def encode_value(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def decode(cls, value) -> "Value":
        raise NotImplementedError()

    @classmethod
    def type_str(cls) -> str:
        return c.contractTypeStr


class Link(Value):
    def __init__(self, value=None) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        raise NotImplementedError()

    def encode_value(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def decode(cls, value) -> "Value":
        raise NotImplementedError()

    @classmethod
    def type_str(cls) -> str:
        return c.linkTypeStr


class Path(Value):
    def __init__(self, value=None) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        raise NotImplementedError()

    def encode_value(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def decode(cls, value) -> "Value":
        raise NotImplementedError()

    @classmethod
    def type_str(cls) -> str:
        return c.pathTypeStr


class TypeValue(Value):
    def __init__(self, value=None) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        raise NotImplementedError()

    def encode_value(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def decode(cls, value) -> "Value":
        raise NotImplementedError()

    @classmethod
    def type_str(cls) -> str:
        return c.typeTypeStr


class Capability(Value):
    def __init__(self, value=None) -> None:
        super().__init__()
        self.value = value

    def __str__(self):
        raise NotImplementedError()

    def encode_value(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def decode(cls, value) -> "Value":
        raise NotImplementedError()

    @classmethod
    def type_str(cls) -> str:
        return c.capabilityTypeStr


cadence_types: list[pyType[Value]] = [
    Void,
    Optional,
    Bool,
    String,
    Address,
    Int,
    Int8,
    Int16,
    Int32,
    Int64,
    Int128,
    Int256,
    UInt,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    UInt128,
    UInt256,
    Word8,
    Word16,
    Word32,
    Word64,
    Fix64,
    UFix64,
    Array,
    Dictionary,
    Contract,
    Link,
    Path,
    Capability,
]

for t in cadence_types:
    add_cadence_decoder(t)
