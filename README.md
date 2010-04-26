# django-mongoblog

## Install

Make sure that you have the django-mongoblog/mongoblog directory on your PYTHONPATH.
Then add the application to your INSTALLED_APPS:

    INSTALLED_APPS = (
        ...
        'mongoblog',
    )

and to your urls.py:
    
    urlpatterns = patterns('',
        ...
        url(r'^blog/', include('mongoblog.urls')),
        ...
    )

The connection is currently made in mongoblog.views to support testing for
mongodb using the testrunner shipped with this app. To use the testrunner,
change your settings.py and add:
    
    TEST_RUNNER = 'mongoblog.testrunner.TestRunner'

## Dependencies

 * Django-1.2-beta-1 (should work with earlier versions without the use of the testrunner)
 * mongoengine
 * PyMongo

## Example
Check mongoblog/views.py and the templates for example usage. To add posts to your mongo-database, simple run the Django interactive shell:
    
    python manage.py shell

and use the following to add a test Entry.

    from mongoengine import connect
    connect('myDatabase')
    from mongoblog.models import Entry
    # status is needed to make the post show up on the blog, otherwise it will default to a draft which will not be visible
    Entry(title='Hello world!', body='This is a test entry!', status=Entry.STATUS_PUBLIC).save()

## Other info
The connection could be moved from the view to settings.py. The reason it's located in views.py is to make the test-suite work with the testrunner that is creating a temporary database. Putting the connection in settings.py will override the testrunners attempt to create and use the test-database. If you don't need to run any tests, feel free to move it if you feel like it.