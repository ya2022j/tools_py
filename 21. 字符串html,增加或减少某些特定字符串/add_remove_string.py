

import re

logo_title_string = "{% logo_title.html %} \n"
html = "<!DOCTYPE html>  <title>MSN</title>  sdfAadfafasfds"


remove_string = "<!DOCTYPE html>|<title>(.*?)</title>"
def clean_except_big_string(big_string):

    big_string = re.sub(remove_string,'',big_string)
    big_string = logo_title_string+big_string
    return big_string

print(clean_except_big_string(html))