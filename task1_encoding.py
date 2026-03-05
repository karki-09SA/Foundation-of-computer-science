import base64
import urllib.parse
import hashlib

print("=" * 55)
print("         BASE64 ENCODING DEMONSTRATION")
print("=" * 55)

original_text = "Hello, this is a secure message!"
print(f"\nOriginal Text  : {original_text}")

encoded_bytes = base64.b64encode(original_text.encode("utf-8"))
encoded_str = encoded_bytes.decode("utf-8")
print(f"Base64 Encoded : {encoded_str}")

decoded_str = base64.b64decode(encoded_bytes).decode("utf-8")
print(f"Base64 Decoded : {decoded_str}")

original_size = len(original_text.encode("utf-8"))
encoded_size = len(encoded_str)
overhead = round(((encoded_size - original_size) / original_size) * 100, 1)
print(f"\nOriginal Size  : {original_size} bytes")
print(f"Encoded Size   : {encoded_size} bytes")
print(f"Size Overhead  : +{overhead}%")

print("\n--- Email Attachment Simulation ---")
file_data = b"This is the content of a PDF attachment."
attachment_encoded = base64.b64encode(file_data).decode("utf-8")
print(f"Raw data    : {file_data}")
print(f"Base64      : {attachment_encoded}")

print("\n" + "=" * 55)
print("         ASCII ENCODING DEMONSTRATION")
print("=" * 55)

sample = "Hello!"
print(f"\nCharacter -> Decimal -> Binary")
print("-" * 38)
for ch in sample:
    print(f"  '{ch}'  ->  {ord(ch):>3}  ->  {format(ord(ch), '08b')}")

print(f"\n'A'={ord('A')}, 'a'={ord('a')}, '0'={ord('0')}, Space={ord(' ')}")
print(f"ASCII : 'Hello' -> {('Hello').encode('ascii')}")
print(f"UTF-8 : 'Hello World' -> {'Hello World'.encode('utf-8')}")

print("\n" + "=" * 55)
print("         URL ENCODING DEMONSTRATION")
print("=" * 55)

search_query = "ethical hacking & cybersecurity 2024"
url_encoded = urllib.parse.quote(search_query)
url_decoded = urllib.parse.unquote(url_encoded)

print(f"\nOriginal : {search_query}")
print(f"Encoded  : {url_encoded}")
print(f"Decoded  : {url_decoded}")

print("\n--- Special Characters ---")
for ch, name in [(" ","space"),("&","&"),("=","="),("?","?"),("/","/"),("'","'")]:
    print(f"  {name:6} -> {urllib.parse.quote(ch)}")

print("\n--- Injection Prevention ---")
malicious = "' OR 1=1 --"
print(f"Raw     : {malicious}")
print(f"Encoded : {urllib.parse.quote(malicious)}")
print("Single quote becomes %27 - safe, not executable SQL")

print("\n" + "=" * 55)
print("         HEX ENCODING DEMONSTRATION")
print("=" * 55)

hex_input = "CyberSec"
hex_encoded = hex_input.encode("utf-8").hex()
hex_decoded = bytes.fromhex(hex_encoded).decode("utf-8")

print(f"\nOriginal : {hex_input}")
print(f"Hex      : {hex_encoded}")
print(f"Decoded  : {hex_decoded}")

for ch in hex_input:
    print(f"  '{ch}' -> {format(ord(ch), '02x').upper()}")

hash_hex = hashlib.sha256("password123".encode()).hexdigest()
print(f"\nSHA-256 of 'password123':")
print(f"  {hash_hex}")

print("\n" + "=" * 55)
print("       OAuth Basic Auth Simulation")
print("=" * 55)

client_id = "myapp_client"
client_secret = "supersecretkey"
encoded_creds = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

print(f"\nClient ID   : {client_id}")
print(f"Secret      : {client_secret}")
print(f"Encoded     : {encoded_creds}")
print(f"Auth Header : Basic {encoded_creds}")
print("Sent over HTTPS - Base64 alone gives zero security")
