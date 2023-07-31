from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from PIL import Image
import pytesseract
import urllib.request
from io import BytesIO

class OCR(APIView):
    def get(self, request):
        #filename = f"{request.file}"
        #filepath = f"media/{filename}"
        #image = Image.open(filepath)
        image = Image.open(request.data.file)

        lang = ''
        for l in request.data.langs:
            lang += l
            lang += "+"
        lang = lang[0:-1]

        result = pytesseract.image_to_string(image, lang=lang)
        return Response({"result":result})
    
    def post(self, request):
        data = request.data
        file = data.get('file')
        langs = data.get('langs')
        #file = file[1:]

        with urllib.request.urlopen(file) as url:
            image_bytes = BytesIO(url.read())

        image = Image.open(image_bytes)

        lang = ''
        for l in langs:
            lang += l
            lang += '+'
        lang = lang[0:-1]

        result = pytesseract.image_to_string(image, lang=lang)
        print('result:',result)
        return Response({"result":result})

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login_form.html')

def board_write(request):
    return render(request, 'board_form.html')

def board(request, post_no):
    return render(request, 'board.html')

def join(request):
    return render(request, 'join_form.html')

def mypage(request):
    return render(request, 'mypage.html')

def user_update(request):
    return render(request, 'user_update_form.html')

def board_list(request):
    return render(request, 'board_list.html')

def board_update(request, post_no):
    return render(request, 'board_update_form.html')

# def logout(request):
#     return render(request, 'logout_form.html')