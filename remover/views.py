from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from rembg import remove
from PIL import Image
import os

def index(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        input_path = fs.save(uploaded_file.name, uploaded_file)
        input_full_path = fs.path(input_path)

        # Process image
        input_image = Image.open(input_full_path)
        output_image = remove(input_image)

        # Save result
        output_path = "removed_" + uploaded_file.name.split('.')[0] + ".png"
        output_full_path = fs.path(output_path)
        output_image.save(output_full_path)

        return render(request, 'index.html', {
            'uploaded_file_url': fs.url(input_path),
            'output_file_url': fs.url(output_path)
        })

    return render(request, 'index.html')
