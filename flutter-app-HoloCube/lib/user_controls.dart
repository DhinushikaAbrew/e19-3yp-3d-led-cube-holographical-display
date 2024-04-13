import 'package:flutter/material.dart';
import 'package:my_app/bluetooth.dart';
import 'package:my_app/user.dart';

class UserControls extends StatefulWidget {
  UserControls({Key? key}) : super(key: key);

  @override
  State<UserControls> createState() => _UserControlsState();
}

class _UserControlsState extends State<UserControls> {
  @override
  Widget build(BuildContext context) {
    Map data = {};
    String userid = '';
    data = ModalRoute.of(context)!.settings.arguments as Map;

    setState(() {
      userid = data['userid'];
    });

    double y = 170; //move num plate up and down
    double x = 100; //move num plate and rotate left and right
    double z = -30; //rotate rotate plate top and bottom
    return Scaffold(
      backgroundColor: Colors.white,
      body: Stack(
        children: [
          Positioned(
            child: Container(),
          ),
          //images
          Positioned(
            left: 170,
            top: 100 + z,
            child: Transform.rotate(
              angle: 1.5708,
              child: Image.asset(
                'assets/left1.png',
                width: 125,
                height: 170,
              ),
            ),
          ),

          Positioned(
            child: Container(),
          ),
          //images

          Positioned(
            left: 100,
            top: 110 + z,
            child: Transform.rotate(
              angle: 1.5708,
              child: Image.asset(
                'assets/left2down.png',
                width: 50,
                height: 50,
              ),
            ),
          ),
          Positioned(
            left: 100,
            top: 220 + z,
            child: Transform.rotate(
              angle: 1.5708,
              child: Image.asset(
                'assets/left2up.png',
                width: 50,
                height: 50,
              ),
            ),
          ),

          Positioned(
            left: x,
            top: 350 + y,
            child: Transform.rotate(
              angle: 1.5708,
              child: Image.asset(
                'assets/numlbot.png',
                width: 50,
                height: 50,
              ),
            ),
          ),

          Positioned(
            left: x + 65,
            top: 350 + y,
            child: Transform.rotate(
              angle: 1.5708,
              child: Image.asset(
                'assets/numlmid.png',
                width: 50,
                height: 50,
              ),
            ),
          ),

          Positioned(
            left: x + 130,
            top: 350 + y,
            child: Transform.rotate(
              angle: 1.5708,
              child: Image.asset(
                'assets/numltop.png',
                width: 50,
                height: 50,
              ),
            ),
          ),

          Positioned(
            left: x,
            top: 430 + y,
            child: Transform.rotate(
              angle: 1.5708,
              child: Image.asset(
                'assets/numrbot.png',
                width: 50,
                height: 50,
              ),
            ),
          ),

          Positioned(
            left: x + 65,
            top: 430 + y,
            child: Transform.rotate(
              angle: 1.5708,
              child: Image.asset(
                'assets/numrmid.png',
                width: 50,
                height: 50,
              ),
            ),
          ),

          Positioned(
            left: x + 130,
            top: 430 + y,
            child: Transform.rotate(
              angle: 1.5708,
              child: Image.asset(
                'assets/numrtop.png',
                width: 50,
                height: 50,
              ),
            ),
          ),
          Positioned(
            left: x + 30,
            top: 200,
            child: Transform.rotate(
              angle: 1.5708, // 90 degrees in radians
              child: Image.asset(
                'assets/rightrotate.png',
                width: 150,
                height: 350,
              ),
            ),
          ),

//controller-bottom
          Positioned(
            left: 165,
            top: 140,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('controller-bottom');
                  sendDataToConnectedDevice('s1z');
                },
              ),
            ),
          ),

          //controller-top
          Positioned(
            left: 250,
            top: 130,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('controller-top');
                  sendDataToConnectedDevice('s2z');
                },
              ),
            ),
          ),

          //controller-right
          Positioned(
            left: 210,
            top: 170,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('controller-right');
                  sendDataToConnectedDevice('s3z');
                },
              ),
            ),
          ),

          //controller-left
          Positioned(
            left: 210,
            top: 90,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('controller-left');
                  sendDataToConnectedDevice('s4z');
                },
              ),
            ),
          ),
/*
          //controller-middle
          Positioned(
            left: 140,
            top: 155,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('controller-middle');
                  sendDataToConnectedDevice('s5z');
                },
                child: Material(
                  color: Colors.blue,
                  child: Container(
                    width: 50,
                    height: 50,
                    decoration: BoxDecoration(),
                  ),
                ),
              ),
            ),
          ),*/

          //middle +
          Positioned(
            left: 100,
            top: 80,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('middle +');
                  sendDataToConnectedDevice('s6z');
                },
              ),
            ),
          ),

          //middle -
          Positioned(
            left: 100,
            top: 190,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('middle -');
                  sendDataToConnectedDevice('s7z');
                },
              ),
            ),
          ),

          //right - numlbottom
          Positioned(
            left: 100,
            top: 520,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('numlbottom');
                  sendDataToConnectedDevice('s8z');
                },
              ),
            ),
          ),

          //right - numlmid
          Positioned(
            left: 165,
            top: 520,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('numlmid');
                  sendDataToConnectedDevice('s9z');
                },
              ),
            ),
          ),

          //right - numltop
          Positioned(
            left: 230,
            top: 520,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('right - numltop');
                  sendDataToConnectedDevice('s10z');
                },
              ),
            ),
          ),

          //right - numrbottom
          Positioned(
            left: 100,
            top: 600,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('numrbottom');
                  sendDataToConnectedDevice('s11z');
                },
              ),
            ),
          ),

          //right - numrmid
          Positioned(
            left: 165,
            top: 600,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  debugPrint('numrmid');
                  sendDataToConnectedDevice('s12z');
                },
              ),
            ),
          ),

          //right - numrtop
          Positioned(
            left: 230,
            top: 600,
            child: Transform.rotate(
              angle: 0,
              child: Container(
                width: 50,
                height: 50,
                decoration: BoxDecoration(),
                child: GestureDetector(
                  onTap: () {
                    debugPrint('numrtop');
                    sendDataToConnectedDevice('s13z');
                  },
                ),
              ),
            ),
          ),

          //right - ROTATE
          Positioned(
            left: 170,
            top: 300,
            child: Container(
              width: 70,
              height: 150,
              decoration: BoxDecoration(),
              child: GestureDetector(
                onTap: () {
                  fetchDataFromAPI(userid).then((data) {
                    String cube_data = data.toString();

                    cube_data = 's' + '$cube_data' + 'z';
                    //cube_data = cube_data.replaceAll('\r', '');
                    //print('initial part' + cube_data + 'final part');
                    sendDataToConnectedDevice(
                        cube_data); // Call getPairedDevices function
                  });
                },
                /*child: Material(
                  color: Colors.blue,
                  child: Container(
                    width: 50,
                    height: 50,
                    decoration: BoxDecoration(),
                  ),
                ),*/
              ),
            ),
          ),
        ],
      ),
    );
  }
}
