
class Extractor():
	"""This class is used to extract information from the string or documents or webpages"""
	def __init__(self):
		pass

	def phoneNumberExtractor(self,data):
		"""
		This function handled phone number extraction using various methods in the given data
		:param data : type: string
		:return set
		"""
		data = data.replace("\r", " ")
		data = data.replace("\r\n", " ")

		#first is identifying 10 digits code
		data = data.split()
		result = []
		for word in data:
			res = None
			res = word if word.isdecimal() and len(word) == 10 and not res else res
			res = word[2:] if word.isdecimal() and len(word) == 12 and not res else res
			res = word[3:] if word[3:].isdecimal() and len(word) == 10 and not res else res
			if ("(" and ")") in word or "-" in word:
				word = word.replace("(","")
				word = word.replace(")","")
				word = word.replace ("-","")
				res = word if(len(word) == 10) else None
			if res:
				result.append(res)
				del(res)
		return set(result)

if __name__ == "__main__":
	fr = open("webScrap.txt","r")
	ex = Extractor()
	phoneNumbers = ex.phoneNumberExtractor(data=fr.read())
	print(phoneNumbers)
