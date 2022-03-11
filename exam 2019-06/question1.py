from collections import Counter

s = '<a href="http://www.amazon.co.uk/gp/deals">amazon deals</a> and <a href="www.google.com">google</a>'

def extract_links(s):
    links = []
    pos = 0
    while True:
        pos = s.find('<a href="', pos)
        if pos == -1:
            break
        pos += 9
        endpos = s.find('"', pos)
        links.append(s[pos:endpos])
        pos = endpos  # Start from here next search
    return links



def extract_domain(link):
    link = link.strip('https://')
    link = link.split('/')
    link = link[0]

    return link


with open('links.html') as file:
    counter = Counter()
    for line in file:
        links = extract_links(line)
        for i in links:
            domain = extract_domain(i)
            counter[domain] += 1
    the_list = counter.most_common()
    print(the_list)
    header = '| Domain' + ' '*13 + '| Links |'
    line = '+' + '-'*20 + '+-------+'
    print(header)
    print(line)

    for domain in the_list:
        print('{:20s} | {:5.0f} |'.format(domain[0], domain[1]))







#a = extract_domain('https://www.amazon.co.uk')
#b = extract_domain('http://www.foo.org/stuff/index.html')
#c = extract_domain('google.se/search?q=kitten')

#print(a)
#print(b)
#print(c)