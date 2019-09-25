from utils.output import shell_out, picture_out, file_out


def select_out(data, method, location):
    if method == 'file':
        file_out.file_out(data, location)
    elif method == 'shell':
        shell_out.shell_out(data)
    elif method == 'pic':
        print('not implemented yet')
