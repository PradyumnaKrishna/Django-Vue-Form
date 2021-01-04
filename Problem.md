# Problem Statement

## Task Details
1. Create a Django or Node.js or Go or ‘Ruby on Rails’ Application which shows a simple format "/user-form". The form asks the user for his details(name, date of birth, email, phone number). The form is rendered in any of the modern frontend frameworks like React.js, Vue.js or ​ Angular. The date of the birth field should be a calendar option.
2. The user fills the form and presses submit. Perform basic front-end validation on the name, email, DoB (age cannot be less than 18 years).
3. Phone number validation happens at the backend. If you are using Django then Django-Rest-Framework is preferred. If RoR, node.js or Go or Scala, use the relevant framework/suggested best practice for writing modular code.
4. Save the form and send an email to the form submitter.
5. After the form is submitted redirect the user to a page where all the submitted forms are displayed.

## Other Requirements:
- If using Python then follow Python's coding standard (PEP8). For other languages/platforms use appropriate recommended coding standards.
- Use git to revise your code. You can upload your code to GitHub
- Use python virtual environments to manage the dependencies in case you are using Django/Python

## Bonus:
- Write tests if possible

## Tips:
- Django Rest Framework: [http://www.django-rest-framework.org​](http://www.django-rest-framework.org). This helps in serialization/deserialization of data and auto data validation via Models you created.
- Celery helps in performing tasks asynchronously. While Rabbit MQ queues and de-queue's the tasks and gives them to celery. These have a very standard implementation/integration with Django
- Kindly note that not all platforms require the use of Celery as Asynchronous code can be executed natively on platforms like Node.js or Go

## What you will submit:
- Upload your application to Heroku cloud or similar online hosting platforms and share URL link for your submission
- Maintain your complete code via GIT. Upload it to Github/Gitlab. Share the repository’s link
- Upload demo video of using the form (optional)

**NOTE​: There is no extra weightage for Django. Developing in any language/framework will carry equal weightage (Django/Node.js/Go/Ruby on Rails).**