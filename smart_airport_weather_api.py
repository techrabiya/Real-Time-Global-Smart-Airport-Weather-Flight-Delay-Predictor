print("--- API Challenge 1 Initialized: Airport Weather Stream ✈️ ---")

def fetch_and_analyze_airport_weather(api_json_response):
    print(f"Processing live API payload for airport: {api_json_response.get('airport_code')}")
    
    visibility = api_json_response.get('visibility_meters', 10000)
    wind_speed = api_json_response.get('wind_speed_knots', 10.0)
    
    try:
        if visibility < 1000:
            print("API Data Alert: Dense fog or low visibility detected from live feed.")
            return "critical flight delay and diversion advisory issued"
        elif wind_speed > 35.0:
            if visibility < 3000:
                print("API Risk Log: High crosswinds coupled with reduced visibility.")
                return "temporary runway operations hold activated"
            else:
                print("API Warning: High wind speed warning logged.")
                return "cautionary crosswind landing advisory"
        else:
            print("API Status: Weather conditions are optimal.")
            return "nominal flight operations greenlit"
            
    except Exception as e:
        print(f"API Error Caught: Failed to parse payload -> {e}")
        return "api exception safely handled"

mock_api_payload_1 = {"airport_code": "BOM", "visibility_meters": 800, "wind_speed_knots": 15.0}
print("\nRunning API Test 1:")
print(fetch_and_analyze_airport_weather(mock_api_payload_1))
