"""Shared Data"""


MAIN_FILE_TEMPLATE = """# Hello, this is main file of your visual novel!

# GENERAL SYNTAX

# Comments (rows, which would not be proceded) are marked with #(hashtag)
# This line will not be proceded
# If you are familiar with Python, it will be easier to understand syntax




# DEFENITIONS

# Where is located file that defines characters
# You can define as many files with characters definitions as you need
# All definitions should be in format: CHARACTERS[your label, without square brackets] = [path to file]
# Example:
CHARACTERS = {character_example}
# Next example is commented, so it's not be used
# CHARACTERS_EPILOGUE = D:/visual_novel/characters/epilogue.less




# REPLICAS (Check {characters_filename} first)

# Narrator thought
"~I saw cats without smiling, but a smile without a cat..."

# Narrator replica
"You didn't expect this?"

# Replica of character that was defined as john
john"Who asked for my help? John Doe is here!"




# CONDITONS, FLAGS




# Player choices




# BG, CG, EMBIENT, SOUNDS, VISUAL EFFECTS, AUDIO EFFECTS




# Extra options

"""

CHARACTERS_FILE_SAMPLE = """# Person from which story will be readed (Narrator)
# Syntax is [label] = Character([name, that will be displayed], [Color of name, hex])
narrator = Character('Jesus', '000000')

# Sample character
john = Character('John Doe', 'FF1AB2')
"""
