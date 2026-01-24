status_code = int(input('status code:'))
match status_code:
    case 400: description = 'bad request'
    case 401: description = 'unauthorized'
    case 403: description = 'forbidden'
    case 404: description = 'not found'
    case 405: description = 'method not allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'too many requests'
    case _: description = 'unknown error'
print('status code description:', description)