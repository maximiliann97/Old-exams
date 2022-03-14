class Color:
    def __init__(self, red, green, blue):
        if red < 0 or red > 1 or green < 0 or green > 1 or blue < 0 or blue > 1:
            raise ColourError('Colour must range from 0 to 1')
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return 'Color(red={}, green={}, blue={})'.format(self.red, self.green, self.blue)

    @staticmethod
    def from_html(v):
        r = int(v[1:3])/255
        g = int(v[3:5])/255
        b = int(v[5:7])/255
        return Color(r, g, b)

    def html(self):
        return '#{:02x}{:02x}{:02x}'.format(int(self.red * 255), int(self.green * 255),
                                            int(self.blue * 255))

    def __add__(self, other):
        if self.red+other.red > 1:
            red = 1
        else:
            red = self.red + other.red

        if self.green+other.green > 1:
            green = 1
        else:
            green = self.green+other.green

        if self.blue+other.blue > 1:
            blue = 1
        else:
            blue = self.blue+other.blue

        return Color(red, green, blue)

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue


class ColourError(Exception):
    def __repr__(self):
        return ColourError


cyan = Color(0, 1, 1)
magenta = Color(1, 0, 1)
white = Color.from_html('#FFFFFF')
if cyan + magenta == white:
    print('{} and {} makes {}'.format(cyan.html(), magenta, repr(white)))
try:
    Color(1.1, 0.5, 0.5)
except ValueError:
    print('Value error caught')