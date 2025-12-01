def word_count (text):
    words = 1
    text = text.strip()
    for i in range(len(text)):
        
        if text[i]==' ':
            if text[i+1] != ' ':
                words += 1
    print(words)