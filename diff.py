import difflib
from IPython.display import display, HTML
hdf = difflib.HtmlDiff()
F1 = open('f1.html').readlines()
F2 = open('f2.html').readlines()
# display(HTML(hdf.make_file(F1, F2))) # To be used with Jupiter
print(hdf.make_file(F1, F2, context=True, numlines=3))
