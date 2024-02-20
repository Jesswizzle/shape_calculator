class Rectangle:
  # Rectangle object with width and height attributes

  def __init__(self, width, height):
    self.width = width
    self.height = height

# set_width

  def set_width(self, width):
    self.width = width

# set_height

  def set_height(self, height):
    self.height = height

# get_area: Returns area (width * height)

  def get_area(self):
    return (self.width * self.height)

# get_perimeter: Returns perimeter (2 * width + 2 * height)

  def get_perimeter(self):
    return ((2 * self.width) + (2 * self.height))

# get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)

  def get_diagonal(self):
    return (((self.width**2) + (self.height**2))**.5)

# get_picture: String represents the shape using lines of "*"
# number of lines should be equal to the height
# number of "*" in each line == equal to width
# new line (\n) at the of each line
# If width or height > 50, return string: "Too big for picture."

  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    else:
      row = (('*' * self.width) + '\n')
      shape = row * self.height
    return shape

# get_amount_inside: Takes another shape (square or rectangle) as an argument
# Returns the number of times the passed in shape could fit inside the shape (with no rotations)
# eg. a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4
# Use floor remiander to make it easier

  def get_amount_inside(self, another_shape):
    return (self.get_area() // another_shape.get_area())

# If an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'


# Square class
class Square(Rectangle):

  # Subclass of Rectangle.
  # When a Square object is created, a single side length is passed in
  # The __init__ method should store the side length in both the width and height attributes from the Rectangle class
  # Make square class attribute length - super() will then store length as width and height back to parent rectangle class

  def __init__(self, length):
    super().__init__(length, length)

# Square class can access Rectangle class methods but should also contain a set_side method
#If an instance of a Square is represented as a string, it should look like: Square(side=9)

  def set_side(self, side):
    self.width = side
    self.height = side


# set_width and set_height methods on the Square class should set both the width and height

  def __str__(self):
    return f'Square(side={self.width})'
