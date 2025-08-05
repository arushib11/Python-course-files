class Page:
    def __init__(self,text,page_number):
        self.text=text
        self.page_number=page_number

    # overriding len to give length of text on the page
    def __len__(self):
        return len(self.text)
    
    # overriding len to give string contained in the page
    def __str__(self):
        #return self.text
        return f"{self.text},{self.page_number}"
    
    # overriding repr to get internal representation
    def __repr__(self):
        return self.__str__()

class Book:
    def __init__(self,title,author,pages,id_number):
        self.title=title
        self.author=author
        self.pages=pages
        self.id_number=id_number

    # overriding len to give number of pages a book has
    def __len__(self):
        return len(self.pages)    
    
    # overriding len to give number of pages a book has
    def __str__(self):
        output= f"Book({self.title},{self.author},{self.id_number})"
        for page in self.pages:
            output+="\n"+str(page)
        return output
    
    # overriding repr function to get internal representation
    # we want to print the id_number instead of internal representation
    def __repr__(self):
        return f"Book(id_number={self.id_number})"

page1=Page("page1!",1)   
page2=Page("This is page2!",2)   
book=Book("God is great","God",[page1,page2],1)
print(len(page1))
print(len(page2))
print(len(book))
print(page1,page2) # calls string function on both objects, printing out internal representation since str has not be overridden
print(book)
print(repr(book))

# Trying out the repr function
print(repr([1,2,3,4]))
print(repr(True))
