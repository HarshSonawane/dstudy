from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail

from institute.models import College, University
from educourse.models import EduCourse, Subject, QuetionPaper, ModelAnswerPaper, Curriculam
from .forms import ContactForm
from contact.models import Contact


def index(request, *args, **kwargs):
    return render(request, "pages/index.html", {})

def help(request, *args, **kwargs):
    return render(request, "pages/help.html", {})

def about(request, *args, **kwargs):
    return render(request, "pages/about.html", {})

def services(request, *args, **kwargs):
    return render(request, "pages/services.html", {})

def careers(request, *args, **kwargs):
    return render(request, "pages/careers.html", {})

def seminars(request, *args, **kwargs):
    return render(request, "pages/seminars.html", {})

def workshops(request, *args, **kwargs):
    return render(request, "pages/workshops.html", {})

def terms(request, *args, **kwargs):
    return render(request, "pages/terms.html", {})

def privacy(request, *args, **kwargs):
    return render(request, "pages/privacy.html", {})

def contact(request, *args, **kwargs):
    return render(request, "pages/contact.html", {})

def enquiry(request, *args, **kwargs):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        name    = request.POST['name']
        email   = request.POST['email']
        subject = request.POST['subject']
        phone   = request.POST['phone']
        type    = request.POST['type']
        message = request.POST['message']

        contact = Contact(user_id=user_id, name=name, email=email, subject=subject, phone=phone, type=type, message=message)

        contact.save()

        msg = 'New Enquiry by:  Name ' + name + 'Email :' + email + 'Phone :' + phone + 'Subject :' + subject + 'Thank you'

        datatuple = (
                    ('Enquiry @ Dstudy by Dream Designers', 'Thank You for your enquiry, dstudy will get in your touch as soon as possible. Regards, Dstudy Admin & Dream Designers.', 'ddsi.dstudy@gmail.com', [email]),
                    ('Enquiry @ Dstudy by Dream Designers', '-' + msg +'-', 'ddsi.dstudy@gmail.com', ['designweb.dds@gmail.com', 'sonawanehvs@gmail.com']),
        )
        send_mass_mail(datatuple)

        messages.success(request, 'Request submited successfully, we will be in touch with you soon')

        return render(request, "pages/contact.html", {})


class CollegeListView(ListView):
    model = College
    template_name = "pages/colleges.html"
    context_object_name = 'colleges'
    paginate_by = 10
    queryset = College.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(CollegeListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *srgs, **kwargs):
        request = self.request
        return College.objects.all()

class CollegeDetailSlugView(DetailView):
    queryset = College.objects.all()
    template_name = "college_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CollegeDetailSlugView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = College.objects.get(slug=slug)
        except College.DoesNotExist:
            raise Http404("Not found..")
        except College.MultipleObjectsReturned:
            qs = College.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance

class UniversityListView(ListView):
    model = University
    template_name = "pages/universities.html"
    context_object_name = 'universities'
    paginate_by = 10
    queryset = College.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(UniversityListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *srgs, **kwargs):
        request = self.request
        return University.objects.all()
    
class UniversityDetailSlugView(DetailView):
    queryset = University.objects.all()
    template_name = "university_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UniversityDetailSlugView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = University.objects.get(slug=slug)
        except University.DoesNotExist:
            raise Http404("Not found..")
        except University.MultipleObjectsReturned:
            qs = University.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance

class EduCourseListView(ListView):
    model = EduCourse
    template_name = "pages/courses.html"
    context_object_name = 'courses'
    paginate_by = 10
    queryset = EduCourse.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(EduCourseListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *srgs, **kwargs):
        request = self.request
        return EduCourse.objects.all()

class SubjectListView(ListView):
    model = Subject
    template_name = "pages/subjects.html"
    context_object_name = 'subjects'
    paginate_by = 10
    queryset = Subject.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(SubjectListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *srgs, **kwargs):
        request = self.request
        return Subject.objects.all()

class QuetionPaperListView(ListView):
    model = QuetionPaper
    template_name = "pages/quetionpapers.html"
    context_object_name = 'quetionpapers'
    paginate_by = 10
    queryset = QuetionPaper.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(QuetionPaperListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *srgs, **kwargs):
        request = self.request
        return QuetionPaper.objects.all()

class ModelAnswerPaperListView(ListView):
    model = ModelAnswerPaper
    template_name = "pages/modelanswerpaper.html"
    context_object_name = 'modelanswerpapers'
    paginate_by = 10
    queryset = ModelAnswerPaper.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ModelAnswerPaperListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *srgs, **kwargs):
        request = self.request
        return ModelAnswerPaper.objects.all()

class CurriculamListView(ListView):
    model = Curriculam
    template_name = "pages/curriculam.html"
    context_object_name = 'curriculams'
    paginate_by = 10
    queryset = Curriculam.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(CurriculamListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *srgs, **kwargs):
        request = self.request
        return Curriculam.objects.all()