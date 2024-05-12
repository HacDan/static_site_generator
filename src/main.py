from textnode import TextNode

print("hello world")

def main():
    textnode1 = TextNode(text="This is some text", text_type="bold", url="https://www.google.com")
    textnode2 = TextNode(text="This is more text", text_type="italic", url="https://www.hacdan.org")

    print(textnode1)
    print(textnode2)


if __name__ == "__main__":
    main()
