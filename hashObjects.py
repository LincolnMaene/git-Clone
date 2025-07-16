import zlib
import hashlib

def readBlob(fileHash):
    fileLoc = f".git/objects/{fileHash[:2]}/{fileHash[2:]}"

    with open(fileLoc, "rb") as f:
        rawBytes = f.read()
        decompressedFile = zlib.decompress(rawBytes)
        filetype, fileData = decompressedFile.split(b" ", 1)

        if filetype != b"blob":
            raise ValueError("expected blob.")   
        
        fileSplit = fileData.split(b"\0")
        fileContent = fileSplit[1]
        print(fileContent.decode("utf-8"), end="")

def writeBlob(fileToHash):

    with open(fileToHash, "rb") as f:
        fileBin = f.read()
        zippedFile = f"blob {len(fileBin)}\x00".encode("utf-8")
        zippedFile += fileBin
        hash = hashlib.sha1(zippedFile).hexdigest()
        print(hash)