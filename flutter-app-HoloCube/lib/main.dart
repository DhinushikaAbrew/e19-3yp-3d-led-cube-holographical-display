import 'package:flutter/material.dart';
import 'package:my_app/home.dart';
import 'package:my_app/user.dart';
import 'package:my_app/user_controls.dart';

void main() => runApp(MaterialApp(
      //home: UserControls(),

      routes: {
        '/': (context) => Home(),
        '/user': (context) => User(),
        '/cube': (context) => UserControls(),
      },
    ));
