class Icons:

    IMG_PREFIX = 'img/'

    @staticmethod
    def getImgThemePrefix():
        if True:
            return Icons.IMG_PREFIX + 'dark/'
        else:
            return Icons.IMG_PREFIX + 'light/'

    @staticmethod
    def getClose():
        return Icons.getImgThemePrefix() + 'close-circle.png'

    @staticmethod
    def getColorClose():
        return Icons.IMG_PREFIX + 'close-circle-red.png'

    @staticmethod
    def getCloseOutline():
        return Icons.getImgThemePrefix() + 'close-circle-outline.png'

    @staticmethod
    def getAdd():
        return Icons.getImgThemePrefix() + 'add-circle.png'

    @staticmethod
    def getColorAdd():
        return Icons.IMG_PREFIX + 'add-circle-green.png'

    @staticmethod
    def getAddOutline():
        return Icons.getImgThemePrefix() + 'add-circle-outline.png'

    @staticmethod
    def getPwdField():
        return Icons.getImgThemePrefix() + 'textbox-password.png'

    @staticmethod
    def getEye():
        return Icons.getImgThemePrefix() + 'eye.png'
