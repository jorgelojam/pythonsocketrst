# Servidor web connection reset

Prueba de concepto de servidor web que responde a un peticion con un connection reset desde el servidor

Se levantan dos maquinas virtuales una como servidor web1 y una como cliente cliente1, las definiciones puede verse en el archivo Vagrantfile

```
vagrant up
```

Se conecta al servidor por medio de

```
vagrant ssh vm1
```

Dentro de la vm1 del servidor web1 bebe ejecutar como root


```
dnf install python3
pip3 install -r /vagrant/requirements.txt
```

Levantar el servidor web

```
python3 /vagrant/server.py

```

Ahora se conecta a la máquina cliente

```
vagrant ssh vm2
```

Se instala como root el sniffer y se lo ejecuta

```
dnf install tcpdump
tcpdump -i enp0s8 -w /tmp/salida.pcap
```

Se abre otra sesion ssh a la maquina cliente para realizar peticiones con el curl

```
vagrant ssh vm2
```

Ejecutar las peticiones con curl

```
curl http://192.168.56.10:8000/
curl http://192.168.56.10:8000/about
curl http://192.168.56.10:8000/reset
```

Copiar el archivo /tmp/salida.pcap y abrir con wireshark para revisar el reset enviando por el servidor de manera explicita