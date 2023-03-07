def cleanLs(x):
    lsN = []
    for k in range(0,len(x)):
        if x[k] != '':
            lsN.append(x[k])
    return lsN
def urlToPieces(ls):
    for k in range(0,len(ls)):
        ls[k]=splUrl(ls[k])
    return ls
def splUrl(x):
    if '.com' in x:
        return cleanLs(x.split('.com')[1].split('/'))
def getPerc(x,y):
    if x in y:
        return float(len(x)/len(y))
    return 0
def compareStr(reqs,jsPerc):
    n = '',
    for c in range(0,len(jsPerc['current']['urlLs'][-1])):
      perc = 0
      if jsPerc['current']['urlLs'][-1][c] in reqs:
          if n+jsPerc['current']['urlLs'][-1][c] in reqs:
              n = n + jsPerc['current']['urlLs'][-1][c]
              perc = getPerc(n,req)
          else:
              if n != '':
                  perc = getPerc(n,req)
                  n = ''
          if perc>jsPerc['urlPerc'][-1]:
                  jsPerc['urlPerc'][-1] = perc
    return jsPerc
urls,request = [],requests
reques,urlLs = splUrl(request),urlToPieces(urlsList)

for i in range(0,len(reques)):
    reqs = reques[i]
    
    for k in range(0,len(urlLs)):
        if k not in jsPerc:
            jsPerc[k] = {'urlLs':'','urlPart':'','urlPiece':[],'urlPerc':[]}
        jsPerc[k]['urlLs'] = urlsList[k]
        jsPerc[k]['urlPart'] = urlLs[k][i]
        jsPerc[k]['urlPiece'].append('')
        jsPerc[k]['urlPerc'].append(getPerc(jsPerc[k]['urlPart']))
        jsPerc = compareStr(reqs,jsPerc)
        
        
            
                   
                
    
