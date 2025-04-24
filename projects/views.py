from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
import tempfile
from django.http import HttpResponse
from weasyprint import HTML
from django.conf import settings
from django.contrib import messages
# Create your views here.




def index(request):
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Message from {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            send_mail(subject, message, sender, [settings.EMAIL_HOST_USER])
            
            messages.success(request, "Your message has been sent successfully!")
            form = ContactForm()  # Clear the form after successful send

    return render(request, 'projects/project/index.html', { 'projects': projects, 'form': form })



def details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project/details.html', {'project': project})

def resume_view(request):
    return render(request, 'projects/resume.html')




def generate_resume_pdf(request):
    try:
        html_string = render_to_string("resume.html", {})
        response = HttpResponse(content_type="application/pdf")
        response['Content-Disposition'] = 'inline; filename="resume.pdf"'
        with tempfile.NamedTemporaryFile(delete=True, suffix=".pdf") as output:
            HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(output.name)
            output.seek(0)
            response.write(output.read())
        return response
    except Exception as e:
        return HttpResponse(f"An error occurred while generating the PDF: {e}", status=500)







    




    