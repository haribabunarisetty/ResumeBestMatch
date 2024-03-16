def getBestMatch(context,category,threshold):
    resObj=[]
    context= {'context': context}
    category= {'category': category}
    threshold= {'threshold': threshold}
    resObj.append(context)
    resObj.append(category)
    resObj.append(threshold)
    return resObj