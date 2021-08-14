import os
import sys
from datetime import date

# directory = os.system('pwd')
# todo_file = str(directory) + "/todo.txt"
# print(todo_file)
# print(sys.argv[0])
def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    a = open(file_name, "a")
    a.close()
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'a') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for lines in read_obj.readlines(): 
        	write_obj.write(lines)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

# print(len(sys.argv))
if (len(sys.argv) == 1 or sys.argv[1] == 'help'):
	print("Usage:-")
	print('$ ./todo add "todo item"  # Add a new todo') 
	print("$ ./todo ls               # Show remaining todos")
	print("$ ./todo del NUMBER       # Delete a todo") 
	print("$ ./todo done NUMBER      # Complete a todo") 
	print("$ ./todo help             # Show usage") 
	print("$ ./todo report           # Statistics")

elif sys.argv[1] == 'add':
	prepend_line("todo.txt", sys.argv[2])
	print('Added todo: "' + sys.argv[2] + '"')

elif sys.argv[1] == 'ls':
	with open("todo.txt", "r") as file:
		content = file.readlines()
		count = len(content)
	
	for line in content: 
		print("[{}] {}".format(count, line.strip()))
		count = count - 1

elif sys.argv[1] == 'del':
	with open("todo.txt", "r") as file:
		lines = file.readlines()
	if int(sys.argv[2]) > len(lines) or int(sys.argv[2]) < 1:
		print("Error: todo #" + sys.argv[2] + " does not exist. Nothing deleted.")
	else:
		del lines[len(lines)-int(sys.argv[2])]
		with open("todo.txt", "w+") as new_file:
			for line in lines:
				new_file.write(line)
		print("Deleted todo #" + sys.argv[2])

elif sys.argv[1] == 'done':
	with open("todo.txt", "r") as file: 
		lines = file.readlines()
		done = lines[len(lines)-int(sys.argv[2])]
	if int(sys.argv[2]) > len(lines) or int(sys.argv[2]) < 1:
			print("Error: todo #" + sys.argv[2] + " does not exist.")
	else:
		del lines[len(lines)-int(sys.argv[2])]
		with open("todo.txt", "w+") as new_file, open("done.txt", "a") as complete:
			complete.write(done)
			for line in lines:
				new_file.write(line)
		print("Marked todo #" + sys.argv[2] + " as done.")

elif sys.argv[1] == 'report':
	with open("todo.txt", "r") as file1, open("done.txt", "r") as file2:
		len1 = len(file1.readlines())
		len2 = len(file2.readlines())
	print(str(date.today()) + " Pending : " + str(len1) + " Completed : " + str(len2))
