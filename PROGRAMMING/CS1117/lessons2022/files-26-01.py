# r means to read the file
# w means to write the file
# a means to append or change the existing file
file_name = "whatever.txt"
textfile = open(file_name, "r") #(1) Must "open" before use

# (2) Read through the file from the beginning to the end

textfile.close() #(3) "close" when done

#f.readline() reads a single line as a string ; empty string signifies end of file read devours entire file and returns contents
# of as a single string readlines devours entire file and returns contents as list of lines (strings)

# Other way : Use a file iterator. Enters loop

"f.readline()" # readline reads a single line (as a string, including newline); empty string signifies end of file.

"f.read()" #read devours entire file and re-turns contents as single string

"f.readlines()" # readlines devours entire file and returns contents as list of lines (strings)

