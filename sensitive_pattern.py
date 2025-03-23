patterns = {
     "API Key": r"(api_key|apikey|key|access_token)[\s=:\"']{0,10}([a-zA-Z0-9_\-]{10,})",
     "JWT Token": r"ey[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
     "Secret Key": r"(secret|token|password)[\s=:\"']{0,10}([a-zA-Z0-9_\-]{10,})",
     "Email Address": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
     "Phone Number": r"(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
}