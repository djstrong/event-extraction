slownik = {}
f = open("morfologik.txt")
#ff = f.read()
for line in f:#ff.split('\n'):
    line = line.rstrip()
    odmieniona, podstawowa, znaczniki = line.split('\t')

    if odmieniona not in slownik:
	slownik[odmieniona] = [podstawowa]
    else:
	slownik[odmieniona].append(podstawowa)
f.close()