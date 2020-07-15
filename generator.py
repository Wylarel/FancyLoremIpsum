import random
import re

working_directory = "DasKapital"

input_text = open("data/" + working_directory + ".txt", "r").read().replace("\n", "").replace("#", "")

while "  " in input_text:
    input_text = input_text.replace("  ", " ")

sentences = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.?])\s").split(input_text)
random.shuffle(sentences)

f = open("output/" + working_directory + ".txt", "a")
for sentence in sentences:
    f.write(sentence.replace("- ", "") + " ")
f.close()
