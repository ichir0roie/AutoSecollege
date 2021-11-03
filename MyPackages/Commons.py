import os

pathChromeProfile="Data/ChromeProfile/"

class page:
    homePage="https://secollege.jp/"
    movie=homePage+"course/movie/"
    detail=homePage+"/course/detail/"


def getCssSelect(elemClassName: str):
    cssSelect = elemClassName.replace(" ", ".")
    cssSelect = "." + cssSelect
    return cssSelect

class cssSelect:
    alwaysButton=getCssSelect("course-type current")
    courseTypeList=getCssSelect("course-type-list")
    simpleCard=getCssSelect("simple-card")
    buttonContainer=getCssSelect("button-container")

    class child:
        buttonPlay="vjs-big-play-button"

class elemTexts:
    buttonWatchMovie="動画を見る"

    class child:
        buttonNextMovie = "次の動画へ >"


def getFullPath(path):
    cwd = os.getcwd().replace("\\","/")+"/"
    path = cwd + path
    return path


if __name__ == '__main__':
    print(getFullPath(pathChromeProfile))