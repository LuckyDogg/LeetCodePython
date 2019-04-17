def sortdate(sort_list):
    try:
        sortedlist=sorted(sort_list, key=lambda x:x[1]['date'].split('-'))
        return sortedlist
    except:
        return False


