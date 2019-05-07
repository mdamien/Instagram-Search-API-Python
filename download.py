import sys
import requests
import re

REGEXES = {
    'hashtag': re.compile(r'(?:#)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)'),
    'username': re.compile(r'(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)'),
}

print("hashtag", "user", "url_or_text", sep='\t')
for i, line in enumerate(sys.stdin):
    url, text, user = line.strip().split('\t')
    req = requests.get(url)
    f = "%d.jpg" % i
    with open(f'%s/%d.jpg' % (sys.argv[1], i), 'wb') as img:
        img.write(req.content)
    for hashtag in set(REGEXES['hashtag'].findall(text)):
        print(hashtag, user, text, sep='\t')
        print(hashtag, user, f, sep='\t')