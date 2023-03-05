# This code is licensed under the MIT License, view the file "LICENSE" or go to...
# https://github.com/EliStillCantCode/VariableTypeFunctions/blob/master/LICENSE
# ...to see restrictions and permissions


def changetype(input, convert):
    try:
        convert(input)
    except:
        return "Input failed to convert."
    else:
        return convert(input)
  

def checktype(input, check):
    return type(input) is check

def findtype(input):
    conversions = {
        "<class 'str'>" : 'str',
        "<class 'int'>" : 'int',
        "<class 'float'>" : 'float',
        "<class 'complex'>" : 'complex',
        "<class 'list'>" : 'list',
        "<class 'tuple'>" : 'tuple',
        "<class 'range'>" : 'range',
        "<class 'dict'>" : 'dict',
        "<class 'set'>" : 'set',
        "<class 'frozenset'>" : 'frozenset',
        "<class 'bytes'>" : 'bytes',
        "<class 'bytearray'>" : 'bytearray',
        "<class 'memoryview'>" : 'memoryview',
        "<class 'bool'>" : 'bool',
        "<class 'None'>" : 'None',
    }
    return conversions[str(type(input))]

def checktypenot(input, check):
    return type(input) is not check