import argparse
import os  
import os.path

#Search string
search_string = "conda env"

#Search current directory
directory ='.'

parser = argparse.ArgumentParser(description='Search ipython notebooks.')
parser.add_argument('search_string', type=str, help='Our search term')
parser.add_argument('--dir', type=str, default='.')
args = parser.parse_args()

# print(f"this={args.dir}")

#set my variables here
search_string = args.search_string
directory = args.dir

print(f"Searching for {search_string} in {directory}")

search_string = search_string.lower()
links=[]

files = os.listdir(directory)
files.sort()
for fn in files:
    if 'ipynb' in fn:
        filename = f"{directory}/{fn}"
        if os.path.isfile(filename):
            found = False
            with open(filename,'r') as fp:
                for line in fp:
                    line = line.lower()
                    if search_string in line:
                        links.append(f"{filename}\n")
                        break
        else:
            print(f"File {filename} not found")
if links:
    print(' '.join(links))
else:
    print(f'string {search_string} not found in {directory}')
            