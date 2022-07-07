"""
Sluggifify the sentence. The process is 2 folds
1. Lower case the file name
2. Replace the space with '-'
"""
noise = [',', '%', '"']


def slug(sentence):
    new_name = []
    for word in sentence.split(' '):
        slug_word = word.strip().lower()

        for noise_word in noise:
            slug_word = slug_word.replace(noise_word, '')

        new_name.append(slug_word)

    return '-'.join(new_name)


if __name__ == '__main__':
    input = 'Creating delight is 90% "how", 10% "what"'
    slugiffied_word = slug(input)
    print(slugiffied_word)
