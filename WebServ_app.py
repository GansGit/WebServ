import bottle
import MySQL
from bottle import  route, run, static_file, redirect, auth_basic, request, template


# @route('/')
# def default():
#        redirect('/login')
# @route('/login')
# def serve_homepage():
#       return static_file('login.html', root = './')
@route ('/main')
def main_page():
     return static_file('main.html', root='./')

GetAllAutors()
#################
run(host='localhost', port=80, debug=True, reloader=True)

# test = {
#     'protocol': ['p1','p2','p3'],
#     'service':['s1','s2','s3'],
#     'plugin': ['p1','p2','p3'],
#     'result':[1,0,1]
# }

# @route('/page1')
# def serve_homepage():
#     return template('disp_table',root="./" ,rows=test)
