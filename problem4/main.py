def ubah_huruf(sentence : str):
	result = ""

	for i in range (0, len(sentence), 1):
		if ord(sentence[i]) != 32 :
			a = ord(sentence[i]) + 10
			if a > 90 :
				a = (a-65)%26 + 65
				result = result + chr(a)
			else:
				result = result + chr(a)
		else:
			result = result + chr(ord(sentence[i]))

	return result

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB