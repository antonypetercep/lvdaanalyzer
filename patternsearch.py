# python implementation of grep first_pattern | grep second_pattern


import re


class PatternSearch:
    def __init__(self, first_pattern, second_pattern):

        self.first_pattern = first_pattern
        self.second_pattern = second_pattern

    def searchforpattern(self, first_pattern, second_pattern):

        for matched_lines in filter(lambda line: re.search(first_pattern, line), open('vda.log')):
            # print(matched_lines,end='')
            m = re.search(second_pattern, matched_lines, re.I)
            if m:
                print(matched_lines)
