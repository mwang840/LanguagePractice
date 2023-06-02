def domain_name(url):
    #Split the string by https://, www. then split if none are applicabloe
    #then split or parse the string by the . check if its .com/.cu/etc...
    # return the name of the url
    # or we could use the parse library/check the length of the string
    name = url.replace("https://", "").replace("http://", "").replace("www.", "").split(".")
    return name[0]
    # name = url.split("/")
    # domainOnly = ""
    # if(name[0] == "https:" or name[0] == "http:" or "co" not in name):
    #     name = name[2].split(".")
    # else:
    #     name = name[0].split(".")

    # #checks the length of the array splitted
    # if(len(name) == 2):
    #     domainOnly = name[0]
    # else:
    #     domainOnly = name[1]    

    # return domainOnly


def main():
   
    dotco = "http://google.co.jp"
    print(domain_name(dotco))

if __name__ in "__main__":
    main()    