"""
This is the manager program for helping a user to create and test a story
"""

import story_explorer

STORY_DEFAULT = ""
CHAPTER_DEFAULT = ""

def launch_story_explorer(storyfile_name):
	pass

def new_story():
	print("Creating a new story, initializing base files")
	with open("story.st", 'w') as f:
		f.write(STORY_DEFAULT)
		print('.', end='', sep='')
	with open("chapter_1.chap", 'w') as f:
		f.write(CHAPTER_DEFAULT)
		print('.', end='', sep='')
	with open("story.set", 'w') as f:
		f.write('')
		print('.', end='', sep='')
	print("Done creating story.")

def menu():
	print("1	Begin a new story")
	print("2	Work on an existing story")
	print("3	Test a story")
	print("4	Edit story preferences")
	print("0	Quit")

	selection = int(input("\n"))
	if selection == 0:
		print("Quitting, thank you.")
		quit()
	elif selection == 1:
		new_story()

def main():
	menu()

if __name__ == '__main__':
	main()