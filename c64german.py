from fontc64germanregular8 import fontC64GermanRegular8

class C64German:

	def chunker(self, seq, size):
		return (seq[pos:pos + size] for pos in range(0, len(seq), size))  # type: ignore

	def toCharField(self, byte):
		binaryString = bin(byte)
		binaryString = binaryString[2:]
		l = len(binaryString)
		for i in range(l, 8):  # type: ignore
			binaryString = '0' + binaryString
		binaryString = binaryString.replace('0', '..')
		binaryString = binaryString.replace('1', 'XX')
		return binaryString

	def readFont(self):
		counter = 0
		for line in self.chunker(fontC64GermanRegular8, 8):
			counter += 1
			print(str(counter) + ': '+ str(line))  # type: ignore
			for byte in line:
				charString = self.toCharField(byte)
				print(charString)
    
	def __init__(self, *argv, **kwargs):
		pass

if __name__ == '__main__':  # type: ignore
	font = C64German()
	font.readFont()
