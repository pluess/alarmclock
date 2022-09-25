try:
    import gc
except ImportError:
    gc = None

import logging
from logutil import get_logger


def chunker(seq: list, size: int):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))  # type: ignore


class Font:

    def __init__(self, bitMapList : list, width : int, height : int, mapper) -> None:
        """
        Args:
            bitMapList (list): List of bytes making up the bit map.
            width (int): Number of bits per line of a letter.
            height (int): Number of lines of a letter
            mapper : Callable[[dict], dict]: A function that creates a dict with mappings
                    for the characters like 'A', 'B' or 'heart', 'colon'
        """
        self.width = width
        self.height = height
        self.logger = get_logger(__name__)
        self.numericCharacterList = self.readFont(bitMapList)
        self.symbolicCharacterDict = mapper(self.numericCharacterList)

    def __getitem__(self, key) -> list:
        if isinstance(key, int):
            return self.numericCharacterList.get(key)  # type: ignore
        else:
            return self.symbolicCharacterDict.get(key)  # type: ignore

    def toCharField(self, byte: int) -> str:
        binaryString = self.toBinaryString(byte)
        binaryString = binaryString.replace('0', '..')
        binaryString = binaryString.replace('1', 'XX')
        return binaryString

    def toBinaryString(self, byte: int) -> str:
        binaryString = bin(byte)
        binaryString = binaryString[2:]
        l = len(binaryString)
        for i in range(l, self.width):
            binaryString = '0' + binaryString
        return binaryString

    def readFont(self, bitMapList : list) -> dict:
        characterList = {}
        counter = 0
        for character in chunker(bitMapList, self.height):
            characterList[counter] = character  # type: ignore
            counter += 1
            if self.logger.isEnabledFor(logging.DEBUG):
                if gc is not None: gc.collect()
                self.logger.debug(str(counter) + ': '+ str(character))  # type: ignore
                for byte in character:
                    charString = self.toCharField(byte)
                    self.logger.debug(charString)
        if gc is not None: gc.collect()
        return characterList