# create n netsted dictionary from a list
import string
list_content=  list(string.ascii_uppercase)

print("\n")
print("\n")



print(list_content)
print("\n")
print("\n")
print("-"*100)
print("\n")
print("\n")
def nested_dict(list_content):
    if list_content:
        return {list_content[0]: nested_dict(list_content[1:])}

print(nested_dict(list_content))
print("\n")
print("\n")

# https://stackoverflow.com/questions/40401886/how-to-create-a-nested-dictionary-from-a-list-in-python

