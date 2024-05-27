from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
from .models import Course, Ourpartner, AcademyTestimonial, Aboutpage
from .forms import ContactForm


def index(request):
    course = Course.objects.all()
    partners = Ourpartner.objects.all()
    testimonial = AcademyTestimonial.objects.all()
    return render(request, 'index.html', {'courses': course, 'media_url': settings.MEDIA_URL, 'partners': partners,
                                          'testimonial': testimonial})


def about(request):
    ap = Aboutpage.objects.get(pk=1)
    return render(request, 'about.html', {'aboutpage': ap, 'media_url': settings.MEDIA_URL})


def courses(request):
    course = Course.objects.all()
    return render(request, 'courses.html', {'courses': course, 'media_url': settings.MEDIA_URL})


def contact(request):
    course1 = Course.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact1 = form.cleaned_data['contact']
            course = form.cleaned_data['course']
            print(course);
            message = form.cleaned_data['message']
            context = {'name': name, 'highlightmsg': 'Thank You for contacting us',
                       'message': 'We will contact you soon.'}
            clientrendered_text = render_to_string('email_template.txt', context)
            admincontext = {'name': name, 'message': message, 'email': email, 'contact': contact1, 'course': course}
            adminrendered_text = render_to_string('admin_email_template.txt', admincontext)
            # send_mail(
            #     course,
            #     clientrendered_text,
            #     'hr@workiy.ca', 
            #     [email], 
            # )

            # send_mail(
            #     course,
            #     adminrendered_text,
            #     'hr@workiy.ca',  
            #     ['arul.ramu@workiy.ca'], 
            # )

            return redirect('/success/')

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'media_url': settings.MEDIA_URL, 'form': form, 'courses': course1})


def my_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ContactForm()
    return render(request, 'my_form.html', {'form': form})


def course_detail(request, course_id):
    # Retrieve the course from the database using the course_id
    course = get_object_or_404(Course, pk=course_id)
    if course:
        return render(request, 'course_detail.html', {'c': course, 'media_url': settings.MEDIA_URL})
    else:
        return HttpResponseNotFound("Home page")


def success_view(request):
    return render(request, 'success.html')


def page_not_found(request):
    return render(request, '404.html', {}, status=404)
