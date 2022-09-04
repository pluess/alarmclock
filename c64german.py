from fontc64germanregular8 import fontC64GermanRegular8

"""
Provides a the C64 bitmap font with german characters.

A-Z: 01-26
0-9: 48-57
colon(:): 58
heart: 83
A-Z inverse: 129-154
0-9 inverse: 176-185
colon(:) inverse: 186
heart inverse: 211
a-z: 257-282
a-z inverse: 385-410

Based on
https://github.com/robhagemans/hoard-of-bitfonts
https://github.com/robhagemans/monobit
"""
class C64German:

	def __init__(self):
		self.numericCharacterList = self.readFont(False)
		self.symbolicCharacterDict = self.mapCharacters(self.numericCharacterList)  # type: ignore
		self.numberOfBits = 8

	def __getitem__(self, key) -> list:
		if isinstance(key, int):
			return self.numericCharacterList.get(key)  # type: ignore
		else:
			return self.symbolicCharacterDict.get(key)  # type: ignore

	def mapCharacters(self, characterList: dict)-> dict:
		characterDict = {}
		pos = 1
		for i in range(ord('A'), ord('Z') + 1):  # type: ignore
			characterDict[chr(i)] = characterList[pos]  # type: ignore
			pos += 1
		pos = 257
		for i in range(ord('a'), ord('z') + 1):  # type: ignore
			characterDict[chr(i)] = characterList[pos]  # type: ignore
			pos += 1
		pos = 48
		for i in range(ord('0'), ord('9') + 1):  # type: ignore
			characterDict[chr(i)] = characterList[pos]  # type: ignore
			pos += 1
		characterDict['heart'] = characterList[83] # type: ignore
		characterDict['colon'] = characterList[58] # type: ignore
		return characterDict

	def chunker(self, seq: list, size: int):
		return (seq[pos:pos + size] for pos in range(0, len(seq), size))  # type: ignore

	def toCharField(self, byte: int) -> str:
		binaryString = self.toBinaryString(byte)
		binaryString = binaryString.replace('0', '..')
		binaryString = binaryString.replace('1', 'XX')
		return binaryString

	def toBinaryString(self, byte: int) -> str:
		binaryString = bin(byte)  # type: ignore
		binaryString = binaryString[2:]
		l = len(binaryString)
		for i in range(l, self.numberOfBits):  # type: ignore
			binaryString = '0' + binaryString
		return binaryString

	def readFont(self, output: bool) -> dict:
		characterList = {}
		counter = 0
		for character in self.chunker(fontC64GermanRegular8, 8):
			characterList[counter] = character  # type: ignore
			if output: print(str(counter) + ': '+ str(character))  # type: ignore
			counter += 1
			if output:
				for byte in character:
					charString = self.toCharField(byte)
					print(charString)
		return characterList

if __name__ == '__main__':  # type: ignore
	font = C64German()
	font.readFont(True)
