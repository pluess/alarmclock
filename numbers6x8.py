from fontnumber6x8 import font_numbers6x8_Regular_8
from font import Font

def mapCharacters(characterList: dict)-> dict:
	return {
		'0': characterList[0],
		'1': characterList[1],
		'2': characterList[2],
		'3': characterList[3],
		'4': characterList[4],
		'5': characterList[5],
		'6': characterList[6],
		'7': characterList[7],
		'8': characterList[8],
		'9': characterList[9],
		'colon' : characterList[10]
	}
class Numbers6x8(Font):
	"""
	Font with numbers and a colon witha 6 by 8 bitmap
 
	Based on
	fonts/numbers8x6.draw
	https://github.com/pluess/monobit
	"""

	def __init__(self, output : bool = False):
		super(Numbers6x8, self).__init__(font_numbers6x8_Regular_8, 6, 8, mapCharacters, output) # type: ignore

if __name__ == '__main__':  # type: ignore
	font = Numbers6x8(True)
