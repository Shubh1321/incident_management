from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from utils.helpers import get_address_from_pincode

class UserRegisterView(APIView):
    def post(self, request):
        data = request.data.copy()  # Create a copy of the request data

        # Auto-fetch city and country using pin code (assuming 'pin_code' is the correct key)
        pincode = data.get('pin_code')
        
        if not pincode:
            return Response({"error": "Pin code is required!"}, status=status.HTTP_400_BAD_REQUEST)
        
        address_info = get_address_from_pincode(pincode)
        
        if not address_info:
            return Response({"error": "Could not fetch city and country for the given pin code."}, status=status.HTTP_400_BAD_REQUEST)

        # Assign fetched city and country to the data
        data['city'] = address_info.get('city')  # Use .get() for safety in case of missing keys
        data['country'] = address_info.get('country')

        # Create user serializer instance with the modified data
        serializer = UserSerializer(data=data)
        
        # Validate the serializer and save the user
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)