with open('data/Trec.train') as f:
   labels, queries = zip(*[(x[0]," ".join(x[1:])) for x in (x.split() for x in f)])
