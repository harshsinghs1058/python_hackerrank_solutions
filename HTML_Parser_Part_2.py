# This code is written by harsh.
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        temp = str(data).count("\n")
        if temp == 0:
            print(f">>> Single-line Comment\n{data}")
        else:
            print(f">>> Multi-line Comment\n{data}")

    def handle_data(self, data):
        if len(data) > 1:
            print(f">>> Data\n{data}")


if __name__ == "__main__":
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += "\n"
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
