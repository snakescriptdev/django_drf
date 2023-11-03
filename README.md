# DRF AUTHRIAZATION
In DRF we have multiple ways to authorize the user. In this project, we will see how to authorize the user using the token. We will also see how to create a token for the user and how to use it to authorize the user.

## type of authorization
1. BasicAuthentication
2. SessionAuthentication
3. TokenAuthentication
4. OAuthAuthentication

## BasicAuthentication
In django basic authentication is used to authenticate the user using the username and password. In this type of authentication, the user needs to send the username and password with every request to authenticate the user. This type of authentication is not recommended for production use. This type of authentication is used for testing purposes.

## SessionAuthentication
In django session authentication is used to authenticate the user using the session id. In this type of authentication, the user needs to send the session id with every request to authenticate the user. This type of authentication is recommended for production use. This type of authentication is used for testing purposes.

## TokenAuthentication
In django token authentication is used to authenticate the user using the token. In this type of authentication, the user needs to send the token with every request to authenticate the user. This type of authentication is recommended for production use. This type of authentication is used for testing purposes.



## OAuthAuthentication
In django OAuth authentication is used to authenticate the user using the OAuth. In this type of authentication, the user needs to send the OAuth with every request to authenticate the user. This type of authentication is recommended for production use. This type of authentication is used for testing purposes.
