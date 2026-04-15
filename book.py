class Book:
  def __init__(self, title, author, is_issued=False):
    self.title = title
    self.author = author
    self.is_issued = is_issued

  def issue(self):
    self.is_issued = True

  def return_book(self):
    self.is_issued = False

  def to_dict(self):
    return{
      "title": self.title,
      "author": self.author,
      "is_issued":self.is_issued
    }  
    
  @staticmethod
  def from_dict(data):
    return Book(data["title"], data["auhtor"], data[is_issued])  