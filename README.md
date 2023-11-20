# LibraLoom 📚

## Project Structure
This repository contains the code for LibraLoom, a Django-based library system designed to streamline book management and user interactions.

## Features

### Home Page 🏠
The central hub of the website, showcasing an intuitive interface for easy navigation and access to various functionalities. 
![home](https://github.com/chamith-Hemisara/LibraLoom_new/assets/147907538/9db59e64-d455-480d-aa5f-b8cde3f4c0c7)


### Social Sign-In Page 🔐
A dedicated page allowing users to log in using their Facebook, Google, and GitHub accounts for authentication. We used django-allauth in here. 
![social](https://github.com/chamith-Hemisara/LibraLoom_new/assets/147907538/58329932-ed8a-42ee-9a38-3416ed918ee4)


### Advanced Search 🔍
A comprehensive search function allowing users to explore the library's catalog by title, author, and category. Additionally, users can check book availability and reserve books if they're in stock.
![Advanced Search ](https://github.com/chamith-Hemisara/LibraLoom_new/assets/147907538/a467396f-be9b-467e-a7c1-648e5854fe61)

### Any Book Details 📖
Access detailed information about specific books and acquire downloadable links. This feature integrates with the Libgen API, providing users with comprehensive book details.

![Any Book Details](https://github.com/chamith-Hemisara/LibraLoom_new/assets/109784789/473f5c38-d063-4c60-a120-ec9e5ebca03e)

![download_link](https://github.com/chamith-Hemisara/LibraLoom_new/assets/129577822/34649ed9-e618-4962-88b2-722b535fb00a)

### Any Book Summary 📝
Leveraging generative AI via the Plam API, users can input a book title and select the desired length for a generated summary. This feature assists users in previewing book content before making a borrowing decision.

![Any Book Summary_Long](https://github.com/chamith-Hemisara/LibraLoom_new/assets/109784789/a42ad6fc-57df-48ac-97d2-1a69fb31bd90)


### Profile Page 👤
The user-centric section provides personal and membership details along with book reservation information. To reserve books, users need to visit the library and complete the registration process.

![Profile Page](https://github.com/chamith-Hemisara/LibraLoom_new/assets/109784789/23238608-c1d1-4efd-b7e1-1438bcb5211e)

### Contact Us Page 🙌
This page contains contact information for LibraLoom. Also, it includes details about the LibraLoom team.

![Contact us page ](https://github.com/chamith-Hemisara/LibraLoom_new/assets/129577822/b73bd3ff-2f48-4c63-bb4f-60a93c340a0e)


### Admin Dashboard 👩‍💼
An administrative interface enabling librarians to manage books, categories, members, and handle reservation requests efficiently.

![Admin Dashboard](https://github.com/chamith-Hemisara/LibraLoom_new/assets/129577822/5a84884f-5bd5-4d7f-ac1e-7c7f5717a1ea)


## Technology Stack
- Django
- Templates (HTML/CSS)
- JavaScript

## How to Use

**To set up and run LibraLoom on your local machine, follow these steps:**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/chamith-Hemisara/LibraLoom_new.git

2.**Navigate to the Project Directory:**
	```
	cd LibraLoom
	```

3.**Set Up a Virtual Environment (Optional but Recommended):**
	```
	virtualenv venv
	source venv/bin/activate
	```
	

4.**Install Dependencies:**
	```
	pip install -r requirements.txt
	```
	
5.**Perform Database Migrations:**
	```
	python manage.py makemigrations
	python manage.py migrate
	```
	
6.**Run the Development Server:**
	```
	python manage.py runserver
	```

7.**Access the Application:**
	Open a web browser and go to http://127.0.0.1:8000 or         http://localhost:8000 to explore LibraLoom.

 ## Deployment Note

### LibraLoom on PythonAnywhere
[LibraLoom on PythonAnywhere](https://chamithlibraloom.pythonanywhere.com/LibraLoom/home/)

### Functionalities:
While the deployed version showcases the key features of LibraLoom, including the Home Page, Advanced Search, Any Book Details, Any Book Summary, Profile Page, Admin Dashboard, and Social Sign-In Page, it's important to note a few limitations.

### Limited Book and Category Display:
As a free service, we have included a restricted set of content to demonstrate the platform's capabilities. The current deployment features only five books and five categories. This limitation is in place as per the requirements of the free service.

### Book Additions:
We add books to the platform in accordance with our specific requirements. While the number of books is limited in this demonstration, the application's structure allows for easy expansion to include a more extensive library collection.

### Social Authentication and Any Book Details:
Due to the constraints of the free version, the social authentication feature and the "Any Book Details" pages may not be fully operational. We encourage you to explore and test the other functionalities available on the deployed platform.

### Get Involved
If you're interested in contributing to LibraLoom or have feedback, check out our GitHub repository. Feel free to explore the codebase, report issues, and contribute to the growth of the project.

### Acknowledgments
Acknowledge any libraries, APIs, or resources used in the project:

### Libgen API
-Plam API (Google)
-Video Demonstration 🎥
-Explore the diverse functionalities and features of LibraLoom in action: [](https://github.com/chamith-Hemisara/LibraLoom_new/assets/82514256/8c89a9d5-1a06-47ca-8b28-eade49e9398b)

Thank you for your understanding, and we hope you enjoy exploring LibraLoom!




