import urllib.request

f_hand = urllib.request.urlopen('http://127.0.0.1:9001/romeo.txt')
for line in f_hand:
    print(line.decode('utf-8').strip())