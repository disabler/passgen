#!/usr/bin/python
# -*- coding: utf-8 -*-

# Импорт компилятора и настройщика
import py2exe
from distutils.core import setup

# Версия готового .exe файла.
# Должна состоять из 4 групп цифр. Например: 1.0.0.0
VER_FILE = 'version.txt'

VER = file(VER_FILE).read().strip()

# Подготовка к сборке
setup(
	# Опции сборки.
	# includes - подключаемые библиотеки
	#            для PyQt4 обязательно надо включать в сборку библиотеку sip
	# bundle_files - собрать все библиотеки в один zip файл
	# compressed - сжать готовый файл
    options = {'py2exe': {"includes":["sip"], 'bundle_files': 1, 'compressed': True}},
    # None - включить library.zip в .exe файл
	zipfile = None,
	# Версия .exe файла
	version = VER,
	# Название .exe файла
	name = 'PassGen2',
	# Описание
	description = 'Password Generator',
    windows = [{
			# Название скрипта для компиляции
            "script":"PassGen.pyw",
			# Пакет иконок приложения
            "icon_resources": [(1, "icons/PassGen.ico")],
			# Исходное имя файла
            "dest_base":"PassGen2",
			# Копирайты
			"copyright":'Copyright (C) diSabler <dsy@dsy.name>',
			# Название компании производителя
			"company_name": 'Disabler Production Lab.'
            }],
)

# The end is near!
