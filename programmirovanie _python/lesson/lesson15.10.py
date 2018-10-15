"""wowo momo momomomomomomo aaaaaa wwwwwww documentiruyushaya straka!!!! incredibileeeeeeeee"""


def f1():
    """ononononono incredibile che roba""" #works as function "pass", in comparison to #, is commentary that is sent in function f1.__doc__, so is considered as documentation

import re #import Regular Expressions, does not work in lists
s = "<<совесть>>!"
r = re.search("<<(.+?)>>", s) #1 arg regex,2 arg data, this finds is something is inside the <<>>
if r:
    word = r.group(1) #search needs groups, they starts counting from 1 and not 0 in regex
print(word)

c = input()
if re.search("^[0-9]+$", c): #finds if it is a digit field
    print(c)

a = re.findall("",) #(regexp, data), returns a list instead of groups

s = re.sub["[а-я]", "1", s] #replace left part with right one, can put a callable element
s = re.sub("[а-я]+?(,|;)", r"a\1", s) #change all words before commas with a
s = re.sub("(о|е)р(у|ю)", r"\2р\1", s) #invert group 1 with 2 in a word with р

regexp = re.compile("[а-я]+?<<") #does not load expression every time in memory making things faster and lighter
r = regexp.search(s) #regexp make superflous to write regex, can be called on the method and needs only data as arg