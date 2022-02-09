import json
import os
import glob
import pprint

keywordList = []
# todo: config path
path = 'C:/Users/Tal/Desktop/Course/Spotipy/songs'
for filename in glob.glob(os.path.join(path, '*.json')):  # only process .JSON files in folder.
    with open(filename, encoding='utf-8', mode='r') as currentFile:
        data = currentFile.read().replace('\n', '')
        keyword = json.loads(data)
        if keyword not in keywordList:
            keywordList.append(keyword)


def main():
    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(keywordList)


if __name__ == '__main__':
    main()
