from modules.hsw import hsw
from modules.hsj import hsj

u = input("HSW/HSJ/HSL(for now only hsw,hsj supported): ")
if u.lower()=="hsw":
    hsw()
elif u.lower()=="hsj":
    hsj()
