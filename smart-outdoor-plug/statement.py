""" Security statement """
# pylint: disable=pointless-statement
# pylint: disable=expression-not-assigned

from tdsaf.main import Builder, TLS, DNS

system = Builder.new("Deltaco Smart Outdoor Plug")

any_host = system.any("Services")

mobile = system.mobile("Smart Home App")

tuya_1 = system.backend("Tuya Smart 1").serve(TLS(auth=True)).dns("a1.tuyaeu.com") #18.193.211.120
tuya_2 = system.backend("Tuya Smart 2").serve(TLS(auth=True)).dns("m1.tuyaeu.com") #18.194.10.142
aws = system.backend("AWS").serve(TLS(auth=True)).dns("euimagesd2h2yqnfpu4gl5.cdn5th.com") # 18.165.122.35, ...

mobile >> any_host / DNS
mobile >> tuya_1 / TLS(auth=True)
mobile >> tuya_2 / TLS(auth=True)
mobile >> aws / TLS(auth=True)

if __name__ == '__main__':
    system.run()
