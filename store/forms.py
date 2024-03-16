from django import forms
from .models import Book





class BookCreationForm(forms.ModelForm):

        class Meta:
         model = Book
         fields = [ 'img' ,'title' , 'author']
        
        def __init__(self, *args, **kwargs):
            super(BookCreationForm,self).__init__(*args, **kwargs)
           
            for field  in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].widget.attrs['placeholder']=field.capitalize()

            
            self.fields['img'].widget.attrs['onchange']="showPreview(event);"
            


        def clean(self):
            cleaned_data = super(BookCreationForm, self).clean()
            title = cleaned_data.get('title')
            
            book = Book.objects.filter(title=title)
            if book.exists():
                
                self.add_error('title','book already exist')
                

            


            return cleaned_data   
