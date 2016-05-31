"""

Verify collection before transfer to dark archive.

Create a list of folders/files that should be present in an archive collection
based upon user inputs. Compare that list to the existing folders/files
looking for missing folders/files. Compare the existing folders/files
to the list looking for extra folders/files that shouldn't be present.

"""

import os
import os.path

baseDir = input('Enter location to check (e.g. C:\\Users\\christopher\\Desktop\\ttu_test02): ')
collectionCode = input('Enter collection code (e.g. ttu_ices01): ')
firstItemNumber = input('Enter first item number (e.g. 1): ')
lastItemNumber = input('Enter last item number (e.g. 100): ')

itemFolderList = []
firstItemNumber = str(firstItemNumber).zfill(6)
lastItemNumber = str(lastItemNumber).zfill(6)
totalItemNumber = int(lastItemNumber) - int(firstItemNumber) + 1

contentFolderName = 'content'
archiveFolderName = 'archive'
displayFolderName = 'display'

for number in range(int(totalItemNumber)):
    itemFolderName = collectionCode + '_' + str(firstItemNumber)
    itemFolderList.append(itemFolderName)
    firstItemNumber = int(firstItemNumber)
    firstItemNumber += 1
    firstItemNumber = str(firstItemNumber).zfill(6)

for dirPath, dirNames, fileNames in os.walk(baseDir):
    if dirPath == baseDir:
        for itemFolderName in itemFolderList:
            if itemFolderName not in dirNames:
                print('Missing folder: ' + itemFolderName)
        for dirName in dirNames:
            if dirName not in itemFolderList:
                print('Extra folder:   ' + dirName)
    for itemFolderName in itemFolderList:
        contentFolderPath = os.path.join(itemFolderName, contentFolderName)
        if dirPath == os.path.join(baseDir, itemFolderName):
            if contentFolderName not in dirNames:
                print('Missing folder: ' + contentFolderPath)
            for dirName in dirNames:
                if dirName != contentFolderName:
                    print('Extra folder:   ' + os.path.join(itemFolderName, dirName))
    for itemFolderName in itemFolderList:
        contentFolderPath = os.path.join(itemFolderName, contentFolderName)
        archiveFolderPath = os.path.join(itemFolderName,
                                         contentFolderName,
                                         archiveFolderName)
        displayFolderPath = os.path.join(itemFolderName,
                                         contentFolderName,
                                         displayFolderName)
        if dirPath == os.path.join(baseDir, itemFolderName, contentFolderName):
            if archiveFolderName not in dirNames:
                print('Missing folder: ' + archiveFolderPath)
            if displayFolderName not in dirNames:
                print('Missing folder: ' + displayFolderPath)
            for dirName in dirNames:
                if dirName != archiveFolderName:
                    if dirName != displayFolderName:
                        print('Extra folder:   ' + os.path.join(contentFolderPath,
                                                                dirName))
    for itemFolderName in itemFolderList:
        contentFolderPath = os.path.join(itemFolderName, contentFolderName)
        archiveFolderPath = os.path.join(itemFolderName,
                                         contentFolderName,
                                         archiveFolderName)
        displayFolderPath = os.path.join(itemFolderName,
                                         contentFolderName,
                                         displayFolderName)
        archiveFileName = (itemFolderName + '.tif')
        displayFileNameJPG = (itemFolderName + '.jpg')
        displayFileNamePDF = (itemFolderName + '.pdf')
        if dirPath == os.path.join(baseDir, itemFolderName,
                                   contentFolderName, archiveFolderName):
            if archiveFileName not in fileNames:
                print('Missing file:   ' + os.path.join(contentFolderPath,
                                                        archiveFolderName,
                                                        archiveFileName))
            for fileName in fileNames:
                if fileName != archiveFileName:
                    print('Extra file:     ' + os.path.join(contentFolderPath,
                                                            archiveFolderName,
                                                            fileName))
        if dirPath == os.path.join(baseDir, itemFolderName,
                                   contentFolderName, displayFolderName):
            if displayFileNameJPG not in fileNames:
                if displayFileNamePDF not in fileNames:
                    print('Missing file:   ' + os.path.join(contentFolderPath,
                                                            archiveFolderName,
                                                            displayFileNamePDF))
            for fileName in fileNames:
                if fileName != displayFileNameJPG:
                    if fileName != displayFileNamePDF:
                        print('Extra file:     ' + os.path.join(contentFolderPath,
                                                                displayFolderName,
                                                                fileName))
input('Press ENTER to exit.')
