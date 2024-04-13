import 'package:flutter/material.dart';
import 'package:sensors/sensors.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:my_app/bluetooth.dart';

final TextEditingController emailController = TextEditingController();
final TextEditingController passwordController = TextEditingController();
late String gyroscopeData; // Define the variable gyroscopeData
late String showData = ""; // Define the variable gyroscopeData
bool flag = false;
bool upload_pressed = false;

//getting gyroscope data
void printGyroscopeData(BuildContext context) {
  if (flag) {
    showData = gyroscopeData;
  } else {
    showData = "";
  }
}

//change this to convert to a binary format
Future<String> fetchDataFromAPI(String str) async {
  print('http://16.171.4.112:5000/api/getobjfile/$str');
  final response =
      await http.get(Uri.parse('http://16.171.4.112:5000/api/getobjfile/$str'));
  if (response.statusCode == 200) {
    //jsonDecode(response.body);
    String resp = response.body;
    print('uthsarauthsara');
    print(resp);
    return resp;
  } else {
    throw Exception('Failed to fetch data from API');
  }
}

class User extends StatefulWidget {
  @override
  _UserState createState() => _UserState();
}

class _UserState extends State<User> {
  Map data = {};
  String userid = '';
  String cubeid = '';

  @override
  void initState() {
    super.initState();
    gyroscopeEvents.listen((GyroscopeEvent event) {
      setState(() {
        gyroscopeData = 'X: ${event.x}, \nY: ${event.y}, \nZ: ${event.z}';
        if (flag) {
          showData = 's' + gyroscopeData + 'z';
          sendDataToConnectedDevice(
              showData); // Call sendDataToConnectedDevice function
        }
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    data = ModalRoute.of(context)!.settings.arguments as Map;

    setState(() {
      userid = data['email'];
      cubeid = data['cube'];
    });

    return Scaffold(
      appBar: AppBar(
          title: const Text('Holo Cube'),
          centerTitle: true,
          backgroundColor: Colors.black87),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          Container(
            height: 100,
            alignment: AlignmentDirectional
                .centerStart, // Aligns the container to the left
            decoration: BoxDecoration(
              //color: Colors.black, // Add background color here
              borderRadius:
                  BorderRadius.circular(10), // Add rounded corners here
            ),
            child: Padding(
              padding: const EdgeInsets.all(10), // Set the desired padding here
              child: Text(
                'User ID: $userid'
                '\n'
                'Cube ID: $cubeid',
                textAlign: TextAlign.left,
                style: const TextStyle(fontSize: 15),
              ),
            ),
          ),
          Container(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.end,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                Padding(
                  padding:
                      const EdgeInsets.all(30), // Set the desired margin here
                  child: ElevatedButton(
                    onPressed: () {
                      fetchDataFromAPI(userid).then((data) {
                        String cube_data = data.toString();

                        cube_data = 's' + '$cube_data' + 'z';
                        print(cube_data);
                        //cube_data = cube_data.replaceAll('\r', '');
                        //print('initial part' + cube_data + 'final part');
                        sendDataToConnectedDevice(
                            cube_data); // Call getPairedDevices function

                        upload_pressed = true;
                        ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(
                                content: Text('Downloading Cube Data')));
                      });
                    },
                    child: const Text(
                      'Upload Cube',
                      style: TextStyle(fontSize: 20),
                    ),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.black,
                    ),
                  ),
                ),

                Padding(
                  padding:
                      const EdgeInsets.all(0), // Set the desired margin here
                  child: ElevatedButton(
                    onPressed: () {
                      //Navigator.pushNamed(context, '/cube', arguments: {});

                      upload_pressed
                          ? Navigator.pushNamed(context, '/cube',
                              arguments: {'userid': userid})
                          : ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                  content: Text('Upload Cube First')));
                    },
                    child: const Text(
                      '<<',
                      style: TextStyle(fontSize: 20),
                    ),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.black,
                    ),
                  ),
                ),
                // Add more widgets here
              ],
            ),
          ),
          Container(
            width: 300,
            height: 20,
            decoration: BoxDecoration(
              color: Colors.white, // Add background color here
              borderRadius:
                  BorderRadius.circular(10), // Add rounded corners here
            ),
            child: Text(
              upload_pressed ? 'uploaded' : 'not uploaded',
              textAlign: TextAlign.center,
            ),
          ),
          /*Container(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                Padding(
                  padding: const EdgeInsets.only(
                      left: 0,
                      right: 0,
                      top: 50,
                      bottom: 10), // Set the desired margin here
                  child: ElevatedButton(
                    onPressed: () {
                      //flag = !flag;
                      //printGyroscopeData(context);
                      //sendDataToConnectedDevice(showData);

                      upload_pressed
                          ? {
                              flag = !flag,
                              printGyroscopeData(context),
                              sendDataToConnectedDevice(showData)
                            }
                          : // Call getPairedDevices function
                          // Add your button click logic here
                          ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                  content: Text('Upload Cube First')));
                    },
                    child: const Text(
                      'Connect Gyroscope',
                      style: TextStyle(fontSize: 20),
                    ),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.black,
                    ),
                  ),
                ),
                // Add more widgets here
              ],
            ),
          ),*/
          /*Container(
            width: 350,
            height: 250,
            decoration: BoxDecoration(
              color: Colors.white, // Add background color here
              borderRadius:
                  BorderRadius.circular(10), // Add rounded corners here
            ),
            child: Text(
              'Gyroscope Data:\n\n\n $showData',
              textAlign: TextAlign.center,
            ),
          ),*/
          Padding(
            padding: EdgeInsets.only(
                top: 40), // Add your desired padding values here
            child: Container(
              width: 250,
              height: 250,
              decoration: BoxDecoration(
                image: DecorationImage(
                  image: AssetImage('assets/qrcode.png'),
                  fit: BoxFit.cover,
                ),
                borderRadius: BorderRadius.circular(10),
              ),
            ),
          )
        ],
      ),
    );
  }
}
