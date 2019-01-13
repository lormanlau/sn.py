import csv
import codecs

# path = 'KFP1Script.csv'

datafile = 'movie.txt'

pairs = []

# with open(path, 'rb') as f:
#   for row in f:
#     pairs.append(row)
  


# with open(datafile, 'w') as outputfile:
#     writer = csv.writer(outputfile, delimiter="*", lineterminator='\n')
#     writer.writerow(pairs)

with open(datafile, 'r', encoding='iso-8859-1') as f:
  pair = []
  for line in f:
    values = line.split(": ")
    if len(pair) == 1:
      try:
        pair.append(values[1].rstrip())
      except:
        continue
      pairs.append(pair)
      pair = []
    else:
      try:
        pair.append(values[1].rstrip())
      except:
        continue
  if len(pair) == 1:
    pair.append("Fight me")
    pairs.append(pair)

delimiter = '\t'
# Unescape the delimiter
delimiter = str(codecs.decode(delimiter, "unicode_escape"))

with open(datafile, 'w', encoding='utf-8') as outputfile:
    writer = csv.writer(outputfile, delimiter=delimiter, lineterminator='\n')
    for pair in pairs:
        writer.writerow(pair)
    