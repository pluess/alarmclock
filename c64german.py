from fontc64germanregular8 import fontC64GermanRegular8
from font import Font

def mapCharacters(characterList: dict)-> dict:
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

class C64German(Font):
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
	https://github.com/robhagemans/hoard-of-bitfonts/blob/master/commodore/c64-german.draw
	https://github.com/pluess/monobit
	"""

	def __init__(self):
		super(C64German, self).__init__(fontC64GermanRegular8, 8, 8, mapCharacters)

if __name__ == '__main__':
	font = C64German()
