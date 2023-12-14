import re
import os

def convert(dir):
    csvpaths = []
    for root, subdirs, files in os.walk(dir):
        if len(files) == 0:
            continue
        else:
            for file in files:
                if os.path.splitext(file)[1] == '.txt':
                    csvpaths.append(tocsv(os.path.join(root, file)))
                

    return csvpaths

def tocsv(path):
    print(f"Reading file {path}")
    # Read the contents of the text file
    with open(path, 'r') as file:
        content = file.read()

    # Define the pattern using regular expression
    pattern = r'\[.*?\]'

    # Split the content based on the pattern
    sections = re.split(pattern, content)

    # get sectiong with the data
    data = sections[12]

    # new path with csv extesnsion and _ instaed of / 
    csvpath = path[:-3]+"csv"
    csvpath = csvpath.replace("/", "_").strip()
    csvpath = "./"+csvpath[1:]
 
    # Write to CSV
    print(f"Reading file {csvpath}")
    with open(csvpath, 'w') as file:
        # check if there is a semicolon in the data to fix it first
        if ';' in data:
            file.write(data.replace(",", ".").replace(";", ","))
        else:
            file.write(data.replace("\t", ","))
    

    return csvpath

def main(path):
    files = convert("./Irrigada") + convert("./Nao_irrigada")
    with open(path, 'w') as fpath:
        for file in files:
            fpath.write(file+"\n")

if __name__ == '__main__':
    main("arquivos.txt")