
from openerp import http
from openerp.http import request
import webbrowser

class website_openacademy(http.Controller):

    @http.route('/hello/world', auth='public')
    def test_controller(self):
        return "Hello World"

    @http.route('/hello/world2', auth='public')
    def test_controller2(self):
        return "<h1><b>Hello World</b></h1>"

    @http.route('/hello/world3', auth='user')
    def test_controller3(self):
        return "<b>Hello, %s</b>"%(request.env.user.name)


     # Website Pages
    @http.route('/simple_page', auth='user', website=True)
    def simple_page(self):
        return request.website.render("openacademy.simple_page", {})
       
#     @http.route('/simple_page', auth='user', website=True)
#     def simple_page(self):
#         return webbrowser.open_new('http://www.google.com')

    @http.route('/dynamic_page', auth='user', website=True)
    def dynamic_page(self):
        return request.website.render("openacademy.dynamic_page", {'user':request.env.user,'array':[1,2,3,4],'my_func':self.test})

    def test(self,var1):
        print "var1------------",var1
        return "Return test :::"
    
    @http.route('/simple', type='http', auth='user', methods=['POST'], website=True)
    def simple_page1(self):
        return request.website.render('index.html')
    
    @http.route('/openacademy/course', auth='user', website=True)
    def courses(self):
        courses = request.env['openacademy.course'].search([])
        return request.website.render("openacademy.openacademy_course", {'courses':courses})

    @http.route("/openacademy/course/<model('openacademy.course'):course>", auth='user', website=True)
    def courses_detail(self, course):
        return request.website.render("openacademy.openacademy_courses_detail", {'course':course})

