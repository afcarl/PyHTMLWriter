import sys
sys.path.append('/media/data-nix/work/side/PyHTMLWriter/src');
from Table import Table
from TableWriter import TableWriter

t = Table()
t.readFromCSV('table.csv')
tw = TableWriter(t, 'out', makeChart = True)
tw.write()
