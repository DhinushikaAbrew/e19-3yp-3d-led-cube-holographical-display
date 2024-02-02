import 'package:flutter/material.dart';

void loginForm(TextEditingController emailController,
    TextEditingController passwordController, BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text('Login'),
        content: SingleChildScrollView(
          child: ListBody(
            children: [
              Padding(
                padding: EdgeInsets.symmetric(vertical: 6.0),
                child: TextField(
                  controller: emailController,
                  decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Email',
                  ),
                ),
              ),
              Padding(
                padding: EdgeInsets.symmetric(vertical: 6.0),
                child: TextField(
                  controller: passwordController,
                  decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Password',
                  ),
                ),
              ),
            ],
          ),
        ),
        actions: [
          TextButton(
            child: Text('Login'),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}
