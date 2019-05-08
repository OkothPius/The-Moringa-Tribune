from django.test import TestCase
from .models import Editor,Articles,tags

# Create your tests here.
class EditorTestCase(TestCase):

    #set Up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name = 'Muriuki', email ='james@moringaschool.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    #testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

        



class ArticlesTestCase(TestCase):

    #setup method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name = 'Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()        

        self.new_article.tags.add(self.new_tag)
        
        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()


class tagsTestCase(TestCase):

    #setup method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name = 'Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        #creating a new tag and saving it        
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

   
    def tearDown(self):
            Editor.objects.all().delete()
            tags.objects.all().delete()
            Articles.objects.all().delete()