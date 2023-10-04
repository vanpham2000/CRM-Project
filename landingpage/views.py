from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import MyAccountModel, CustomerAccount
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from .filter import CustomerAccountFilter # Import your filter class


# Create your views here.

def AccessDenied(request):
    return render(request, "access.html")

def Error(request, catch_all):
    return render(request, "error.html")

@login_required
def CustomerAccounts(request,user_identifier):
    user = get_object_or_404(MyAccountModel, userID=user_identifier)
    # url = reverse('customeraccount', userID=[user_identifier])
    role = user.role
    if role =="Manager":
        all_customer_accounts = CustomerAccount.objects.all()
        customer_filter = CustomerAccountFilter(request.GET, queryset=all_customer_accounts)
        paginator = Paginator(customer_filter.qs, 10)  # Show 10 customer accounts per page

        # Create a list of dictionaries to store the data for each customer account
        customer_data_list = []
        for account in all_customer_accounts:
            customer_data = {
                'accountID': account.accountID,
                'firstname': account.firstname,
                'lastname': account.lastname,
                'email': account.email,
                'phone_number': account.phone_number,
                'address': account.address,
                'state': account.state,
                'city': account.city,
                'zipcode': account.zipcode,
                'birthdate': account.birthdate,
                'created_date': account.created_date,
            }
            customer_data_list.append(customer_data)

            page = request.GET.get('page')
            customers = paginator.get_page(page)

        context = {
            'filter': customer_filter,
            'customer_data_list': customer_data_list,
        }

        return render(request, 'customeraccount.html', context)
    else:
        return render(request, 'customeraccount.html', {})

def customer_search(request):
    customer_list = CustomerAccount.objects.all()
    customer_filter = CustomerAccountFilter(request.GET, queryset=customer_list)

    paginator = Paginator(customer_filter.qs, 10)  # Show 10 customer accounts per page

    page = request.GET.get('page')
    customers = paginator.get_page(page)

    context = {
        'filter': customer_filter,
        'customers': customers,
    }

    return render(request, 'customer_search.html', context)

@login_required
def welcome(request, user_identifier):
    # Get the user's own ID from the session (if it exists)
    user_id_in_session = request.session.get('access')

    # Retrieve the user from the database based on the user identifier
    user = get_object_or_404(MyAccountModel, userID=user_identifier)
    if user_id_in_session and user_id_in_session != user.userID:
        # Redirect to an "access denied" page or handle it in your preferred way
        return redirect('accessdenied')

    # Store the user's ID in the session only if it doesn't exist
    if not user_id_in_session:
        request.session['access'] = user.userID
    #
    # if user.role == 'Manager':
    #     # Redirect to the customeraccount page with the user identifier as a parameter
    #     return redirect('customeraccount')
    # elif role == 'Marketing':
    #     return redirect('marketing_page')
    # elif role == 'Data Analyze':
    #     return redirect('marketing_page')
    # else:
    #     # Handle other roles or display an error message
    #     return render(request, 'access.html')

    firstname = user.firstname
    lastname = user.lastname
    role = user.role

    # Render the welcome page with user data
    context = {
        'user_identifier': user_identifier,
        'firstname': firstname,
        'lastname': lastname,
        'role': role,
    }
    return render(request, 'yourpage.html', context)

def nav(request):
    return render(request, "WelcomePage.html",{})


def VerifyAccount(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = MyAccountModel.objects.get(email=email)
            if check_password(password,user.password):
                return redirect('welcome', user_identifier=user.userID)
                request.session['access'] = user.userID
            else:
                return render(request, 'index.html',  {'error_message': 'Invalid email or password'})
        except MyAccountModel.DoesNotExist:
            return render(request, 'index.html', {'error_message': 'Invalid email or password'})

    else:
        return render(request, "index.html")



def register(request):
    # Calculate the next available user ID
    latest_user = MyAccountModel.objects.order_by('-userID').first()
    if latest_user:
        latest_id = int(latest_user.userID.split('-')[1])
        next_user_id = f'USER-{latest_id + 1}'
    else:
        next_user_id = 'USER-1'

    if request.method == 'POST':
        # Get form data from POST request
        email = request.POST.get("email"),
        firstname = request.POST.get("firstname"),
        lastname = request.POST.get("lastname"),
        password = request.POST.get("password")  # Get the user-entered password
        company = request.POST.get("company")
        # Hash the password using Django's make_password function
        hashed_password = make_password(password)

        # Create a new user with the hashed password
        user = MyAccountModel.objects.create(
            userID=next_user_id,
            email=email[0],
            firstname=firstname[0],
            lastname=lastname[0],
            password=hashed_password,  # Save the hashed password
            company=company[0]
        )

        # Save the user instance to the database
        user.save()

        # Optionally, you can log the user in after registration
        # (requires proper authentication settings)
        # Example: login(request, user)

        # Redirect to a success page or home page
        return redirect('/login')

    # If the request method is GET, render the registration form
    return render(request, 'registerform.html')






