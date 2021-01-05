import sys
import os
import random
docname = 'Exam.tex'
folder = os.getcwd()
bank = os.path.join(folder, 'banks/')
doc = os.path.join(folder, docname)
pre = open(os.path.join(folder, 'preExam.tex'),'r')
post = open(os.path.join(folder, 'postExam.tex'),'r')
qdirs = (('IDGLin', 2),('LinEq', 2))

questions = []
#Looks at pairs of arguments to determine which directories to use and how many questions from each.
for bankf, number in qdirs:
    qfiles = [
        os.path.join(dirpath, fname) 
        #Walks through all directories and filenames in the listed directories 
        for dirpath, dirnames, filenames in os.walk(os.path.join(bank, bankf))
        for fname in filenames 
        if os.path.splitext(fname)[-1].lower() == '.tex'
        ]
    for qfile in random.sample(qfiles, number):
        with open(qfile, 'r') as qfh:
            questions.append(qfh.read())
with open(doc, 'w') as efh:
    prefile = pre.read()
    print(prefile,file=efh)
    for question in questions:
        print(question, file=efh)
    postfile = post.read()
    print(postfile,file=efh)

#cmd = [pdflatex, docname] 
#os.system(' '.join(cmd))
#os.system(' '.join(cmd))


