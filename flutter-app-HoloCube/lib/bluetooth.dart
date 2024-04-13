import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter_bluetooth_serial/flutter_bluetooth_serial.dart';
import 'dart:typed_data';
import 'dart:convert';

String address_to_connect = '';
bool connect = false;
String? connection_name = '';
BluetoothConnection? bluetoothConnection;
Future<bool> connectionFlag = Future.value(false);

void enableBluetooth() {
  FlutterBluetoothSerial.instance
      .requestEnable(); // Request Bluetooth to be turned on
}

Future<List<BluetoothDevice>> getPairedDevices(BuildContext context) {
  Completer<List<BluetoothDevice>> completer = Completer();

  FlutterBluetoothSerial.instance
      .getBondedDevices() // Get list of paired devices
      .then((List<BluetoothDevice> pairedDevices) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Paired Devices'),
          content: SingleChildScrollView(
            child: ListBody(
              children: pairedDevices.map((device) {
                return GestureDetector(
                  child: Text(device.name ?? ''),
                  onTap: () {
                    //print(device.address + device.name!);
                    //print('fuckfuck');
                    address_to_connect = device.address;
                    connectionFlag = connectToDevice(
                        /*'B8:27:EB:50:60:E7'*/ address_to_connect);
                    //B8:27:EB:50:60:E7 ==> raspberrypi
                    //00:A5:54:BB:95:3F ==> UTHSARAIW
                    Navigator.of(context).pop();
                    completer.complete(pairedDevices);
                  },
                );
              }).toList(),
            ),
          ),
        );
      },
    );
  });

  return completer.future;
}

//get the connected devices in the mobile
Future<List<BluetoothDevice>> getConnectedDevices() async {
  List<BluetoothDevice> connectedDevices = [];

  List<BluetoothDevice> pairedDevices =
      await FlutterBluetoothSerial.instance.getBondedDevices();

  for (BluetoothDevice device in pairedDevices) {
    if (device.isConnected) {
      connectedDevices.add(device);
    }
  }

  return connectedDevices;
}

Future<bool> isDeviceConnected() async {
  List<BluetoothDevice> devices = await getConnectedDevices();

  for (var device in devices) {
    print(device.name);
    if (address_to_connect == device.address) {
      connection_name = device.name;
      connect = true;
      break;
    }
  }

  print(connect);

  return connect;
}

Future<bool> connectToDevice(String address) async {
  try {
    //this connection has an error because it doesnt connect to alresdy connected devices
    //with the device

    BluetoothConnection connection =
        await BluetoothConnection.toAddress(address);
    bluetoothConnection = connection;

    // ...

    bluetoothConnection?.input?.listen((List<int> data) {
      // Use a logging framework instead of print
      // Example: logger.info('Received data from the device');
      print('Received data from the device');
    }).onDone(() {
      // Use a logging framework instead of print
      // Example: logger.info('Disconnected by remote request');
      print('Disconnected by remote request');
    });
    print('connect to device passed');
    print('connect to device passed');
    print('connect to device passed');
    return true;
  } catch (error) {
    // Use a logging framework instead of print
    // Example: logger.error('Failed to connect to device: $error');
    print('connect to device failed');
    print('connect to device failed');
    print('connect to device failed');
    print('Failed to connect to device: $error');
    return false;
  }
}

void sendDataToConnectedDevice(String data) {
  if (/*bluetoothConnection != null && bluetoothConnection!.isConnected*/ connect ==
      true) {
    bluetoothConnection?.output?.add(Uint8List.fromList(utf8.encode(data)));
    bluetoothConnection?.output?.allSent.then((_) {
      // Use a logging framework instead of print
      // Example: logger.info('Data sent successfully');
      print('Data sent successfully');
    }).catchError((error) {
      // Use a logging framework instead of print
      // Example: logger.error('Failed to send data: $error');
      print('Failed to send data: $error');
    });
  } else {
    // Use a logging framework instead of print
    // Example: logger.warning('No connected device');
    print('No connected device');
  }
}

void sendHexToConnectedDevice(String hexString) {
  if (bluetoothConnection != null && bluetoothConnection!.isConnected) {
    List<int> bytes = hexStringToBytes(hexString);
    bluetoothConnection?.output?.add(Uint8List.fromList(bytes));
    bluetoothConnection?.output?.allSent.then((_) {
      // Use a logging framework instead of print
      // Example: logger.info('Hex values sent successfully');
      print('Hex values sent successfully');
    }).catchError((error) {
      // Use a logging framework instead of print
      // Example: logger.error('Failed to send hex values: $error');
      print('Failed to send hex values: $error');
    });
  } else {
    // Use a logging framework instead of print
    // Example: logger.warning('No connected device');
    print('No connected device');
  }
}

List<int> hexStringToBytes(String hexString) {
  hexString = hexString.replaceAll(' ', '');
  List<int> bytes = [];
  for (int i = 0; i < hexString.length; i += 2) {
    String hex = hexString.substring(i, i + 2);
    int byte = int.parse(hex, radix: 16);
    bytes.add(byte);
  }
  return bytes;
}
