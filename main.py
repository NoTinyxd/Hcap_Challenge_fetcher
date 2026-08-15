from modules.hsw import hsw
from modules.hsj import hsj
from modules.hsl import hsl
u = input("HSW/HSJ/HSL: ")
if u.lower()=="hsw":
    hsw()
elif u.lower()=="hsj":
    hsj()
elif u.lower()=="hsl":
    hsl()
