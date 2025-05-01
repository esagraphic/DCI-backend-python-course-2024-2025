def pig_latin(*words, suffix='ay', single=False):
    vowels = 'aeiouAEIOU'
    result = []

    for sentence in words:
        translated_words = []
        for word in sentence.split():
            if word[0] in vowels:
                translated_word = word + suffix
            else:
                translated_word = word[1:] + word[0] + suffix
            translated_words.append(translated_word)
        result.append(" ".join(translated_words))
    
    if single:
        return " ".join(result)
    else:
        return result

test1_data = ["Word", "Apple"]
test1_config = {}
print(pig_latin(*test1_data, **test1_config))  


test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}
print(pig_latin(*test2_data, **test2_config))  


test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}
print(pig_latin(*test3_data, **test3_config))  
