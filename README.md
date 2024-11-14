# Security Statement: Deltaco Smart Outdoor Plug
This repository contains our security statement for the Deltaco Smart Outdoor Plug.

The statement was created based on data collected with `nmap` and `tcpdump`.

## Device Description
The Deltaco Smart Outdoor Plug is an electrical plug that can be controlled with a mobile application.

<img src="Smart_Outdoor_Plug.jpg" width="40%" alt="Deltaco Smart Outdoor Plug"></br>
Fig. The device

The device's companion mobile application can be found [here](https://play.google.com/store/apps/details?id=com.deltaco.smarthome).

## Findings

### Ports
The device had the following ports open:
| Protocol | ID | State |
|----------|----|-------|
| TCP | 6668 | Open |
| UDP | 63144 | Open (Filtered) |

### Notable Connections
The device and/or mobile application connect to these backends:

| Note | URL / IP |
|------|----------|
| Tuya Smart Services       | `a1.tuyaeu.com`, `m1.tuyaeu.com`, `a2.tuyaeu.com`, `m2.tuyaeu.com`, `images.tuyaeu.com` |
| Tuya Smart IoT DNS        | `h3.iot-dns.com` |
| AWS                       | `euimagesd2h2yqnfpu4gl5.cdn5th.com` |
| Tencent Cloud Computing   | `162.14.14.21` |

### Sample Data
Sample data for this security statement can be found [here](https://github.com/testofthings/sample-data/deltaco-smart-outdoor-plug).

## Running the Statement
First create a Python virtual environment and install TDSAF, then run with:
```shell
python3 smart-outdoor-plug/statement.py -r ../sample-data/deltaco-smart-outdoor-plug
```
