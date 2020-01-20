import re

# pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# res = pattern.findall("call me at 415 555-42421")
# or
# re.search(r'\d{3} \d{3}-\d{4}',"call me at 415 555-42421")

# print(res)

# def extract_phone(input):
#     pattern = re.compile(r'\d{3} \d{3}-\d{4}')
#     match = pattern.search(input)

#     return match.group()

# print(extract_phone("my number is 432 567-8975"))

# def is_valid_time(input):
#     pattern = re.compile(r'^\d{1,2}:\d{1,2}$')
#     match = pattern.search(input)
#     print(match)
#     if match:
#         return True
#     return False

# print(is_valid_time("232:23"))

# def parse_bytes(input):
#     pattern = re.compile(r'\b0+|1+\b')
#     match = pattern.findall(input)
#     return match

# print(parse_bytes("my data is : 1010101 10100110"))

# def parse_date(date):
#     pattern = re.compile(r'(\d{2})[.,/](\d{2})[.,/](\d{4})')
#     match = pattern.search(date)
#     print(match.groups())


import re

# def parse_date(date):
#     pattern = re.compile(r'(\d{2})[.,/](\d{2})[.,/](\d{4})')
#     match = pattern.search(date)
#     print(match.group(1))
#     if not match:
#         return None
#     return dict(d=match.group(1),m=match.group(2),y=match.group(3))
# print(parse_date("01/22/1999"))

# def censor(word):
#     pattern = re.compile(r'\bfrack[a-z]*',re.IGNORECASE)
#     # match = pattern.findall(word)
#     match = pattern.sub("CENSORED",word)
#     print(match)

# censor("hello i am fracking")

print("hello".replace())