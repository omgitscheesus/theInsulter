from utils.input import file_in, website_in


def insult_in(method, location):
    if method == 'file':
        return file_in.getInsults_file(location)
    elif method == 'website':
        return website_in.getInsult_website(location)
    else:
        print('uups, something went wrong')
