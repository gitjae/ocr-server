from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Board
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from pyuploadcare import Uploadcare, File
from django.conf import settings
from django.shortcuts import redirect
import os

from urllib import request
from .serializer import BoardSerializer

def say_hello(request):
    return render(request, 'index.html', {
        'data':Board.objects.all(),
    })

# @api_view(['GET', 'POST'])
# def get_board_all(request):
#     boards = Board.objects.all()
#     # boards -> json형변환 (restframework의 serializer)
#     serializer = BoardSerializer(boards, many=True)
#     return Response(serializer.data)

class Boards(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            board = serializer.save()   # create()메소드 호출

            if board.file and board.file.size < settings.FILE_SIZE_LIMIT : 
                uploadcare = Uploadcare(public_key=settings.UC_PUBLIC_KEY, secret_key=settings.UC_SECRET_KEY) 
                with open(board.file.path, "rb") as file_object:
                    ucare_file = uploadcare.upload(file_object)
                    print('ucare_file.uuid:', ucare_file.uuid)
                    img_url = f'https://ucarecdn.com/{ucare_file.uuid}/'
                    print('img_url:',img_url)
                    board.image_link = img_url
            
            board.username = request.user
            board.save()

            mediafile = f"media/{board.file}"
            print('mediafile:',mediafile)
            if os.path.isfile(mediafile):
                os.remove(mediafile)

            return redirect(f'/board/{board.post_no}')
            #return Response(serializer.data)
        return Response(serializer.errors)

class BoardDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, post_no):
        try:
            board = Board.objects.get(post_no=post_no)
            return board
        except Board.DoesNotExist:
            raise NotFound

    def get(self, request, post_no):
        # pk를 가져와서 보드 한개 가져오기
        board = self.get_object(post_no=post_no)
        # 보드 인스턴스를 json 형변환
        serializer = BoardSerializer(board)
        # Response 객체로 반환
        return Response(serializer.data)

    def put(self, request, post_no):
        board = self.get_object(post_no=post_no)

        if not board.username == request.user:
            raise PermissionDenied

        serializer = BoardSerializer(instance=board, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, post_no):
        board = self.get_object(post_no)
        if not board.username == request.user:
            raise PermissionDenied
        board.delete()
        return Response({})
    
    