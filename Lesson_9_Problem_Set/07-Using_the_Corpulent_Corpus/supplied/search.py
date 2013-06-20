###
### search.py
###

# Change this to use the new WebCorpus type.

def lookup(windex, keyword):
    if keyword in windex.index:
        return windex.index[keyword]
    else:
        return None

def lucky_search(windex, keyword):
    pages = lookup(windex, keyword)
    if not pages:
        return None
    best_page = pages[0]
    for candidate in pages:
        # Note: you should not use the _ranks attribute: the _ indicates it is private to the
        #    WebCorpus object.
        if windex.rank[candidate] > windex.rank[best_page]:
                best_page = candidate
    return best_page

def quicksort_pages(pages, ranks):
    if not pages or len(pages) <= 1:
        return pages
    else:
        pivot = ranks[pages[0]]
        worse = []
        better = []
        for page in pages[1:]:
            if ranks[page] <= pivot:
                worse.append(page)
            else:
                better.append(page)
        return quicksort_pages(better, ranks) + [pages[0]] + quicksort_pages(worse, ranks)
            
def ordered_search(windex, keyword):
    pages = windex.lookup(keyword)
    return quicksort_pages(pages, windex.ranks)
