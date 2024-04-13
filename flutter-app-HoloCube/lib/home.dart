import 'package:flutter/material.dart';
import 'package:my_app/login.dart';
import 'package:my_app/bluetooth.dart';

final TextEditingController emailController = TextEditingController();
final TextEditingController passwordController = TextEditingController();

class Home extends StatefulWidget {
  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String cube_connection_status = 'Disconnected';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          title: Text('Holo Cube'),
          centerTitle: true,
          backgroundColor: Colors.black87),
      body: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Container(
              height: 75, // Set the desired width here

              child: Row(
                mainAxisAlignment: MainAxisAlignment.end,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  ElevatedButton(
                    onPressed: () async {
                      // Add your button click logic here
                      loginForm(emailController, passwordController, context);
                    },
                    child: Text(
                      'Login',
                      style: TextStyle(fontSize: 20),
                    ),
                    style: ElevatedButton.styleFrom(
                      primary: Colors.black,
                    ),
                  ),
                  // Add more widgets here
                ],
              ),
            ),
            Container(
              height: 125,
              child: Center(
                child: Image.asset(
                  'assets/logo.png', // Replace with your image path
                  height: 150,
                  width: 150,
                ),
              ),
            ),
            Container(
              height: 75,
              child: Center(
                child: Text(
                  '$cube_connection_status to cube',
                  style: TextStyle(
                    fontSize: 25,
                    fontWeight: FontWeight.bold,
                    color: Colors.black,
                  ),
                ),
              ),
            ),
            Container(
              height: 75,
              child: Center(
                child: Text(
                  '$connection_name',
                  style: TextStyle(
                    fontSize: 25,
                    fontWeight: FontWeight.bold,
                    color: Colors.black,
                  ),
                ),
              ),
            ),
            Container(
              height: 200,
              width: 300,
              decoration: BoxDecoration(
                color: Colors.black, // Add background color here
                borderRadius:
                    BorderRadius.circular(10), // Add rounded corners here
              ),
              child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: <Widget>[
                    ElevatedButton(
                      onPressed: () {
                        enableBluetooth();
                        ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(content: Text('Bluetooth enabled')));
                        // Add your button click logic here
                      },
                      child: Text(
                        'Enable Bluetooth',
                        style: TextStyle(fontSize: 20),
                      ),
                      style: ElevatedButton.styleFrom(
                        primary: Colors.black54,
                      ),
                    ),
                    ElevatedButton(
                      onPressed: () async {
                        await getPairedDevices(context);
                        bool isconnected = await isDeviceConnected();

                        if (isconnected == true) {
                          setState(() {
                            cube_connection_status = 'connected';
                          });
                        } else {
                          setState(() {
                            cube_connection_status = 'Disconnected';
                          });
                        }

                        // Add your button click logic here
                      },
                      child: Text(
                        'Connect to cube',
                        style: TextStyle(fontSize: 20),
                      ),
                      style: ElevatedButton.styleFrom(
                        primary: Colors.black54,
                      ),
                    ),
                    ElevatedButton(
                      onPressed: () {
                        print(connection_name);
                        if (/*passwordController.text == 'admin' && emailController.text == 'uthsaraiw@gmail'*/
                            cube_connection_status != 'connected') {
                          Navigator.pushNamed(context, '/user', arguments: {
                            'email': emailController.text,
                            'password': passwordController.text,
                            'cube': connection_name,
                          });
                        } else {
                          ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                  content: Text(
                                      'login or connection to cube failed')));
                        } // Add your button click logic here
                      },
                      child: Text(
                        'Next',
                        style: TextStyle(fontSize: 20),
                      ),
                      style: ElevatedButton.styleFrom(
                        primary: Colors.black,
                      ),
                    ),
                  ]),
            ),
          ],
        ),
      ),
    );
  }
}
