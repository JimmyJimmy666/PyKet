# 导入库
from .KClasses import *
import pathlib
import sys
import os

# 获取自身绝对路径
def getSelfAbspath() -> KString:
    return KString(pathlib.Path(sys.argv[0]).resolve())

# 获取自身上级目录绝对路径
def getSelfParentAbsPath(layers: int = 1) -> KString:
    path = pathlib.Path(sys.argv[0]).resolve()

    for layer in range(layers):
        path = path.parent.resolve()

    return KString(path)

# 获取路径上级目录绝对路径
def getParentAbsPath(path: str, layers: int = 1) -> KString:
    path = pathlib.Path(path).resolve()

    for layer in range(layers):
        path = path.parent.resolve()

    return KString(path)

# 获取传参
def getArgv(includePath: bool = False) -> KList:
    if includePath == False:
        return KList(sys.argv[1:])
    else:
        return KList(sys.argv)
    
# 合并路径
def joinPath(*paths) -> KString:
    return KString(os.path.join(*paths))

# 创建文件夹
def makeFolders(path: str) -> None:
    os.makedirs(path, exist_ok=True)
