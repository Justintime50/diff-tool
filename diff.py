""" Display a diff between two files in HTML. """

import difflib
# from IPython.display import display, HTML # To be used with Jupiter
HDF = difflib.HtmlDiff()
F1 = open('f1.html').readlines()
F2 = open('f2.html').readlines()
# display(HTML(HDF.make_file(F1, F2))) # To be used with Jupiter
print(HDF.make_file(F1, F2, context=True, numlines=3))
