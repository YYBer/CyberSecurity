SSRF (Server-Side Request Forgery)

The application allows users to fetch content from a specified URL by making a GET request. This can be exploited to make the server issue requests to internal services or sensitive endpoints.
LFI (Local File Inclusion)

The application allows users to fetch the contents of local files by specifying a file:/// URL. This can be exploited to read sensitive files on the server.