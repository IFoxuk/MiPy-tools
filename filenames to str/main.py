import os, configparser

## Глобальные переменные по умолчанию
toolsPath = 'C:\\Users\\user\Documents\MiPy tools'
settingsPath = 'C:\\Users\\user\Documents\MiPy tools\settings.ini'
settingsErr = True

def output(outputInConsole, outputInFile, outputPath):
    config = configparser.ConfigParser()
    print('Введите полный путь каталога, список объектов которого вы хотите вывести:')
    outputDir = input()
    fileNames = os.listdir(outputDir)
    if outputInConsole == True:
        print('\nОбъекты каталога:')
        ## Вывод имён файлов построчно
        for i in fileNames:
            print (i)
    if outputInFile == True:
        with open(outputPath, 'w') as outputFile:
            for i in fileNames:
                outputFile.write(i+'\n')
        print('\nСписок объектов каталота сохранен в:', outputPath)
    if outputInConsole == False and outputInFile == False:
        print('Значения outputinconsole и outputinfile установлены False. \nВывод не осуществлён.')

    

def settings_create():
    '''
    Создание файла настроек и каталога.
    '''
    global settingsErr

    config = configparser.ConfigParser()

    try:
        config['DEFAULT'] = {
            "outputinconsole": "True",
            "outputinfile": "True",
            "outputpath": "C:\\\\Users\\\\user\Documents\MiPy tools\output.txt"
        }
        with open(settingsPath, 'w') as configfile:
                config.write(configfile)
        print('>Файл настроек создан по пути', settingsPath)
    except PermissionError:
        print('>>Не удалось создать файл настроек!\n>>Запустите программу от имени администратора.')
        settingsErr = False
    except:
        try:
            print('>>>Создание каталога MiPy tools.')
            os.mkdir(toolsPath)
            print('>>>Каталог создан по пути', toolsPath)
        except:
            print('>>>Создание каталога не удалось! Неизвестная ошибка.')
            settingsErr = False
    
def main():
    global settingsErr

    config = configparser.ConfigParser()

    ## Проверка файла настроек и считывание переменных
    while settingsErr == True:
        if os.path.exists(settingsPath):
            config.read(settingsPath)
            outputInConsole = config['DEFAULT'].getboolean('outputinconsole')
            outputInFile = config['DEFAULT'].getboolean('outputinfile')
            outputPath = config['DEFAULT']['outputpath']
            settingsErr = False
        else:
            settings_create()
    output(outputInConsole, outputInFile, outputPath)
    

main()
