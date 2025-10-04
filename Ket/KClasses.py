# String
class KString(str):
    def __init__(self, string: str):
        super().__init__()
        self = string

    # 查找int
    def integer(self):
        integer = ""
        for intr in self:
            if intr.isdigit():
                integer += intr
        return int(integer) if integer else 0
    
    # 转换二进制
    def binary(self, prefix: bool = False):
        byteData = self.encode('utf-8')
        binaryList = [bin(byte).zfill(8) for byte in byteData] if prefix else [bin(byte)[2:].zfill(8) for byte in byteData]
        return ' '.join(binaryList)

    # 转换八进制
    def octal(self, prefix: bool = False):
        byteData = self.encode('utf-8')
        octalList = [oct(byte).zfill(3) for byte in byteData] if prefix else [oct(byte)[2:].zfill(3) for byte in byteData]
        return ' '.join(octalList)

    # 转换十六进制
    def hexadecimal(self, prefix: bool = False):
        byteData = self.encode('utf-8')
        hexList = [hex(byte).upper().zfill(2) for byte in byteData] if prefix else [hex(byte)[2:].upper().zfill(2) for byte in byteData]
        return ''.join(hexList)
    
# List
class KList(list):
    def __init__(self, lst: list):
        super().__init__(lst)

    # 查找int项
    def intgerItems(self):
        integerItems = []
        for item in self:
            if isinstance(item, int):
                integerItems.append(item)
        return integerItems

    # 加入项
    def addItem(self, item):
        self.append(item)
        return self

    # 加入多个项
    def addItems(self, items: list):
        for item in items:
            self.append(item)
        return self

# FileTypes
class FileTypes():
    UTF8 = KString("UTF-8")
    CSV = KString("CSV")
    JSON = KString("JSON")
    XML = KString("XML")
    TOML = KString("TOML")

# PrinteTypes()
class PrinteTypes():
    COMMON = KString("COMMON")
    COLOURFUL = KString("COLOURFUL")
