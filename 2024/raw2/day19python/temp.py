import urllib.parse

def decode_url(safelink_url):
    # Extract the part of the URL after "url="
    start_index = safelink_url.find('url=') + 4
    end_index = safelink_url.find('%3F', start_index)  # Safe stop point at query parameters, if necessary
    encoded_url = safelink_url[start_index:end_index]

    # Decode the URL
    decoded_url = urllib.parse.unquote(encoded_url)
    
    return decoded_url

# Example usage
safelink_url = "https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Finvoices.guru%2FXSEZyUVVERTlWSVR4by9lUXIveVA3cmk5d1VjL3BMeEk0bHNmTW5yUUszSmhFdUkvRFdRMFprcnN3ZWU4c04vdUhMNGl0WnJSK3k2WGJFNVorcmhkWlpJa3oxQzNoenliMjVlK2FVOHlURklXT3NHS2IvOUt1cDI2YmRDeWEwQU5aRm5wSTlSeVJRYzdtWVAyV2dNTjZWOVFvNGhBeE5YSUZFdjhZajR1YXNpajNlb25UY3Zqb1YvRE96Vk5DNHo5eXZWK0pFRHgxY1ZBYXFvRGV3THZPR0lIaU01SXNtbTZMdTJSNUEvNzJVblhBSXc9LS1XZEZJSUo1Qzc4bWJ5c1AxLS1lQXhPNStCZHRyQnRSbmhVSmt0L2d3PT0%3D%3Fcid%3D300783549&data=05%7C02%7Cremco.vaes%40ns.nl%7C16591d7f780948c1585508dd19ca3c1f%7C644581590d9a4d84966f1a13c0ac7a34%7C0%7C0%7C638695078578329672%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C28000%7C%7C%7C&sdata=sS%2BPWGkMmHREvNt9xupTyhzXArLPtkzWbbop6%2F%2FBvDE%3D&reserved=0"
decoded_url = decode_url(safelink_url)
print("Decoded URL:", decoded_url)
