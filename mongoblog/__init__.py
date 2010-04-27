# FIXME: This should and could be done better, need to check django source for a way of detecting a test so that this part can be moved back to settings.py
# Check if we're runing a test, otherwise connect to the default database
from mongoblog import testrunner
if not testrunner._running_test:
    from mongoengine import connect
    from django.conf import settings
    
    db_name = getattr(settings, 'MONGOBLOG_DATABASE_NAME', 'mongoblog')
    
    db = {}
    db['username'] = getattr(settings, 'MONGOBLOG_DATABASE_USERNAME', None)
    db['password'] = getattr(settings, 'MONGOBLOG_DATABASE_PASSWORD', None)
    db['host'] = getattr(settings, 'MONGOBLOG_DATABASE_HOST', None)
    db['port'] = getattr(settings, 'MONGOBLOG_DATABASE_PORT', None)

    params = {}
    for k, v in db.iteritems():
        if v:
            params[k] = v

    connect(db_name, ','.join(['%s=%s' % (k, v) for k, v in params.iteritems()]))
