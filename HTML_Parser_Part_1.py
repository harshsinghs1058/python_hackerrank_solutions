# This code is written by harsh.
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for a in attrs:
            print(f"-> {a[0]} > {a[1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for a in attrs:
            print(f"-> {a[0]} > {a[1]}")


# instantiate the parser and fed it some HTML
if __name__ == "__main__":
    n = int(input())
    parser = MyHTMLParser()
    for _ in range(n):
        s = input()
        parser.feed(s)
