from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response

from .models import Stats
from .serilizers import StatsSerializer
from .leastPositiveInteger import validateArray
from .stats import validateStats


# This viewset will return a list of all the Stats objects.
class SmallestViewSet(generics.ListAPIView):
    queryset = Stats.objects.all()

    def get(self, request, *args, **kwargs):
        """
        It takes a list of integers, validates it, and then saves it to the database
        
        :param request: The request object is a HttpRequest object. It contains all the information about
        the request sent by the client
        :return: The response is a JSON object with the key 'result' and the value is the sum of the array.
        """
        try:
            arrayNumbers = request.data['array']
            intList = list(map(int, arrayNumbers))
            data = validateArray(intList) 
            for key in data.keys():
                if key != str('result'):
                    return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)    
                self.create(data.get('result'))
                return Response(data=data, status=status.HTTP_200_OK)
        except ValueError as e:
            error = {'error': '{}'.format(e)}
            return Response(data=error, status=status.HTTP_400_BAD_REQUEST)


    def create(self, result):
        """
        It takes the result of the user's input and saves it to the database
        
        :param result: The result of the test
        """
        smallest = Stats(
            result= result,
            total = 1
        )
        smallest.save()



# It takes in a request, checks if the request is valid, and returns a response
class StatsViewSet(generics.ListAPIView):
    queryset = Stats.objects.all()

    def get(self, request, *args, **kwargs):
        """
        It takes in a request, checks if the request is valid, and returns a response
        
        :param request: the request object
        :return: The response is being returned.
        """
        stats = request.data['stats']
        response = validateStats(stats)
        if response != False:
            return Response(data=response, status=status.HTTP_200_OK)
        error = {'Error': 'the number entered does not exist in the database'}
        return Response(data=error, status=status.HTTP_400_BAD_REQUEST)