# work_with_wav_files
for win10:
	open cmd with root:
		use cmd:
		pip install matplotlib
		pip install scipy
		pip install numpy
		pip install librosa
		pip install pydub
for ubuntu 19_04:
	press ctrl+alt+t(open terminal) :
	sudo apt-get install pip3
		pip3 install matplotlib
		pip3 install scipy
		pip3 install numpy
		pip3 install librosa
		pip3 install pydub
		
soft that i used :
	pycharm
	rhythmbox
soft version i have :
python 3.8

try1.py скрипт конвертирует mp3 to wav
in line >>>13 убрать "#" что бы запустить скрикт

test.py скрипт визаулизурует ачх и записует в файл бпф
in line >>>54 удалите "#"
in line >>>55 удалите "#" для показа всех ачх
in line >>>56 удалите "#" для записи бпф в файл (FFT_side , freqs_side)

winapp2.py скрипт визуализации полностью рабочий но не закончен (не придумал как)

моя программа полностю выполняет ваши требования масовый перебор .wav и вывод ачх или записать бпф
	что бы начать работать с .wav поместите все ваши файлы в дерикторию 'set_a' и воспользуйтесь 'test.py'
	что бы преобразовать .mp3 в .wav поместите .mp3 файлы в 'set_b' (.mp3  будет УДАЛЕН и заменен .wav) и воспользуйтесь 'try1.py'
	ВИЗУАЛИЗАЦИЮ НЕ ДОДЕЛАНА Я НЕ СМОГ
	 
