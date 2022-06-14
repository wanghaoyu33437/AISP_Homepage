from flask import render_template
from models import Publications,Member

def publications():
    all_publications = Publications.get_all_publications()
    publications_groupByear  =dict()
    authors_set = list()
    for p in all_publications:
        new_p=dict()
        year = p.year
        new_p['year']=p.year
        title = p.title
        new_p['title']= title
        conference = p.conference
        new_p['conference'] = conference
        authors = p.authors
        new_p['authors'] = []
        tag =p.tag
        new_p['tag'] = tag
        authors = p.authors.split(',')
        for a in authors:
            new_p['authors'].append(a)
            if a not in authors_set:
                authors_set.append(a)
        if year not in publications_groupByear.keys():
            publications_groupByear[year] = [new_p]
        else:
            publications_groupByear[year].append(new_p)
    authors = Member.query.filter(Member.en_name.in_(authors_set)).all()
    author_url = dict()
    for a in authors:
        print(a.en_name)
        author_url[a.en_name] = a.url
    print(author_url)
    return render_template('en/publications.html',years=publications_groupByear.keys() ,publications= publications_groupByear,author_url=author_url)