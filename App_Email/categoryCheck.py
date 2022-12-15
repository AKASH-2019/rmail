from pathlib import Path

def category_check(sub, body, adr):
    body = body.lower()
    sub = sub.lower()

    # +++++++++++++++++++++++SOCIAL++++++++++++++++++++++++++++


    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'word/socialSite.txt'
    file1 = file_location.open()
    for line in file1:
        wrd = line.strip()
        if adr.find(wrd) != -1:
            return "social"
    file1.close()
    file_location = script_location / 'word/socialSubject.txt'
    file1 = file_location.open()
    for line in file1:
        wrd = line.strip()
        if sub.find(wrd) != -1:
            return "social"
    file1.close()

    # +++++++++++++++++++++++FORUM++++++++++++++++++++++++++++
    fmcs, fmcb = 0, 0
    file_location = script_location / 'word/forum.txt'
    file1 = file_location.open()
    for line in file1:
        fm = line.strip()
        if sub.find(fm) != -1:
            fmcs = fmcs + 1
        if body.find(fm) != -1:
            fmcb = fmcb + 1
    totalFM = fmcs + fmcb
    if totalFM > 1 and fmcs>0:
        return "forum"
    file1.close()

    # +++++++++++++++++++++++PROMOTION++++++++++++++++++++++++++++
    pmcs, pmcb= 0, 0
    file_location = script_location / 'word/promotions.txt'
    file1 = file_location.open()
    for line in file1:
        pm = line.strip()
        if sub.find(pm) != -1:
            pmcs = pmcs+1
        if body.find(pm) != -1:
            pmcb = pmcb+1
    totalPM = pmcs+pmcb
    if totalPM > 5 and pmcs > 0:
        return "promotions"
    file1.close()
    # +++++++++++++++++++++++PRIMARY++++++++++++++++++++++++++++
    return "primary"