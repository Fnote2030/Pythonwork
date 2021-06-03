#coding=utf-8

try:
    with open("Angela.txt",encoding="utf-8") as f:
        contents =f.read()
except FileNotError:
    print(f"The file Angela.txt is not exist")
else:
    #1、中文字数
    #中文以utf-8编码的时候用三个ASCII表示，以gbk编码的时候用两个ASCII表示
    num_words_1= (len(contents.encode('utf-8')) - len(contents))//2
    print(f"The file Angela.txt has about {num_words_1} Chinese words")

    #num_words= (len(contents.encode('gbk')) - len(contents))
    #print(f"The file Angela.txt has about {num_words} words")

    #2、英文词数
    words =contents.split() #以换行、空格分割
    num_words_2=len(words)-num_words_1
    print(f"The file Angela.txt has about {num_words_2} English words")










