import 'package:flutter/material.dart';
import 'package:get/get.dart';

class RootScreen extends StatefulWidget {
  const RootScreen({super.key});

  @override
  State<RootScreen> createState() => _RootScreenState();
}

class _RootScreenState extends State<RootScreen> {
  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      home: Scaffold(
        body: const Center(
          child: Text('Root Screen'),
        ),
      ),
    );
  }
}
