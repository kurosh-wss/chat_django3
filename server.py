import os
import sys
import webbrowser


try:
    port = sys.argv[1]
except Exception as e:
    port = 8000

try:
    os.system('source /home/kurosh/Desktop/my_portfolio/env/bin/activate')
    os.system("python /home/kurosh/Desktop/my_portfolio/kurosh/manage.py runserver {}".format(port))
    webbrowser.open_new_tab("http://127.0.0.1:{}".format(port))
except Exception as e:
    print(e)