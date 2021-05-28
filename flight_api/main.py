from flask import Flask,jsonify,request
import json
import numpy
import pandas as pd
import pickle
app=Flask(__name__)

Airline_Air_India=0
Airline_GoAir=0
Airline_IndiGo=0
Airline_Jet_Airways=0
Airline_Jet_Airways_Business=0
Airline_Multiple_carriers=0
Airline_Multiple_carriers_Premium_economy=0
Airline_SpiceJet=0
Airline_Trujet=0
Airline_Vistara=0
Airline_Vistara_Premium_economy=0

Source_Chennai=0
Source_Delhi=0
Source_Kolkata=0
Source_Mumbai=0

Destination_Cochin=0
Destination_Delhi=0
Destination_Hyderabad=0
Destination_Kolkata=0
Destination_New_Delhi=0

Additional_Info_1_Short_layover=0
Additional_Info_2_Long_layover=0
Additional_Info_Business_class=0
Additional_Info_Change_airports=0
Additional_Info_In_flight_meal_not_included=0
Additional_Info_No_check_in_baggage_included=0
Additional_Info_No_info=0
Additional_Info_Red_eye_flight=0
@app.route('/',methods=['GET',"POST"])
def value():
    if request.method == "POST":
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))

        tot_stops= request_data['tot_stops']  # done
        departure = request_data['departure']
        arrival= request_data['arrival']
        airline=request_data['airline']
        additional_info=request_data['additional']
        source = request_data['source']
        destination = request_data['destination']

        dep_hour = pd.to_datetime(departure,format='%Y-%m-%d %H:%M').hour
        dep_min = pd.to_datetime(departure,format='%Y-%m-%d %H:%M').minute
        arrival_hour = pd.to_datetime(arrival,format='%Y-%m-%d %H:%M').hour
        arrival_min = pd.to_datetime(arrival,format='%Y-%m-%d %H:%M').minute

        t1=pd.to_datetime(departure,format='%Y-%m-%d %H:%M')
        t2 = pd.to_datetime(arrival, format='%Y-%m-%d %H:%M')

        duration_hours=int(str(t2-t1).split()[0])*24+int(str(t2-t1).split()[2].split(':')[0])
        duration_mins=int(str(t2-t1).split()[2].split(':')[1])

        journey_day = pd.to_datetime(departure, format='%Y-%m-%d %H:%M').day
        journey_month = pd.to_datetime(departure,format='%Y-%m-%d %H:%M').month
        journey_year = pd.to_datetime(departure, format='%Y-%m-%d %H:%M').year

        if arrival=="Air India":
            Airline_Air_India = 1
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif arrival=="GoAir":
            Airline_Air_India = 0
            Airline_GoAir = 1
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif arrival=="IndiGo":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 1
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif arrival=="Jet Airways":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 1
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif arrival=="Jet Airways Business":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 1
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif arrival=="Multiple carriers":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 1
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif arrival=="Multiple carriers Premium economy":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif arrival=="SpiceJet":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 1
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif arrival=="Trujet":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 1
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        elif arrival=="Vistara":
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 1
            Airline_Vistara_Premium_economy = 0
        else :
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Trujet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 1

        if source=="Chennai":
            Source_Chennai = 1
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
        elif source=="Delhi":
            Source_Chennai = 0
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
        elif source=="Kolkata":
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
        else:
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1

        if destination=="Cochin":
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi = 0
        elif destination=="Delhi":
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi = 0
        elif destination=="Hyderabad":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0
            Destination_New_Delhi = 0
        elif destination=="Kolkata":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1
            Destination_New_Delhi = 0
        else:
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi = 1

        if additional_info=="1 Short layover":
            Additional_Info_1_Short_layover = 1
            Additional_Info_2_Long_layover = 0
            Additional_Info_Business_class = 0
            Additional_Info_Change_airports = 0
            Additional_Info_In_flight_meal_not_included = 0
            Additional_Info_No_check_in_baggage_included = 0
            Additional_Info_No_info = 0
            Additional_Info_Red_eye_flight = 0
        elif additional_info=="2 Long layover":
            Additional_Info_1_Short_layover = 0
            Additional_Info_2_Long_layover = 1
            Additional_Info_Business_class = 0
            Additional_Info_Change_airports = 0
            Additional_Info_In_flight_meal_not_included = 0
            Additional_Info_No_check_in_baggage_included = 0
            Additional_Info_No_info = 0
            Additional_Info_Red_eye_flight = 0
        elif additional_info=="Business class":
            Additional_Info_1_Short_layover = 0
            Additional_Info_2_Long_layover = 0
            Additional_Info_Business_class = 1
            Additional_Info_Change_airports = 0
            Additional_Info_In_flight_meal_not_included = 0
            Additional_Info_No_check_in_baggage_included = 0
            Additional_Info_No_info = 0
            Additional_Info_Red_eye_flight = 0
        elif additional_info=="Change_airports":
            Additional_Info_1_Short_layover = 0
            Additional_Info_2_Long_layover = 0
            Additional_Info_Business_class = 0
            Additional_Info_Change_airports = 1
            Additional_Info_In_flight_meal_not_included = 0
            Additional_Info_No_check_in_baggage_included = 0
            Additional_Info_No_info = 0
            Additional_Info_Red_eye_flight = 0
        elif additional_info=="In-flight meal not included":
            Additional_Info_1_Short_layover = 0
            Additional_Info_2_Long_layover = 0
            Additional_Info_Business_class = 0
            Additional_Info_Change_airports = 0
            Additional_Info_In_flight_meal_not_included = 1
            Additional_Info_No_check_in_baggage_included = 0
            Additional_Info_No_info = 0
            Additional_Info_Red_eye_flight = 0
        elif additional_info=="No check-in baggage included":
            Additional_Info_1_Short_layover = 0
            Additional_Info_2_Long_layover = 0
            Additional_Info_Business_class = 0
            Additional_Info_Change_airports = 0
            Additional_Info_In_flight_meal_not_included = 0
            Additional_Info_No_check_in_baggage_included = 1
            Additional_Info_No_info = 0
            Additional_Info_Red_eye_flight = 0
        elif additional_info=="No info":
            Additional_Info_1_Short_layover = 0
            Additional_Info_2_Long_layover = 0
            Additional_Info_Business_class = 0
            Additional_Info_Change_airports = 0
            Additional_Info_In_flight_meal_not_included = 0
            Additional_Info_No_check_in_baggage_included = 0
            Additional_Info_No_info = 1
            Additional_Info_Red_eye_flight = 0
        else:
            Additional_Info_1_Short_layover = 0
            Additional_Info_2_Long_layover = 0
            Additional_Info_Business_class = 0
            Additional_Info_Change_airports = 0
            Additional_Info_In_flight_meal_not_included = 0
            Additional_Info_No_check_in_baggage_included = 0
            Additional_Info_No_info = 0
            Additional_Info_Red_eye_flight = 1

        d = {
            'tot_stops': int(tot_stops),
            'duration_hours': int(duration_hours),
            'duration_mins': int(duration_mins),
            'dep_hour': dep_hour,
            'dep_min': dep_min,
            'arrival_hour': arrival_hour,
            'arrival_min': arrival_min,
            'journey_day': journey_day,
            'journey_month': journey_month,
            'journey_year': journey_year,
            'Airline_Air_India': Airline_Air_India,
            'Airline_GoAir': Airline_GoAir,
            'Airline_IndiGo': Airline_IndiGo,
            'Airline_Jet_Airways': Airline_Jet_Airways,
            'Airline_Jet_Airways_Business': Airline_Jet_Airways_Business,
            'Airline_Multiple_carriers': Airline_Multiple_carriers,
            'Airline_Multiple_carriers_Premium_economy': Airline_Multiple_carriers_Premium_economy,
            'Airline_SpiceJet': Airline_SpiceJet,
            'Airline_Trujet': Airline_Trujet,
            'Airline_Vistara': Airline_Vistara,
            'Airline_Vistara_Premium_economy': Airline_Vistara_Premium_economy,
            'Source_Chennai': Source_Chennai,
            'Source_Delhi': Source_Delhi,
            'Source_Kolkata': Source_Kolkata,
            'Source_Mumbai': Source_Mumbai,
            'Destination_Cochin': Destination_Cochin,
            'Destination_Delhi': Destination_Delhi,
            'Destination_Hyderabad': Destination_Hyderabad,
            'Destination_Kolkata': Destination_Kolkata,
            'Destination_New_Delhi': Destination_New_Delhi,
            'Additional_Info_1_Short_layover': Additional_Info_1_Short_layover,
            'Additional_Info_2_Long_layover': Additional_Info_2_Long_layover,
            'Additional_Info_Business_class': Additional_Info_Business_class,
            'Additional_Info_Change_airports': Additional_Info_Change_airports,
            'Additional_Info_In_flight_meal_not_included': Additional_Info_In_flight_meal_not_included,
            'Additional_Info_No_check_in_baggage_included': Additional_Info_No_check_in_baggage_included,
            'Additional_Info_No_info': Additional_Info_No_info,
            'Additional_Info_Red_eye_flight': Additional_Info_Red_eye_flight,
        }
        try:
            df = pd.DataFrame(data=d, index=[0])
            print(df)
            loaded_model = pickle.load(open(r"predictor", "rb"))
            y_pred = loaded_model.predict(df.values)
            print(y_pred)
            return jsonify({'result': int(y_pred[0])})
        except Exception as e:
            return jsonify({'result': str(e) + "ERROR"})
    else:
        return ''

if __name__=="__main__":
    app.run(debug=True)
