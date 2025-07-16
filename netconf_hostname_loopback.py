# netconf_hostname_loopback.py

from ncclient import manager
import xml.dom.minidom

# Datos del router
router = {
    "host": "192.168.85.3",  # Cambia esta IP si tu CSR1000v tiene otra
    "port": 830,
    "username": "cisco",
    "password": "cisco",
    "hostkey_verify": False
}

# XML para cambiar el hostname
hostname_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Catalan-Toro-Tello</hostname>
  </native>
</config>
"""

# XML para configurar loopback 111 con IP
loopback_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>111</name>
        <ip>
          <address>
            <primary>
              <address>111.111.111.111</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

# Conexión y envío de configuración
with manager.connect(**router) as m:
    print("✅ Conectado al router vía NETCONF.")

    # Cambiar hostname
    hostname_reply = m.edit_config(target="running", config=hostname_config)
    print("✅ Hostname configurado:")
    print(xml.dom.minidom.parseString(hostname_reply.xml).toprettyxml())

    # Crear Loopback111
    loopback_reply = m.edit_config(target="running", config=loopback_config)
    print("✅ Loopback 111 configurado:")
    print(xml.dom.minidom.parseString(loopback_reply.xml).toprettyxml())
