from django.test import TestCase

# Create your tests here.

import re


def slug_page(
	_name_text_field: str,
	_max_leng_url: int,
) -> str:
	_url: str = None
	_reg = (r'([\w]*[^\\\-;\\/ \\,\\><])')
	_url_line = str(re.findall(_reg, _name_text_field, flags=re.ASCII )) \
		.replace(' ', '_').strip("][").replace("'", '')\
		.replace(",", '')[ : _max_leng_url]
	return (_url_line)


t = 'line 241, in _call_with_*frames\_removed'
d =  slug_page(_name_text_field=t, _max_leng_url=20)

print(d)
# reg = (r'([\w]*[^\\\-;\\/ \\*,\\><])')
# url_line = str(re.finditer(reg, t)) \
# 		.replace(' ', '_').strip()


# print(list(url_line))