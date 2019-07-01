from functools import wraps
# https://stackoverflow.com/questions/5929107/decorators-with-parameters


def make_html(element):
    def wrap(func):
        @wraps(func)
        def wrapper_make_html(*args):
            # print(f'Wrapper args: {args}')
            result = f'<{element}>{func(*args)}</{element}>'
            print(result)
            return result
        return wrapper_make_html
    return wrap


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text


print(get_text())
