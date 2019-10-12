#!/usr/bin/env python
import argparse

__author__ = 'mustafauzun0'

'''
CONVERTCASE
'''

def main():
    parser = argparse.ArgumentParser(description='Convert text case')

    parser.add_argument('-t', '--text', dest='text', type=str, help='Text')
    parser.add_argument('-f', '--file', dest='file', help='Text File')
    parser.add_argument('-c', '--case', dest='case', type=str, help='Text Case')
    parser.add_argument('-o', '--output', dest='output', help='Output File')

    args = parser.parse_args()

    text = ''

    if args.text:
        text = args.text
    else:
        if args.file:
            file = open(args.file, 'r')
            text = file.read()
    
    if args.case:
        if args.case == 'upper':
            text = text.upper()
        elif args.case == 'lower':
            text = text.lower()
        elif args.case == 'capitalize':
            text = text.capitalize()
    
    if args.output:
        if text:
            output = open(args.output, 'w')
            output.write(text)
            output.close()
        else:
            print('Output file create failed, because text is empty.')
    else:
        if text:
            print(text)

if __name__ == '__main__':
    main()
