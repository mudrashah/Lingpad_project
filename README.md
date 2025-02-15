Setting Up the Django Project with Virtual Environment  

1. Reference API Documentation
Use the following URLs for API documentation reference:  
- [Swagger Docs](http://127.0.0.1:8000/api/docs/#/)  
- [ReDoc](http://127.0.0.1:8000/api/redoc/)  

2. Set Up a Virtual Environment
1. Create a virtual environment:  
   
   python -m venv venv
   
2. Activate the virtual environment:  
   - Windows:
     
     venv\Scripts\activate
     
   - Mac/Linux:
     
     source venv/bin/activate
     
3. Install dependencies from `requirements.txt`:  
   
   pip install -r requirements.txt
   
4. Verify installed dependencies:  
   
   pip freeze
   

3. Django Commands
- Run the development server:  

  python manage.py runserver

- Create a superuser for Django Admin:  

  python manage.py createsuperuser
