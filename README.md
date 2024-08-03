# Flask HTTPAuth API

## BasicAuth

`what is basic authentication`

Basic Authentication is a simple HTTP authentication mechanism where the client sends a username and password encoded in a base64 string in the Authorization header of each request. This method is widely supported but offers poor security as the credentials are transmitted in plain text.

The client sends a request to the server, including the username and password in the Authorization header.
The server extracts the username and password from the header.
The server verifies the provided credentials against its internal user database or authentication system.
If the credentials match, the server grants access to the requested resource; otherwise, it denies access.

## DigestAuth

`what is digest authentication`

Digest authentication is a challenge-response authentication mechanism used to verify a user’s identity without transmitting their password in plaintext over the network. It’s a more secure alternative to basic authentication, which sends passwords in base64 encoding over HTTP.


The client requests access to a protected resource, and the server responds with a 401 Unauthorized status code and a “WWW-Authenticate” header containing the authentication realm and a nonce value (a random string).
The client generates a hash using the MD5 algorithm, combining the username, password, and nonce value. This hash is then sent to the server in the “Authorization” header, along with the username.
The server verifies the username and computes its own hash using the same inputs (username, password, and nonce value).
If the client’s hash matches the server’s hash, the authentication is successful, and the server grants access to the requested resource.

## Token Authentication

`What is token authentication`

Token authentication is a type of authentication mechanism that generates and verifies encrypted security tokens. These tokens enable users to verify their identity to websites, applications, or services, without having to re-enter their login credentials each time. The token serves as a digital “ticket” or “stamp” that confirms the user’s identity and authorizes access to protected resources.

`Key Components`

Header: Specifies the algorithm used to create the digital signature.
Payload: Defines the token issuer, expiration details, user information, and metadata.
Signature: Verifies the authenticity of the message and ensures it hasn’t been tampered with during transmission.

`How Token Authentication Works`

Request: A user logs in to a service using their credentials, which issues an access request to a server or protected resource.
Token Generation: The server generates a unique, encrypted authentication token based on the user’s credentials and other metadata.
Token Distribution: The token is sent to the user’s device or browser.
Verification: When the user attempts to access a protected resource, they present the token to the server.
Validation: The server verifies the token’s authenticity, expiration, and user information.
Access Grant: If the token is valid, the server grants access to the requested resource.

## Author

- [waltertaya](https://www.github.com/waltertaya)

