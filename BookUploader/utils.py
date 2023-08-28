from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError
from ebooklib import epub

from .models import Book


def process_uploaded(file):

    book_info = {}

    try:
        if file.name.endswith('.epub'):
            book = epub.read_epub(file)
        elif file.name.endswith('.fb2'):
            soup = BeautifulSoup(file, 'xml')

            title_tag = soup.find('book-title')
            if title_tag:
                book_info['Title'] = title_tag.text.strip()

            author_tag = soup.find('author')
            if author_tag:
                author_first_name = author_tag.find('first-name')
                author_middle_name = author_tag.find('middle-name')
                author_last_name = author_tag.find('last-name')

                if author_first_name and author_last_name:
                    full_author_name = f"{author_last_name.text.strip()} {author_first_name.text.strip()} {author_middle_name.text.strip()}"
                    book_info['Author'] = full_author_name.strip()

            publisher_tag = soup.find('publisher')
            if publisher_tag:
                book_info['Publisher'] = publisher_tag.text.strip()

            year_tag = soup.find('year')
            if year_tag:
                book_info['Year'] = year_tag.text.strip()
        else:
            raise ValueError('Unsupported file format')

        existing_book = Book.objects.filter(title=book_info.get('Title', ''), author=book_info.get('Author', ''))
        if existing_book.exists():
            return book_info

        book_obj = Book(title=book_info['Title'], author=book_info['Author'], publisher=book_info['Publisher'],
                        year=book_info['Year'])
        book_obj.save()

    except (ValidationError, ValueError, IndexError) as e:
        raise ValueError('Неверный формат файла или отсутствующие метаданные')

    return book_info
