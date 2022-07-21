from newspaper import Article

def getSummary(url:str = '') -> list:
    article = Article(url)
    article.download()
    article.parse()

    title = article.title

    

    keywords = article.keywords

    text = article.text
    # print(title)

    return title, text
if __name__ == "__main__":
    getSummary("https://bbs.archlinux.org/viewtopic.php?id=260589")


    