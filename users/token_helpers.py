from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from datetime import datetime


def store_access_token(user, access_token_str):
    """Store access token in the OutstandingToken table."""
    token = AccessToken(access_token_str)
    OutstandingToken.objects.create(
        user=user,
        jti=token["jti"],
        token=str(token),
        created_at=datetime.now().isoformat(),
        expires_at=datetime.fromtimestamp(token["exp"]).isoformat(),
    )
