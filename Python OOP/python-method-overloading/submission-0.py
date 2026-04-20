class TextProcessor:
    # Implement method overloading for format_text method
    def format_text_one(self,text1:str):
        return(text1.upper())

    def format_text(self,*args:str):
        s1=""
        for i in args:
            s1+=i
        return(s1)


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text_one("hello"))
print(processor.format_text("hello", "world"))
