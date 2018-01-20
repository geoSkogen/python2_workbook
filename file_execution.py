from sys import argv

script, input_file = argv

def print_all(f):
    print (f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print (line_count, f.readline())

file_obj = open(input_file)
print("printing . . .")
print_all(file_obj)
print("rewinding . . .")
rewind(file_obj)

this_line = 1
print_a_line(this_line, file_obj)
this_line = 2
print_a_line(this_line, file_obj)
this_line = 3
print_a_line(this_line, file_obj)
this_line = 4
print_a_line(this_line, file_obj)
