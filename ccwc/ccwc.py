import sys, getopt, os

def main(argv):
    output = ""
    try:
        opts, args = getopt.getopt(argv,"hc:l:w:m:")
    except getopt.GetoptError:
        print ('Usage: ccwc.py (-hclwm) <filename>')
        sys.exit(2)
    if len(opts) == 0:
        try: 
            output += " " + byteLength(args[0]) + " " + lineCount(args[0]) + " " + wordCount(args[0]) + " " + args[0]
            print(output)
        except IndexError as ex:
            print ('Usage: ccwc.py (-hclwm) <filename>')
    else:
        for opt, arg in opts:
            if opt == '-h' or opt == '-help':
                output = "ccwc -c <filename>"
            elif opt == '-c':
                output += " " + byteLength(arg)
            elif opt == '-l':
                output += " " + lineCount(arg)
            elif opt == '-w':
                output += " " + wordCount(arg)
            elif opt == '-m':
                output += " " + charCount(arg)
            
            else:
                output = 'Unknown option: ' + arg 
            output += " " + arg
            print(output)
    

def byteLength(in_file):
    return str(os.path.getsize(in_file))

def lineCount(in_file):
    lc = 0
    with open(in_file, 'r') as file:
        for lines in file: 
            lc += 1
    return(str(lc))

def wordCount(in_file):
    wc = 0
    with open(in_file, 'r') as file:
        for lines in file: 
            wc += len(lines.split())
    return str(wc)

def charCount(in_file):
    res = 0
    with open(in_file, newline='') as file:
        data = file.read()
    return str(len(data.encode('utf-8')))

if __name__ == "__main__":
   main(sys.argv[1:])