import hashlib, hmac, base64

'''
signature
  sign: timestamp.method.path
  base64(
    sha256(
      sign, secret_key
    )
  )
'''

class Signature:

  @staticmethod
  def generate(timestamp, method, path, secret_key):
    message = f"{timestamp}.{method}.{path}"
    hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
    hash.hexdigest()

    return base64.b64encode(hash.digest())