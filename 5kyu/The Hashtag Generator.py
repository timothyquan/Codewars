
def generate_hashtag(s):
    words = ''.join(s.title().split(' '))
    if 1 > len(words) or len(words) > 139: return False
    return '#' + words

print(generate_hashtag(' Hello there thanks for trying my Kata'))
print(generate_hashtag('              '))