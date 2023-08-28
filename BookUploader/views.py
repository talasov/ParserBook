from django.shortcuts import render

from .forms import BookUploadForm
from .utils import process_uploaded


def upload_book(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file = request.FILES['file']
                book_info = process_uploaded(file)
                return render(request, 'book_info.html', {'book_info': book_info})
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                return render(request, 'upload_book.html', {'form': form, 'error_message': error_message})
    else:
        form = BookUploadForm()
    return render(request, 'upload_book.html', {'form': form})
