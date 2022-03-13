import abc


class HTMLElement(metaclass=abc.ABCMeta):
    def __init__(self, style=None):
        self.style = style

    @abc.abstractmethod
    def __str__(self):
        pass

    def style_string(self):
        return f' style="{self.style}"' if self.style is not None else ''


class Link(HTMLElement):
    def __init__(self, url, element, style=None):
        super().__init__(style)
        self.url = url
        self.element = element

    def __str__(self):
        if self.style is not None and self.style != '':
            return '<a href="{}" style="{}">{}</a>'.format(self.url, self.style, self.element)
        else:
            return '<a href="{}">{}</a>'.format(self.url, self.element)


class TextElement(HTMLElement):
    def __init__(self, element, style=None):
        super().__init__(style)
        if type(element) == str or issubclass(type(element), TextElement):
            self.element = element
        else:
            raise ValueError('Element must be a string or TextElement')

    @abc.abstractmethod
    def tag_name(self):
        pass

    def __str__(self):
        s = self.style_string()
        t = self.tag_name()
        return '<{}{}>{}</{}>'.format(t, s, self.element, t)


class BoldText(TextElement):
    def tag_name(self):
        return 'b'


class ItalicText(TextElement):
    def tag_name(self):
        return 'i'


class Paragraph(HTMLElement):
    def __init__(self, elements, style=None):
        super().__init__(style)
        self.elements = elements

    def __str__(self):
        join_ele = ' '.join([str(element) for element in self.elements])
        s = self.style_string()
        display = '<p{}>{}</p>'.format(s, join_ele)
        return display


class Body(HTMLElement):
    def __init__(self, elements, style=None):
        super().__init__(style)
        self.elements = elements

    def __str__(self):
        join_ele = '\n    '.join([str(element) for element in self.elements])
        s = self.style_string()
        return f'<body{s}>\n    {join_ele}</body>'


p0 = Paragraph(["Text can be", ItalicText("cursive,"), BoldText("bold"), "or",
ItalicText(BoldText("both"), style="color:red")])
print("first paragraph as HTML:")
print(p0)
print()
p1 = Paragraph([BoldText("Chalmers"), Link('https://www.chalmers.se', "link", 'color:blue')])
print("second paragraph as HTML:")
print(p1)
print()
body = Body([p0, p1])
print("whole body as HTML:")
print(body)