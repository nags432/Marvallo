#### 1.Install & configure mysql server ####
recommended encoding serverside - `utf-8` 

#### 2.Installing dependencies & configuring django app ####

   1. * `pip install Django`   
   or if  problems with compatibility is appeared try:  
      * `pip install Django==1.10.4`
     
   2.  * goto `student_survey_base` folder
       * edit file `settings.py'
       * in string `ALLOWED_HOSTS = ['localhost', '192.168.0.111']`
       change ip adress to yours external network ip adress assigned to yours' machine,
       it should be looked like ex.:
       `ALLOWED_HOST=['localhost', '192.168.3.58']`
       where 192.168.3.58 is external ip adress in the net
       * then configure database part but don't change layout of marking symbols, 
       such as `:`  `'`  `,`   `{` `}`and etc.
       
       ```
       DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'student_survey',  # write in database name ex: 'NAME': 'mysurveys_database',
                'USER': 'root',            # root username
                'PASSWORD': '123456abc',   # database root user`s password
                'HOST': 'localhost',       # Or an IP Address that your DB is hosted on
                'PORT': '3306',            # port of mysql server
                'OPTIONS': {
                    'read_default_file': '/etc/mysql/my.cnf',  # path to configuration file for mysql database
                 },
            }
        }
        
       ```
                                        
  3. `pip install mysqlclient`  
   or if problems with compatibility is appeared try:  
     `pip install mysqlclient==1.3.9`

     
##### 3. Create superuser account to manage user accounts or to login #####
  in console:
   * cd to the root project folder 
   * run `python manage.py migrate` to synchronize database and Django ORM 
   * `python manage.py createsuperuser`                                                                                 
     
Input login name, password, email(can be skipped)
Then it is possible to manage user accounts via django admin interface 
http://sitename.com/admin   
Ex.: http://localhost:8000/admin  on test server

* Staff status can be assigned to user account in order to make him able to enter 
django-admin interface, or if it`s not assigned - user can enter only web page 

##### 4. To run test server ######
in console:
1. cd to the root project folder
2. run `python manage.py runserver`
3. goto http://localhost:8000 to see result on test server

 
