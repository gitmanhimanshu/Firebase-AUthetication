from rest_framework.response import Response
from rest_framework.decorators import api_view

from .firebase import auth, admin_auth

@api_view(['POST'])
def register(request):
    email = request.data.get("email")
    password = request.data.get("password")
    try:
        # Create user using Firebase Admin SDK
        user = admin_auth.create_user(
            email=email,
            password=password
        )
        # Get custom token for the user
        custom_token = admin_auth.create_custom_token(user.uid)
        return Response({
            "message": "User created successfully",
            "uid": user.uid,
            "customToken": custom_token
        })
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['POST'])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return Response({"message": "Login successful", "idToken": user['idToken']})
    except Exception as e:
        return Response({"error": str(e)}, status=400)


# Phone number registration using Firebase Admin SDK
@api_view(['POST'])
def registerbyfone(request):
    phone_number = request.data.get('phone_number')
    if not phone_number:
        return Response({"error": "Phone number required"}, status=400)

    try:
        user = admin_auth.create_user(phone_number=phone_number)
        return Response({"message": "User created successfully", "uid": user.uid})
    except Exception as e:
        return Response({"error": str(e)}, status=400)
