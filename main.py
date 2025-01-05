def main(filepath):
	book_report("./books/frankenstein.txt")
	
def count_words(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		words = file_contents.split()

	return len(words)

def count_char_app(filepath):
	char_dict = {}

	with open(filepath) as f:
		file_contents = f.read()
		lowered_content = file_contents.lower()
		for char in lowered_content:
			if char not in char_dict and char.isalpha():
				char_dict[char] = 1
			elif char in char_dict:
				char_dict[char] += 1
	
	return char_dict

def book_report(filepath):
	print(f"--- Begin report of {filepath} ---")
	print(f"{count_words(filepath)} words found in the document")
	print("\n")

	char_app = count_char_app(filepath)
	for char, app in sorted(char_app.items(), reverse=True, key=lambda x: x[1]):
		print(f"The '{char}' character was found {app} times")

	print("--- End report ---")


main("./books/frankenstein.txt")