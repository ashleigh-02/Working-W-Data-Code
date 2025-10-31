# Working-W-Data-Code
WWDC A2 2025
https://github.com/ashleigh-02/WorkingW-code-

#MyWeatherWardrobe 

Table of contents: 
Intro  
Features
Architecture 
Setup & running 
User Use
Future Improvements 
Licence & Acknowledgments 


#Intro:
This application aims to solve the problem of chosing the outfit for the weather by suggesting users outfits based on weather API. It is built using the Anvil platform, enabling full-stack Python (client + server) development.

#Features: 
- User inputs a location (city name)
- Input is sanitised before sending
- App calls server-side code to access weather data securely
- Data parsed to extract temperature and condition
- Conditional logic returns a clothing suggestion (with emojis/icons)
- Multi-screen UI: one form for input, another for results
- Easy navigation: back button to return to the input screen

#Architecture:
**Client (Forms)**
In Form1:
Presents a TextBox for city input
A Button triggers button_1_click()
Calls: anvil.server.call("get_weather", city)
On success: uses open_form('WeatherForm', city=…, weather=…) to navigate
Displays labels and image/icon for results

In WeatherForm:
Receives city and weather data from server
Displays weather information and clothing suggestion
Back button (button_back_click) navigates back to Form1 via open_form('Form1')

**Server Module**
In ServerModule1:
Securely uses OpenWeather API key (hidden from UI)
Defines @anvil.server.callable def get_weather(location): …
Uses requests library to fetch weather JSON
Extracts temp and condition from response
Passes them to a helper function suggest_clothing(temp, condition)
That helper uses control flow (if/elif) to decide suggestion
Returns a dictionary: {"success": True, "temp": …, "condition": …, "suggestion": …}


#Setup & Running:
1. Clone or create a new Anvil app.
2. In Assets, upload any icon/image files (for singlet, jacket, umbrella etc.).
3. In Server Module, insert your OpenWeather API key.
4. In Form1, wire components: text_box_1, button_1, image_icon, label_weather, label_suggestion.
5. In WeatherForm, wire: label_weather_info, label_suggestion, button_back.
6. Run the app: Enter city → submit → navigate to results → optionally go back.
7. Publish when ready for users.

#User use:
1. Open the appilcation link (no software required)
2. Enter desired location (city)in text box
3. Click 'tick' botton
4. View suggested outfits

#Future Improvements
- Insert User Wardrobe 
- Offer localisation (°F, other units) or more nuanced clothing logic
- Persist user settings or history in a Data Table
- Add responsive styling and themes for mobile devices


#License & Acknowledgements
Built with Anvil — see documentation at https://anvil.works/docs
Weather data via OpenWeather API — see https://openweathermap.org/api
Code and logic written by Ashleigh Walker
