from flask import render_template
from models import Publications,Member

def publications():
    all_publications = Publications.get_all_publications()
    publications_groupByear  =dict()
    authors_set = list()
    tags = set()
    for p in all_publications:
        new_p=dict()
        new_p['year']=p.year
        new_p['title']= p.title
        new_p['conference'] = p.conference

        new_p['tag'] = [i for i in p.tag.split(',')]
        for i in p.tag.split(','):
            tags.add(i)
        new_p['authors'] = []
        authors = p.authors.split(',')
        for a in authors:
            new_p['authors'].append(a)
            if a not in authors_set:
                authors_set.append(a)
        if p.year not in publications_groupByear.keys():
            publications_groupByear[p.year] = [new_p]
        else:
            publications_groupByear[p.year].append(new_p)
    authors = Member.query.filter(Member.en_name.in_(authors_set)).all()
    author_url = dict()
    for a in authors:
        # print(a.en_name)
        author_url[a.en_name] = a.url
    # print(author_url)
    return render_template('en/publications.html',years=publications_groupByear.keys() ,tags = tags,publications= publications_groupByear,author_url=author_url)