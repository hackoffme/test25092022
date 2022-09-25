git clone https://github.com/hackoffme/test25092022.git .
Скорипровать свой ключ для api в ./conf/bionic-path-363401-5b625865ca8d.json, проверить настройку GOOGLE_API_SETTINGS = BASE_DIR / 'conf/bionic-path-363401-5b625865ca8d.json' в ./test_hh/settings.py
 
Для запуска приложения docker compose up
Докер без nginx, supervisorctl, в дебаг и без ssl

http://you_ip:8000


Скрипт для синхронизации parse_doc.parse. Запускается при старте и по крону. Настройки крон в test_hh.settyngs.py. (Крон под win не будет работать, поэтому запускаем докере)
Приложение singlpage одностраничник




