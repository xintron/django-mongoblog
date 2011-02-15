from mongorunner import TestCase

from models import Entry

class SimpleTest(TestCase):
    def testEntry(self):
        # Create test entry
        be = Entry(
           title = 'Hello world',
           body = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
               Mauris id libero vitae nisl suscipit consequat a a justo. Proin id
               purus et sem sodales accumsan eget id dolor.
               """,
           status = Entry.STATUS_PUBLIC
        )
        be.save()

        self.failUnlessEqual(be.slug, 'hello-world')

        response = self.client.get('/blog/hello-world/')

        self.assertContains(response, 'consectetur adipiscing')

    # Test 404
    def test404(self):
        response = self.client.get('/blog/non-existing/')

        self.assertTemplateUsed(response, '404.html')

    # Check public blog posts, that only posts marked public is shown
    def testEntryListing(self):
        Entry(title = 'My life', body = 'Hello my dear friend').save()
        Entry(title = 'My lif2', body = 'Hello my dear friend', status = Entry.STATUS_PUBLIC).save()
        response = self.client.get('/blog/')

        self.assertTemplateUsed(response, 'mongoblog/entry_list.html')
        self.assertEquals(len(response.context['entry_list']), 2)
        self.assertContains(response, 'consectetur adipiscing')
