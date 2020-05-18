from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def index(request):
    date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    message = 'Server is live. Checked at : ' + str(date)
    return Response(data=message, status=status.HTTP_200_OK)
