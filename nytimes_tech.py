# Knaysi, (bak9cu)

import urllib.request, re, ssl


def open_primary(url):
    link = ""
    context = ssl._create_unverified_context()
    source = urllib.request.urlopen(url, context=context)
    for line in source:
        decoded = line.decode('UTF-8').strip()
        tech_url = re.search(r'https://www.nytimes.com/pages/technology/index.html', decoded)
        if tech_url and link == "":
            link += tech_url.group(0)
    return link


def draw_info(link):
    info = {}
    context = ssl._create_unverified_context()
    source = urllib.request.urlopen(link, context=context)
    for line in source:
        decoded = line.decode('UTF-8').strip()
        headline = re.search(r'data-rref=\"\">[^<]+', decoded)
        link = re.search(r'<a href=\"[^\"]+\"\sdata-rref=\"\">[A-Z]', decoded)
        if headline and link:
            link = link.group()
            info[headline.group().replace("data-rref=\"\">", "")] = link[9:len(link)-16]
    return info


def sort_info(dict):
    loc = 1
    for item in dict.items():
        print("Article Number:", loc)
        print(item)
        print()
        loc += 1




link = open_primary("https://www.nytimes.com/")
info = draw_info(link)
result = sort_info(info)
