import requests

api_key="39bfd897500c48e8b9f36d1c09ba96ef"





def news():
    main_url="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+api_key
    news=requests.get(main_url).json()
    #print(news)
    article=news["articles"]
    #print(article)

    news_article=[]
    for arti in article:
        news_article.append(arti["title"])
        print(news_article)

    for i in range(5): #for 5 news
        print(i+1,news_article[i]) #for numbering in news
    #for i in range(len(news_article)):
     #   print(news_article[i])

news()
