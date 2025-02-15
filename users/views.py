from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from .serializers import CustomTokenObtainPairSerializer
from .token_helpers import store_access_token
from django.contrib.auth import authenticate

# Create your views here.

User = get_user_model()


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=400)

        response = super().post(request, *args, **kwargs)

        access_token = response.data.get("access")
        if access_token:
            store_access_token(user, access_token)

        return response


class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                return Response(
                    {"error": "No access token provided"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            access_token = auth_header.split(" ")[1]
            decoded_token = JWTAuthentication().get_validated_token(access_token)
            jti = decoded_token["jti"]

            token = OutstandingToken.objects.get(jti=jti)
            BlacklistedToken.objects.create(token=token)

            return Response(
                {"message": "Logged out successfully"},
                status=status.HTTP_205_RESET_CONTENT,
            )

        except OutstandingToken.DoesNotExist:
            return Response(
                {"error": "Token not found in outstanding tokens"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
