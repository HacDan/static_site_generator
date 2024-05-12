class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, comp):
        if self.text != comp.text:
            return False

        if self.text_type != comp.text_type:
            return False

        if self.url != comp.url:
            return False

        return True 

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
