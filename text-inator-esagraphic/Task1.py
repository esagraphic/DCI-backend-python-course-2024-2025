text = input('Enter the word:')
text_count = len(text)
if text_count <=6:
    print(f'{text}inator {text_count}000')
else:
    print(f'{text}-inator {text_count}000')
