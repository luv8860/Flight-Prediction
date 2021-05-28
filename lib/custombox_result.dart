import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'custombox.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Constants {
  Constants._();
  static const double padding = 20;
  static const double avatarRadius = 45;
}

class CustomDialogBox2 extends StatefulWidget {

  final String airline;
  final String departure;
  final String arrival;
  final String dept_time;
  final String arr_time;
  final String stops;
  final String add;
  const CustomDialogBox2(
      {Key? key,
      required this.airline,
      required this.departure,
      required this.arrival,
      required this.dept_time,
      required this.arr_time,
      required this.stops,
      required this.add
      })
      : super(key: key);

  @override
  // ignore: no_logic_in_create_state
  _CustomDialogBox2State createState() => _CustomDialogBox2State(
      airline,departure,arrival,dept_time,arr_time,stops,add
      );
}

class _CustomDialogBox2State extends State<CustomDialogBox2> {
final String airline;
  final String departure;
  final String arrival;
  final String dept_time;
  final String arr_time;
  final String stops;
  final String add;
  _CustomDialogBox2State(
      this.airline,
      this.departure,
      this.arrival,
       this.dept_time,
      this.arr_time,
      this.stops,
      this.add);
  String url = "https://flight-pred01.herokuapp.com/";
  var urll;
  void getname() async {
    print("$departure,$arrival,$dept_time,$arr_time,$stops,$add");
    var send = await http.post(Uri.parse(url),
        headers: {'Content-Type': 'application/json'},
        body: json.encode(
            {
              'airline':airline,
              'source':departure,
              'destination':arrival,
              'departure':dept_time,
              'arrival':arr_time,
              'tot_stops':stops,
              'additional':add   
                
              }
            ));
    final decode = json.decode(send.body);
    setState(() {
      print(decode.toString() + 'main');
      urll = decode['result'];
      print(urll);
    });
  }

  @override
  void initState() {
    super.initState();
    getname();
  }

  @override
  Widget build(BuildContext context) {
    if (urll == null) {
      return Center(
          // ignore: sized_box_for_whitespace
          child: Container(
              height: 200, width: 200, child: const CircularProgressIndicator()));
    } else {
      return CustomDialogBox(
          title: "Result",
          descriptions: "The Total Cost is : $urll",
          text: "OK",);
    }
  }
}
