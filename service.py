def getBestMatch(context,category,threshold,noOfMatches,inputPath):
    resObj=[]
    status= {'status':'success'}
    count= {'count': ""}
    metadata= {'metadata': {'confidenceScore': ""}}
    results= {'results': [""]}
    resObj.append(status)
    resObj.append(count)
    resObj.append(metadata)
    resObj.append(results)
    return resObj