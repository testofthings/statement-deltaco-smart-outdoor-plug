""" Security statement """
# pylint: disable=pointless-statement
# pylint: disable=expression-not-assigned

from toolsaf.main import Builder, TLS, DNS, UDP, ARP, EAPOL, ICMP, TCP, HTTP, MQTT
from toolsaf.common.android import (
    LOCATION, BLUETOOTH, ADMINISTRATIVE, UNCATEGORIZED,
    NETWORK, RECORDING, STORAGE
)

# Start modeling the IoT system
system = Builder.new("Deltaco Smart Outdoor Plug")

# Services by the environment
any_host = system.any("Services")

# Defining the device
smart_plug = system.device("Smart Plug")

# Define open ports on the device
smart_plub_tcp_port = smart_plug / TCP(port=6668)
smart_plug_udp_port = smart_plug / UDP(port=63144)

# Defining the mobile app
mobile_app = system.mobile("Smart Home App")

# Define mobile app permissions
mobile_app.set_permissions(
    LOCATION, BLUETOOTH, ADMINISTRATIVE, UNCATEGORIZED,
    NETWORK, RECORDING, STORAGE
)

# Defining broadcasts
udp_broadcast_1 = smart_plug.broadcast(UDP(port=6667))
mobile_app << udp_broadcast_1

udp_broadcast_2 = mobile_app.broadcast(UDP(port=7000))  # Some data
udp_broadcast_3 = mobile_app.broadcast(UDP(port=30011)) # All zeros
udp_broadcast_4 = mobile_app.broadcast(UDP(port=30012)) # All zeros
smart_plug << udp_broadcast_2
smart_plug << udp_broadcast_3
smart_plug << udp_broadcast_4

# Defining relevant backend services
tuya_1 = system.backend("Tuya Smart 1").serve(TLS, HTTP).dns("a1.tuyaeu.com") #18.193.211.120
tuya_2 = system.backend("Tuya Smart 2").serve(TLS(port=8883), TLS, MQTT).dns("m1.tuyaeu.com") #18.194.10.142
tuya_3 = system.backend("Tuya Smart 3").serve(TLS).dns("a3.tuyaeu.com") # 3.121.131.36
tuya_4 = system.backend("Tuya Smart 4").serve(TLS(port=8886)).dns("m2.tuyaeu.com") # 3.66.126.37 # Not found by shodan
tuya_images = system.backend("Tuya Images").serve().dns("images.tuyaeu.com").dns("djivuyxezwp4s.cloudfront.net") # 3.164.68.75, not found by shodan
aws = system.backend("AWS").serve(TLS, HTTP).dns("euimagesd2h2yqnfpu4gl5.cdn5th.com").dns("d46e0u663bkjg.cloudfront.net") # 18.165.122.35, ...
iot_dns = system.backend("IoT DNS").serve(TLS).dns("h3.iot-dns.com") # 76.223.21.194
tencent = system.backend("Tencent Cloud Computing").serve(TCP(port=443)).dns("tencent.com") # Did not respond # 162.14.14.21

# Defining backend service SBOM
aws.software().sbom(["amazon_cloudfront"])

# Defining connections by the environment
any_host >> smart_plug / ARP / EAPOL / ICMP
any_host >> mobile_app / ARP

# Defining connections from the device
smart_plug >> any_host / DNS / ICMP
smart_plug >> mobile_app / ARP
smart_plug >> tencent / TCP(port=443)
smart_plug >> tuya_3 / TLS
smart_plug >> tuya_4 / TLS(port=8886)
smart_plug >> iot_dns / TLS()

# Defining connections from the mobile application
mobile_app >> any_host / DNS / ARP
mobile_app >> smart_plub_tcp_port
mobile_app >> tuya_1 / TLS
mobile_app >> tuya_2 / TLS(port=8883)
mobile_app >> tuya_images / TLS
mobile_app >> aws / TLS

# Define privacy and security policies
system.online_resource("privacy-policy", url="https://aurdel.com/fi/en/privacy-policy", keywords=[
    "privacy policy", "personal data", "consent", "terms", "third party"
])
system.online_resource("cookie-policy", url="https://aurdel.com/fi/en/cookie-policy", keywords=[
    "cookie policy", "stored", "delete", "personal data", "expiry"
])
# No security policy found

# Define collected sensitive data
system.data(["User e-mail", "WiFi SSID", "WiFi password"])


if __name__ == '__main__':
    system.run()
