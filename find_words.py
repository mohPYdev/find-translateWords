
# a program to find the important words in an article and their meanings.

from googletrans import Translator

def main():
    file = open('text.txt', encoding="utf8")
    content = file.read()
    words = content.split()
    file.close()
    impWords = set([])
    for word in words:
        if len(word) > 10:
            impWords.add(word)
    for word in impWords:
        translator = Translator()
        trans = translator.translate(word , 'fa')
        f = open('important.txt', 'a' , encoding="utf-8")
        f.write(word + (20 - len(word)) * ' '+':'+ trans.text + '\n')
        f.close()


if __name__ == '__main__':
    main()
