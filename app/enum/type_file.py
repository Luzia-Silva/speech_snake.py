def Allowed_file(filename):
    ALLOWED_EXTENSIONS = {'mp3', 'wav'}
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
