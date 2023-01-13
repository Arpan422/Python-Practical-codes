from PIL import ImageColor
hex = input('Enter HEX value: ').lstrip('#')
print('RGB value =', tuple(int(hex[i:i+2],16) for i in (0,2,4)))