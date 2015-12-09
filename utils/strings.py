import re


def lcfirst(s):
    if len(s) == 0:
        return s
    else:
        return s[0].lower() + s[1:]


def ucfirst(s):
    if len(s) == 0:
        return s
    else:
        return s[0].upper() + s[1:]


def slugify(text, delimeter = '-' , num = None):
    text = text.lower()
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)

    if num is not None:
        text += ' ' + str(num)

    text = re.sub(' +',' ', text)
    return text.strip().replace(' ',delimeter)


def slugname(text):
    text = text.lower()
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    text = re.sub(' +',' ', text)
    return text.strip()


def slugtitle(slug):
    return slugname(slug).title()


def camelcase(text):
    text = slugtitle(text)
    text = text.title().replace(' ','')
    return lcfirst(text)


def startslash(text):
    if not text.startswith('/'):
        return  '/' + text 
    else:
        return text


def startendslash(text):
    return startslash(endslash(text))


def endslash(text):
    if not text.endswith('/'):
        return text + '/'
    else:
        return text

