"""
Story explorer, actual editing is done here

Storyfile is a dictionary of lists with keys of the chapter names
E.X. storyfile['chapter_1'] = [filename, exit_behavior]

Storyfile['settings'] is a special entry with global settings for the story
Chapterfiles use these global settings unless otherwise specified 

A chapterfile should return a tuple, with the first value being the name of the next chapter to load, the second being any variables to pass out of the chapter.
E.X. ('chapter_3', [dog_alive=False, health=87, found_monster=True])
"""

def launch(storyfile):
	print("")

if __name__ == '__main__':
	print("ERROR: You should be launching this program from the story designer instead.")
	quit()