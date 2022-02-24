import urllib.request, json
import pandas as pd



def fetchBooks(url : str) -> pd.DataFrame:
  Booklist = []
  response = urllib.request.urlopen(url)
  data = json.loads(response.read())

  for book in data['books']:
    CurrentBookDetails = {}
    try:
        CurrentBookDetails["Book Title"] = book["title"]
        CurrentBookDetails["Book Link"] = book["affiliates"][0]["url"]
        CurrentBookDetails["Book Author"] = book["author"]
        CurrentBookDetails["Book Review"] = book["review"]
        CurrentBookDetails["Book Type"] = data["paramsAsTextString"]
        Booklist.append(CurrentBookDetails)
    except:
        print("Request has failed")
        continue
  df = pd.DataFrame.from_dict(Booklist, orient='columns')

  return df





if __name__ == '__main__':
    Allbooks = []
    for i in range(1,13):
        for j in range(1,11):
            url = "https://www.whichbook.net/api/v1/search?q"+ str(i) + "=" + str(j) +"&pagesize=499"
            Allbooks.append(fetchBooks(url))

BookTypeDataFrame = pd.concat(Allbooks)
BookTypeDataFrame.to_csv('BookRecommenddationDate499.csv')
print(BookTypeDataFrame)
