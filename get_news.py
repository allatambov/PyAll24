def get_news(link0):
    """
    Parameters:
        link0 – url for one piece of news (string)
    Returns:
        list of the following features:
            * new's title (string)
            * new's date (string)
            * new's author (string)
            * new's difficulty (string)
            * new's rubrics (string)
            * new's text (string)
    """
    page0 = requests.get(link0)
    soup0 = BeautifulSoup(page0.text)
    
    title = soup0.find("title").text.replace("\xa0", " ")
    date = soup0.find("meta", {"itemprop" : "datePublished"}).get("content")
    author = soup0.find("meta", {"name" : "author"}).get("content")
    div = soup0.find("div", {"class" : "flex flex-wrap lg:mb-10 gap-2 text-tags xl:pr-9"})
    spans = div.find_all("span")
    diffc = spans[3].text
    rubs_raw = spans[4:]
    rubs = ", ".join([r.text for r in rubs_raw])
    
    # для текста – более универсальный вариант без лишней новости
    pars = soup0.find_all("p", {"class" : "mb-6"})
    classes = [p.get("class") for p in pars]
    for c in classes:
        if "text-main-gray" in c:
            i = classes.index(c)
    pars_upd = pars[:i]
    text = " ".join([p.text for p in pars_upd])
    text = text.replace("\xa0", " ").replace("\n", " ")
    
    return [title, author, date, diffc, rubs, text]