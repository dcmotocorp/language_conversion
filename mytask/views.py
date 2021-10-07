from django.shortcuts import render
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from ai4bharat.transliteration import XlitEngine

class ApiErrorException(Exception):
    pass
"""
class GetAlbumsList(APIView):
    def get(self, request, format=None):
        This function provides Details of all Albums.

        try:

            response = requests.get("https://jsonplaceholder.typicode.com/albums")

            if not response:
                raise ApiErrorException("response is not found.")
                # raise {'msg':'response not found'}
                
            data = response.json()
            if not data:
                raise ApiErrorException("data is not found.")
            return Response(data)

        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
"""            
class GetLangugeData(APIView):
    def get(self,request):
        try:
            """
            laninp = input("Enter language: ")
            word = input("Enter word: ")
            e = XlitEngine(laninp)
            out = e.translit_word(word, topk=5, beam_width=10)
            data = response.json()
            return Response(data)
            """
            laninp = input("Enter language: ")
            e = XlitEngine(laninp)
            word = input("Enter word: ")
            out = e.translit_word(word, topk=5, beam_width=10)
            return Response(out)

        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
