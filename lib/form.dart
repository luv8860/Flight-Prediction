import 'package:date_time_picker/date_time_picker.dart';
import 'package:flutter/material.dart';
import 'custombox.dart';
import 'dart:ui' show ImageFilter;

import 'custombox_result.dart';

// ignore: use_key_in_widget_constructors
class FormPage extends StatefulWidget {
  @override
  _FormPageState createState() => _FormPageState();
}

class _FormPageState extends State<FormPage> {
  // ignore: prefer_typing_uninitialized_variables
  var airline;
  // ignore: prefer_typing_uninitialized_variables
  var departure;
  // ignore: prefer_typing_uninitialized_variables
  var arrival;
  // ignore: prefer_typing_uninitialized_variables
  // ignore: non_constant_identifier_names
  var dept_time;
  var arr_time;
  // ignore: prefer_typing_uninitialized_variables
  var stops;
  var add;

  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [
                  Color.fromRGBO(32, 190, 213, 1),
                  Color.fromRGBO(84, 100, 113, 1)
                ]),
          ),
          child: Form(
            key: _formKey,
            child: Column(children: [
              const SizedBox(
                height: 30.0,
              ),
              Padding(
                padding: const EdgeInsets.all(5.0),
                child: Row(
                  children: [
                    const Text('Flight Price Prediction',
                        style: TextStyle(
                            fontFamily: 'Source Sans Pro',
                            fontWeight: FontWeight.w700,
                            color: Colors.white,
                            fontSize: 30)),
                   
                    IconButton(
                      icon: const Icon(
                        Icons.info,
                        color: Colors.white,
                      ),
                      iconSize: 30,
                      onPressed: () {
                        showGeneralDialog(
                          barrierDismissible: true,
                          barrierLabel: '',
                          barrierColor: Colors.black38,
                          transitionDuration: Duration(milliseconds: 100),
                          pageBuilder: (ctx, anim1, anim2) => CustomDialogBox(
                              title: "How to use This App",
                              descriptions:
                                  "Fill in all the details accurately and Press the Check the data button So that our Machine learning model can accurately detect the price.",
                              text: "OK"),
                          transitionBuilder: (ctx, anim1, anim2, child) =>
                              BackdropFilter(
                            filter: ImageFilter.blur(
                                sigmaX: 4 * anim1.value,
                                sigmaY: 4 * anim1.value),
                            child: FadeTransition(
                              child: child,
                              opacity: anim1,
                            ),
                          ),
                          context: context,
                        );
                      },
                    )
                  ],
                ),
              ),
              SizedBox(
                height: 30.0,
              ),
              Expanded(
                child: SingleChildScrollView(
                  physics: const BouncingScrollPhysics(),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: airline,
                              isExpanded: true,
                              hint: const Text(
                                "Airline",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>[
                                'Air India','GoAir','Jet Airways','Jet Airways Business','Multiple carriers'
                                ,'Multiple carriers Premium economy','SpiceJet','Trujet','Vistara','Vistara Premium Gconomy'
                              ].map((String value) {
                                return DropdownMenuItem<String>(
                                  value: value,
                                  child: Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                airline=value;
                                setState(() {
                                  print(value);
                                });
                              },
                            ),
                          )),
                       const SizedBox(
                        height:20.0
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: departure,
                              isExpanded: true,
                              hint: const Text(
                                "Departure Location",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>[
                                'Chennai','Delhi','Kolkata','Mumbai'
                              ].map((String value) {
                                return DropdownMenuItem<String>(
                                  value: value,
                                  child: Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                departure=value;
                                setState(() {
                                  print(value);
                                });
                              },
                            ),
                          )),
                       const SizedBox(
                        height:20.0
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: arrival,
                              isExpanded: true,
                              hint: const Text(
                                "Arrival Location",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>[
                                'Delhi','Kolkata','New Delhi','Cochin','Hyderabad'
                              ].map((String value) {
                                return DropdownMenuItem<String>(
                                  value: value,
                                  child: Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                arrival=value;
                                setState(() {
                                  print(value);
                                });
                              },
                            ),
                          )),
                       const SizedBox(
                        height:20.0
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value:stops,
                              isExpanded: true,
                              hint: Text(
                                "Total Stops",
                                style: const TextStyle(color: Colors.white),
                              ),
                              items: <String>[
                                '0','1','2','3'
                              ].map((String value) {
                                return DropdownMenuItem<String>(
                                  value: value,
                                  child: Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                stops=value;
                                setState(() {
                                  print(value);
                                });
                              },
                            ),
                          )),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: DateTimePicker(
                          type: DateTimePickerType.dateTimeSeparate,
                          dateMask: 'd MMM, yyyy',
                          initialValue: DateTime.now().toString(),
                          firstDate: DateTime(2000),
                          lastDate: DateTime(2100),
                          icon: const Icon(Icons.event),
                          dateLabelText: 'Date of Departure',
                          timeLabelText: "Hour",
                          onChanged: (value) {
                             dept_time=value;
                                setState(() {
                                  print(value);
                                });
                          },
                          validator: (val) {
                            print(val);
                            return null;
                          },
                          onSaved: (val) => print(val),
                        ),
                      ),
                      const SizedBox(
                        height:20.0
                      ),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: DateTimePicker(
                          type: DateTimePickerType.dateTimeSeparate,
                          dateMask: 'd MMM, yyyy',
                          initialValue: DateTime.now().toString(),
                          firstDate: DateTime(2000),
                          lastDate: DateTime(2100),
                          icon: const Icon(Icons.event),
                          dateLabelText: 'Date of Arrival',
                          timeLabelText: "Hour",
                          selectableDayPredicate: (date) {
                            // Disable weekend days to select from the calendar
                            if (date.weekday == 6 || date.weekday == 7) {
                              return false;
                            }

                            return true;
                          },
                          onChanged: (value) {
                             arr_time=value;
                                setState(() {
                                  print(arr_time);
                                });
                          },
                          validator: (val) {
                            print(val);
                            return null;
                          },
                          onSaved: (val) => print(val),
                        ),
                      ),
                      const SizedBox(
                        height:20.0
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: add,
                              isExpanded: true,
                              hint: const Text(
                                "Additional Information",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>[
                                '1 Short layover','2 Long layover','Business class','Change_airports','In-flight meal not included'
                                ,'No check-in baggage included','No info'
                              ].map((String value) {
                                return DropdownMenuItem<String>(
                                  value: value,
                                  child: Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                add=value;
                                setState(() {
                                  print(value);
                                });
                              },
                            ),
                          )),
                          SizedBox(
                        height: 30.0,
                      ),
                      Container(
                        height: 50,
                        margin: EdgeInsets.symmetric(horizontal: 50),
                        decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(50),
                            color: Color.fromRGBO(17, 113, 213, 1)),
                        child: Center(
                          child: ButtonTheme(
                              splashColor: Colors.transparent,
                              highlightColor: Colors.transparent,
                              minWidth: 200.0,
                              child: FlatButton(
                                  onPressed: () {
                                    showGeneralDialog(
                                      barrierDismissible: true,
                                      barrierLabel: '',
                                      barrierColor: Colors.black38,
                                      transitionDuration:
                                          Duration(milliseconds: 100),
                                      pageBuilder: (ctx, anim1, anim2) =>
                                          CustomDialogBox2(
                                              add:add,
                                              departure: departure,
                                              dept_time: dept_time,
                                              arrival: arrival,
                                              arr_time: arr_time,
                                              stops: stops,
                                              airline:airline,
                                              ),
                                      transitionBuilder:
                                          (ctx, anim1, anim2, child) =>
                                              BackdropFilter(
                                        filter: ImageFilter.blur(
                                            sigmaX: 4 * anim1.value,
                                            sigmaY: 4 * anim1.value),
                                        child: FadeTransition(
                                          child: child,
                                          opacity: anim1,
                                        ),
                                      ),
                                      context: context,
                                    );
                                  },
                                  child: Text(
                                    "Check The Data",
                                    style: TextStyle(
                                        color: Colors.white,
                                        fontWeight: FontWeight.bold),
                                  ))),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ]),
          )),
    );
  }
}
