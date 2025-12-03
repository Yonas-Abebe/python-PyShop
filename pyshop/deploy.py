import hmac
import hashlib
import subprocess
from django.http import HttpResponse

# Optional: Add a secret if you want security
SECRET = b''  # leave empty for now

def deploy(request):
    if request.method != "POST":
        return HttpResponse("POST required", status=405)

    # Run git pull
    subprocess.Popen(["/usr/bin/git", "-C", "/home/yoni/PyShop", "pull"])

    return HttpResponse("Deploy triggered")