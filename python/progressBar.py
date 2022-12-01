

from time import sleep


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix} {progresbars}    ', end=printEnd)
    if iteration == total:
        print()


maxprogress = 100
progressiteration = 0
progresbars = 0
progresori = progressiteration


def updateProgress():
    global progressiteration
    global progresbars
    progressiteration += 1
    if maxprogress == progressiteration:
        progressiteration = progresori
        progresbars += 1
    printProgressBar(progressiteration, maxprogress, prefix='Progress:',
                     suffix='Complete', length=50)


maxprogress = 100
progressiteration = 0
progresbars = 0
progresori = progressiteration

for i in range(1000):
    updateProgress()
    sleep(0.1)
