from django.http import HttpResponse
from django.shortcuts import render
from .forms import AdvancedSearchForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Book, Member, Reservation
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as palm


def index(request):
    return HttpResponse("Hello, world. You're at the LibraLoom index.")


@login_required
def home(request):
    # Fetch some book details for display on the homepage
    pass
    books = Book.objects.all()[:5]  # Adjust this as needed
    return render(request, 'LibraLoom/home.html', {'books': books})

@login_required
def contact_us(request):
    # Create a contact form and handle submissions
    if request.method == 'POST':
        # Handle form submission
        # You may need to create a Contact model and form for this
        pass
    return render(request, 'LibraLoom/contact_us.html')

@login_required
def advanced_search(request):
    books = []
    if request.method == 'POST':
        form = AdvancedSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            category = form.cleaned_data.get('category')
            books = Book.objects.filter(
                title__icontains=title,
                author__icontains=author,
            )
            if category:
                books = books.filter(category=category)

    else:
        form = AdvancedSearchForm()

    return render(request, 'LibraLoom/advance_search.html', {'form': form, 'books': books})

@login_required
def anybook_pdf(request):
    # Implement anybook-pdf functionality using an external API
    # You can use requests library to fetch data from the API
    # Process the API response and render the data in your template
    return render(request, 'LibraLoom/anybook.html')

@login_required
def profile(request):
    # Implement the profile view to display user information, reading history, reservations, etc.
    # You will need to fetch and pass the user's data to the template
    pass
    return render(request, 'LibraLoom/profile.html')


@login_required
def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    is_available = book.book_Availability
    user = request.user  # Assuming you are using Django's built-in authentication

    return render(request, 'LibraLoom/book_details.html', {'book': book, 'is_available': is_available, 'user': user})


@login_required
def reserve_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    member, created = Member.objects.get_or_create(user=request.user)

    # Check if the book is already reserved by the user
    if Reservation.objects.filter(book=book, member=member, status="Active").exists():
        return HttpResponse("You have already reserved this book")

    # Create a new reservation
    reservation = Reservation(book=book, member=member, status="Active")
    reservation.save()

    # Redirect to the home page after a successful reservation
    return redirect('home')


@login_required
def reserve_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        member = Member.objects.get(user=request.user)

        # Check if the book is already reserved by the user
        if Reservation.objects.filter(book=book, member=member, status="Active").exists():
            return HttpResponse("You have already reserved this book")

        # Create a new reservation
        reservation = Reservation(book=book, member=member, status="Active")
        reservation.save()

        # Redirect to the home page after a successful reservation
        return redirect('home')
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    except Member.DoesNotExist:
        return HttpResponse("Member does not exist")


@login_required
def protected_view(request):
    # This view will only be accessible to authenticated users
    pass

def return_book(request):
    return None

from django.shortcuts import render
from libgen_api import LibgenSearch

def search_book(request):
    if request.method == "POST":
        search_query = request.POST.get("search_query")
        # Perform a search using libgen-api
        libgen = LibgenSearch()
        results = libgen.search_title(search_query)

        # You can process the results and display them in your template
        return render(request, "LibraLoom/anybook.html", {"results": results})

    return render(request, "LibraLoom/anybook.html")


from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email to your organization or the appropriate recipient
            send_mail(
                f'Contact from {name}',
                message,
                email,
                ['chamith.2senadeera@gmail.com'],  # Replace with your email address
                fail_silently=False,
            )

            # Redirect to a contact-us page after submission
            return HttpResponseRedirect('/contact-us/')
    else:
        form = ContactForm()

    return render(request, 'LibraLoom/contact_us.html', {'form': form})

from django.http import JsonResponse
import google.generativeai as palm

palm.configure(api_key='AIzaSyCz69hhXVbj-Pkiot-DtDwF-AdHnC2r4iI')

def generate_summary(request):
    summary = None

    if request.method == 'POST':
        book_name = request.POST['book_name']
        summary_length = request.POST['summary_length']

        model_id = "models/text-bison-001"
        prompt = f"Write a {summary_length} summary about the book '{book_name}'"

        completion = palm.generate_text(
            model=model_id,
            prompt=prompt,
            temperature=0.99,
            max_output_tokens=800,
        )

        summary = completion.result

    return render(request, 'LibraLoom/book_summary.html', {'summary': summary})
