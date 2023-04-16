def promptConfig(s, **kwargs):
    aspect = kwargs.get('aspect', '1:1')
    chaos = kwargs.get('chaos', 0)
    no = kwargs.get('no', '')
    quality = kwargs.get('quality', 1)
    anime = kwargs.get('anime', '')

    prefix = f' --ar {aspect} --chaos {chaos} --q {quality}'
    if 'no' in kwargs:
        prefix += ' --no {no}'
    if 'anime' in kwargs:
        prefix += ' --niji'
    return s + prefix
