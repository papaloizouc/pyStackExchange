from scrapper import Scrapper
import ui
from model import Model

from PyQt4 import QtGui
import signal
import sys
import threading

EMAIL = ""
PASSWORD = ""


def run_scrapper(scrapper:Scrapper,model:Model):
    #scrapper.model = model
    #scrapper.login(EMAIL, PASSWORD)
    #scrapper.search_tag("python")
    x=[{'title': 'python getting a list from', 'time': '11 mins ago', 'views': 23, 'answers': 2, 'tags': ['python', 'python-3.x'], 'user': {'reputation': 51.0, 'name': 'Michael C'}, 'votes': 0, 'id': 'question-summary-19472748', 'link': 'http://www.stackoverflow.com/questions/19472748/python-getting-a-list-from'}, {'title': 'Text is replaced at end of file?', 'time': '13 mins ago', 'views': 11, 'answers': 0, 'tags': ['python', 'string', 'file', 'replace'], 'user': {'reputation': 48.0, 'name': 'user1871869'}, 'votes': 0, 'id': 'question-summary-19472723', 'link': 'http://www.stackoverflow.com/questions/19472723/text-is-replaced-at-end-of-file'}, {'title': 'how to improve so that the output plot is changed as I move my slider(a parameter of function) in a GUI program of python?', 'time': '16 mins ago', 'views': 3, 'answers': 0, 'tags': ['python', 'user-interface', 'matplotlib', 'scipy', 'signals'], 'user': {'reputation': 8.0, 'name': 'Guangyue He'}, 'votes': 0, 'id': 'question-summary-19472706', 'link': 'http://www.stackoverflow.com/questions/19472706/how-to-improve-so-that-the-output-plot-is-changed-as-i-move-my-slidera-paramete'}, {'title': 'cv2.convexityDefects error. Python ubuntu 12.04', 'time': '34 mins ago', 'views': 7, 'answers': 1, 'tags': ['python', 'opencv', 'ubuntu'], 'user': {'reputation': 1.0, 'name': 'user2899034'}, 'votes': 0, 'id': 'question-summary-19472603', 'link': 'http://www.stackoverflow.com/questions/19472603/cv2-convexitydefects-error-python-ubuntu-12-04'}, {'title': "python read_fwf error: 'dtype is not supported with python-fwf parser'", 'time': '40 mins ago', 'views': 5, 'answers': 0, 'tags': ['python', 'parsing', 'pandas'], 'user': {'reputation': 1.0, 'name': 'user2899013'}, 'votes': 0, 'id': 'question-summary-19472566', 'link': 'http://www.stackoverflow.com/questions/19472566/python-read-fwf-error-dtype-is-not-supported-with-python-fwf-parser'}, {'title': 'Returning (Passing Around) A Function Call in Python/Tornado?', 'time': '42 mins ago', 'views': 8, 'answers': 0, 'tags': ['python', 'mvc', 'tornado'], 'user': {'reputation': 85.0, 'name': 'SwiftCore'}, 'votes': 0, 'id': 'question-summary-19472563', 'link': 'http://www.stackoverflow.com/questions/19472563/returning-passing-around-a-function-call-in-python-tornado'}, {'title': 'else statements always run', 'time': '44 mins ago', 'views': 34, 'answers': 1, 'tags': ['python', 'if-statement', 'statements'], 'user': {'reputation': 1.0, 'name': 'user2898847'}, 'votes': -2, 'id': 'question-summary-19472548', 'link': 'http://www.stackoverflow.com/questions/19472548/else-statements-always-run'}, {'title': 'Representing graphs (data structure) in Python', 'time': '48 mins ago', 'views': 27, 'answers': 1, 'tags': ['python', 'data-structures'], 'user': {'reputation': 14.0, 'name': 'Ashish Nitin Patil'}, 'votes': 0, 'id': 'question-summary-19472530', 'link': 'http://www.stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python'}, {'title': 'Scrapy and CSV Noobie help Please', 'time': '50 mins ago', 'views': 9, 'answers': 0, 'tags': ['python', 'csv', 'xpath', 'scrapy'], 'user': {'reputation': 6.0, 'name': 'user2898989'}, 'votes': 1, 'id': 'question-summary-19472522', 'link': 'http://www.stackoverflow.com/questions/19472522/scrapy-and-csv-noobie-help-please'}, {'title': 'Blender 2.6: Select object through Python', 'time': '53 mins ago', 'views': 9, 'answers': 2, 'tags': ['python', 'blender', 'bpy'], 'user': {'reputation': 124.0, 'name': 'Joseph'}, 'votes': 0, 'id': 'question-summary-19472499', 'link': 'http://www.stackoverflow.com/questions/19472499/blender-2-6-select-object-through-python'}, {'title': 'In python, can one iterate through large text files using buffers and get the correct file position at the same time?', 'time': '1 hour ago', 'views': 29, 'answers': 1, 'tags': ['python', 'file-io'], 'user': {'reputation': 149.0, 'name': 'Roun'}, 'votes': 0, 'id': 'question-summary-19472441', 'link': 'http://www.stackoverflow.com/questions/19472441/in-python-can-one-iterate-through-large-text-files-using-buffers-and-get-the-co'}, {'title': 'convert JPG to txt causes change in file size in python', 'time': '1 hour ago', 'views': 14, 'answers': 1, 'tags': ['python', 'csv', 'jpeg'], 'user': {'reputation': 1.0, 'name': 'user2639876'}, 'votes': -1, 'id': 'question-summary-19472409', 'link': 'http://www.stackoverflow.com/questions/19472409/convert-jpg-to-txt-causes-change-in-file-size-in-python'}, {'title': 'Convert all photos in a folder to jpg using Python OpenCV', 'time': '1 hour ago', 'views': 15, 'answers': 0, 'tags': ['python', 'opencv'], 'user': {'reputation': 4.0, 'name': 'RAUSHAN RAJ'}, 'votes': -1, 'id': 'question-summary-19472289', 'link': 'http://www.stackoverflow.com/questions/19472289/convert-all-photos-in-a-folder-to-jpg-using-python-opencv'}, {'title': 'Python get return value on else statement, default variable equivalent to Perl $_', 'time': '1 hour ago', 'views': 32, 'answers': 2, 'tags': ['python', 'return-value'], 'user': {'reputation': 215.0, 'name': 'Gregg Leventhal'}, 'votes': -1, 'id': 'question-summary-19472286', 'link': 'http://www.stackoverflow.com/questions/19472286/python-get-return-value-on-else-statement-default-variable-equivalent-to-perl'}, {'title': 'Serial Hexa dialog (python code to C++/QT 5.0)', 'time': '1 hour ago', 'views': 10, 'answers': 1, 'tags': ['c++', 'python', 'qt'], 'user': {'reputation': 25.0, 'name': 'Gilles Grandguillaume'}, 'votes': 0, 'id': 'question-summary-19472278', 'link': 'http://www.stackoverflow.com/questions/19472278/serial-hexa-dialog-python-code-to-c-qt-5-0'}, {'title': 'Need insight on this piece of Python', 'time': '1 hour ago', 'views': 33, 'answers': 1, 'tags': ['python', 'sockets', 'dns', 'recv'], 'user': {'reputation': 45.0, 'name': 'Austin Burk'}, 'votes': 2, 'id': 'question-summary-19472241', 'link': 'http://www.stackoverflow.com/questions/19472241/need-insight-on-this-piece-of-python'}, {'title': 'How do i sort a lot of lists to get a top 10 in python?', 'time': '1 hour ago', 'views': 57, 'answers': 3, 'tags': ['python', 'list', 'order'], 'user': {'reputation': 34.0, 'name': 'Saelyth'}, 'votes': 0, 'id': 'question-summary-19472225', 'link': 'http://www.stackoverflow.com/questions/19472225/how-do-i-sort-a-lot-of-lists-to-get-a-top-10-in-python'}, {'title': 'How to change a list outside function without a = function(a,b)?', 'time': '1 hour ago', 'views': 28, 'answers': 1, 'tags': ['python', 'function', 'return'], 'user': {'reputation': 1.0, 'name': 'user2898980'}, 'votes': 0, 'id': 'question-summary-19472224', 'link': 'http://www.stackoverflow.com/questions/19472224/how-to-change-a-list-outside-function-without-a-functiona-b'}, {'title': 'What is the fastest way to test whether logged in or not when use python to login to a website?', 'time': '1 hour ago', 'views': 13, 'answers': 0, 'tags': ['python', 'http', 'session', 'login', 'urllib2'], 'user': {'reputation': 23.0, 'name': 'CGP'}, 'votes': -1, 'id': 'question-summary-19472177', 'link': 'http://www.stackoverflow.com/questions/19472177/what-is-the-fastest-way-to-test-whether-logged-in-or-not-when-use-python-to-logi'}, {'title': 'Can not import Pygame', 'time': '1 hour ago', 'views': 25, 'answers': 3, 'tags': ['python', 'pygame'], 'user': {'reputation': 15.0, 'name': 'user163505'}, 'votes': 0, 'id': 'question-summary-19472141', 'link': 'http://www.stackoverflow.com/questions/19472141/can-not-import-pygame'}, {'title': "Tic Tac Cover up!! Can't get the program to work correctly", 'time': '1 hour ago', 'views': 46, 'answers': 1, 'tags': ['python', 'python-2.7'], 'user': {'reputation': 3.0, 'name': 'Andy Eggl'}, 'votes': 0, 'id': 'question-summary-19472126', 'link': 'http://www.stackoverflow.com/questions/19472126/tic-tac-cover-up-cant-get-the-program-to-work-correctly'}, {'title': 'Check if a date exists in a pandas dataframe', 'time': '1 hour ago', 'views': 13, 'answers': 3, 'tags': ['python', 'pandas'], 'user': {'reputation': 84.0, 'name': 'Ahdee'}, 'votes': -1, 'id': 'question-summary-19472113', 'link': 'http://www.stackoverflow.com/questions/19472113/check-if-a-date-exists-in-a-pandas-dataframe'}, {'title': 'How do I make mezzanine user email non-updatable?', 'time': '2 hours ago', 'views': 5, 'answers': 1, 'tags': ['python', 'django', 'django-models', 'mezzanine'], 'user': {'reputation': 632.0, 'name': "Victor 'Chris' Cabral"}, 'votes': 0, 'id': 'question-summary-19472079', 'link': 'http://www.stackoverflow.com/questions/19472079/how-do-i-make-mezzanine-user-email-non-updatable'}, {'title': 'Tornado Not Interpreting URL', 'time': '2 hours ago', 'views': 7, 'answers': 0, 'tags': ['python', 'regex', 'url', 'tornado'], 'user': {'reputation': 124.0, 'name': 'Will'}, 'votes': 0, 'id': 'question-summary-19472056', 'link': 'http://www.stackoverflow.com/questions/19472056/tornado-not-interpreting-url'}, {'title': 'Searching and sorting in Python', 'time': '2 hours ago', 'views': 44, 'answers': 1, 'tags': ['python', 'regex', 'loops', 'if-statement', 'for-loop'], 'user': {'reputation': 1.0, 'name': 'Miniminion'}, 'votes': 0, 'id': 'question-summary-19472046', 'link': 'http://www.stackoverflow.com/questions/19472046/searching-and-sorting-in-python'}, {'title': 'How can I access Django Admin Site on Amazon EC2 Instance?', 'time': '2 hours ago', 'views': 10, 'answers': 1, 'tags': ['python', 'django', 'web', 'amazon-ec2', 'ubuntu-12.04'], 'user': {'reputation': 3.0, 'name': 'user2898916'}, 'votes': 0, 'id': 'question-summary-19472012', 'link': 'http://www.stackoverflow.com/questions/19472012/how-can-i-access-django-admin-site-on-amazon-ec2-instance'}, {'title': 'Drag-and-Drop multiple files in Python (Windows)', 'time': '2 hours ago', 'views': 13, 'answers': 0, 'tags': ['python', 'drag-and-drop', 'tkinter', 'whitespace', 'multiple-files'], 'user': {'reputation': 11.0, 'name': 'Riccardo'}, 'votes': 1, 'id': 'question-summary-19471987', 'link': 'http://www.stackoverflow.com/questions/19471987/drag-and-drop-multiple-files-in-python-windows'}, {'title': 'How to avoid “Permission denied” when using pip with virtualenv', 'time': '2 hours ago', 'views': 14, 'answers': 1, 'tags': ['python', 'virtualenv', 'pip'], 'user': {'reputation': 7570.0, 'name': 'MainMa'}, 'votes': 1, 'id': 'question-summary-19471972', 'link': 'http://www.stackoverflow.com/questions/19471972/how-to-avoid-permission-denied-when-using-pip-with-virtualenv'}, {'title': 'Tulip/asyncIO: why not all calls be async and specify when things should be synchronous?', 'time': '2 hours ago', 'views': 13, 'answers': 1, 'tags': ['python', 'asynchronous', 'python-3.x'], 'user': {'reputation': 192.0, 'name': 'Gabriel'}, 'votes': 1, 'id': 'question-summary-19471967', 'link': 'http://www.stackoverflow.com/questions/19471967/tulip-asyncio-why-not-all-calls-be-async-and-specify-when-things-should-be-sync'}, {'title': 'Configuring Sympy startup display output', 'time': '2 hours ago', 'views': 9, 'answers': 0, 'tags': ['python', 'python-3.x', 'ipython', 'sympy'], 'user': {'reputation': 3524.0, 'name': 'helloworld922'}, 'votes': 1, 'id': 'question-summary-19471961', 'link': 'http://www.stackoverflow.com/questions/19471961/configuring-sympy-startup-display-output'}, {'title': "Removing '\\n' from a string sends additional characters to front of line", 'time': '2 hours ago', 'views': 38, 'answers': 3, 'tags': ['python', 'python-3.x'], 'user': {'reputation': 3.0, 'name': 'Emily Rose Salmon'}, 'votes': 0, 'id': 'question-summary-19471866', 'link': 'http://www.stackoverflow.com/questions/19471866/removing-n-from-a-string-sends-additional-characters-to-front-of-line'}, {'title': 'Coursera Vs EDX Vs Lynda Courses', 'time': '2 hours ago', 'views': 22, 'answers': 1, 'tags': ['java', 'python', 'architecture', 'software-engineering'], 'user': {'reputation': 1.0, 'name': 'user2898879'}, 'votes': -2, 'id': 'question-summary-19471849', 'link': 'http://www.stackoverflow.com/questions/19471849/coursera-vs-edx-vs-lynda-courses'}, {'title': 'Connect to a webSocket and maintain a connection', 'time': '2 hours ago', 'views': 13, 'answers': 0, 'tags': ['python'], 'user': {'reputation': 38.0, 'name': 'ruler'}, 'votes': 0, 'id': 'question-summary-19471846', 'link': 'http://www.stackoverflow.com/questions/19471846/connect-to-a-websocket-and-maintain-a-connection'}, {'title': 'Construct image from fabric.js json on python server', 'time': '2 hours ago', 'views': 8, 'answers': 0, 'tags': ['javascript', 'python', 'node.js', 'canvas', 'fabricjs'], 'user': {'reputation': 406.0, 'name': 'student'}, 'votes': 0, 'id': 'question-summary-19471708', 'link': 'http://www.stackoverflow.com/questions/19471708/construct-image-from-fabric-js-json-on-python-server'}, {'title': 'python file.seek() with os.SEEK_CUR vs os.SEEK_SET', 'time': '3 hours ago', 'views': 19, 'answers': 1, 'tags': ['python', 'file', 'python-2.7', 'file-io'], 'user': {'reputation': 201.0, 'name': 'Walkman'}, 'votes': 0, 'id': 'question-summary-19471618', 'link': 'http://www.stackoverflow.com/questions/19471618/python-file-seek-with-os-seek-cur-vs-os-seek-set'}, {'title': 'Editing Key value in dictionary of a csv in order to perform the following', 'time': '3 hours ago', 'views': 36, 'answers': 0, 'tags': ['python', 'python-2.7', 'csv', 'dictionary', 'key'], 'user': {'reputation': 453.0, 'name': 'AEA'}, 'votes': -1, 'id': 'question-summary-19471534', 'link': 'http://www.stackoverflow.com/questions/19471534/editing-key-value-in-dictionary-of-a-csv-in-order-to-perform-the-following'}, {'title': 'how to implement this in django - back button - keep data in request', 'time': '3 hours ago', 'views': 28, 'answers': 1, 'tags': ['javascript', 'jquery', 'python', 'django'], 'user': {'reputation': 1985.0, 'name': 'doniyor'}, 'votes': 0, 'id': 'question-summary-19471344', 'link': 'http://www.stackoverflow.com/questions/19471344/how-to-implement-this-in-django-back-button-keep-data-in-request'}, {'title': 'Python WxWidgets - how to have static text labels appear on top of gradient painted panel', 'time': '3 hours ago', 'views': 10, 'answers': 1, 'tags': ['python', 'wxpython', 'wxwidgets'], 'user': {'reputation': 1753.0, 'name': 'fred basset'}, 'votes': 0, 'id': 'question-summary-19471297', 'link': 'http://www.stackoverflow.com/questions/19471297/python-wxwidgets-how-to-have-static-text-labels-appear-on-top-of-gradient-pain'}, {'title': 'Creating a dictionary in Python [on hold]', 'time': '3 hours ago', 'views': 40, 'answers': 0, 'tags': ['python', 'dictionary'], 'user': {'reputation': 1.0, 'name': 'user2898784'}, 'votes': -5, 'id': 'question-summary-19471277', 'link': 'http://www.stackoverflow.com/questions/19471277/creating-a-dictionary-in-python'}, {'title': 'how can i get the last updatet item in a feed?', 'time': '3 hours ago', 'views': 13, 'answers': 0, 'tags': ['python', 'rss', 'feedparser'], 'user': {'reputation': 1.0, 'name': 'DirectorX'}, 'votes': -1, 'id': 'question-summary-19471239', 'link': 'http://www.stackoverflow.com/questions/19471239/how-can-i-get-the-last-updatet-item-in-a-feed'}, {'title': 'py.test raising ImproperlyConfigured error', 'time': '3 hours ago', 'views': 12, 'answers': 0, 'tags': ['python', 'django', 'django-settings', 'pytest'], 'user': {'reputation': 38.0, 'name': 'aphex'}, 'votes': 0, 'id': 'question-summary-19471137', 'link': 'http://www.stackoverflow.com/questions/19471137/py-test-raising-improperlyconfigured-error'}, {'title': 'Exclude list of words when reading a file', 'time': '3 hours ago', 'views': 34, 'answers': 1, 'tags': ['python', 'regex', 'list', 'exclude'], 'user': {'reputation': 6.0, 'name': 'alexponline'}, 'votes': 1, 'id': 'question-summary-19471136', 'link': 'http://www.stackoverflow.com/questions/19471136/exclude-list-of-words-when-reading-a-file'}, {'title': 'Reading files using different threads', 'time': '3 hours ago', 'views': 25, 'answers': 2, 'tags': ['python', 'multithreading'], 'user': {'reputation': 3065.0, 'name': 'iJay'}, 'votes': 1, 'id': 'question-summary-19471122', 'link': 'http://www.stackoverflow.com/questions/19471122/reading-files-using-different-threads'}, {'title': 'Selenium WebDriver - Disable Native Events (Enable Synthesized Events)', 'time': '4 hours ago', 'views': 3, 'answers': 1, 'tags': ['python', 'firefox', 'selenium', 'selenium-webdriver'], 'user': {'reputation': 12.2, 'name': 'Corey Goldberg'}, 'votes': 0, 'id': 'question-summary-19471102', 'link': 'http://www.stackoverflow.com/questions/19471102/selenium-webdriver-disable-native-events-enable-synthesized-events'}, {'title': 'Warping an image using roll, pitch, and yaw', 'time': '4 hours ago', 'views': 16, 'answers': 0, 'tags': ['python', 'image', 'opencv', 'rotation', 'pitch'], 'user': {'reputation': 8.0, 'name': 'Sinjin Forde'}, 'votes': 0, 'id': 'question-summary-19470955', 'link': 'http://www.stackoverflow.com/questions/19470955/warping-an-image-using-roll-pitch-and-yaw'}, {'title': "Why isn't this code repeating? Python 3.3", 'time': '4 hours ago', 'views': 61, 'answers': 3, 'tags': ['python'], 'user': {'reputation': 9.0, 'name': 'PixelPuppet'}, 'votes': -1, 'id': 'question-summary-19470932', 'link': 'http://www.stackoverflow.com/questions/19470932/why-isnt-this-code-repeating-python-3-3'}, {'title': 'In python is it better to have a series of += or to append to a list and then sum?', 'time': '4 hours ago', 'views': 65, 'answers': 5, 'tags': ['python', 'list', 'sum'], 'user': {'reputation': 10.0, 'name': 'egoburnswell'}, 'votes': 0, 'id': 'question-summary-19470862', 'link': 'http://www.stackoverflow.com/questions/19470862/in-python-is-it-better-to-have-a-series-of-or-to-append-to-a-list-and-then-su'}, {'title': 'Function call in all templates', 'time': '4 hours ago', 'views': 36, 'answers': 1, 'tags': ['python', 'django', 'twitter'], 'user': {'reputation': 42.0, 'name': 'Krasimir'}, 'votes': -1, 'id': 'question-summary-19470859', 'link': 'http://www.stackoverflow.com/questions/19470859/function-call-in-all-templates'}, {'title': 'How do I go about customizing Mezzanine-Cartridge shop/product?', 'time': '4 hours ago', 'views': 9, 'answers': 1, 'tags': ['python', 'django', 'mezzanine', 'cartridge'], 'user': {'reputation': 1.0, 'name': 'Novice User'}, 'votes': 0, 'id': 'question-summary-19470805', 'link': 'http://www.stackoverflow.com/questions/19470805/how-do-i-go-about-customizing-mezzanine-cartridge-shop-product'}, {'title': 'Sockets packet forwarding', 'time': '4 hours ago', 'views': 17, 'answers': 1, 'tags': ['c#', 'python', 'sockets'], 'user': {'reputation': 46.0, 'name': 'your_average_programmer'}, 'votes': 0, 'id': 'question-summary-19470798', 'link': 'http://www.stackoverflow.com/questions/19470798/sockets-packet-forwarding'}]
    model.questions = x

def init_app() -> QtGui.QApplication:
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    #app.setFont(QtGui.QFont("Monospace", 13))
    return app


if __name__ == '__main__':
    app = init_app()

    model = Model()
    view = ui.View(model)
    scrapper = Scrapper(model,view)
    view.register_exit_callback(scrapper.exit_)

    thread = threading.Thread(target=run_scrapper, args=(scrapper,model))
    thread.daemon = True
    thread.start()

    scrapper.exit_(app.exec_())

