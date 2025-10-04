#!/usr/bin/env python3
"""
Test script to verify the cities search functionality
"""

# Test the search function directly
INDIAN_CITIES = [
    {"name": "Mumbai", "state": "Maharashtra", "lat": 19.0760, "lon": 72.8777, "pincode": "400001"},
    {"name": "Delhi", "state": "Delhi", "lat": 28.6139, "lon": 77.2090, "pincode": "110001"},
    {"name": "Bangalore", "state": "Karnataka", "lat": 12.9716, "lon": 77.5946, "pincode": "560001"},
    {"name": "Goa", "state": "Goa", "lat": 15.2993, "lon": 74.1240, "pincode": "403001"},
    {"name": "Pune", "state": "Maharashtra", "lat": 18.5204, "lon": 73.8567, "pincode": "411001"},
]

def search_indian_cities(query, limit=10):
    """Search for Indian cities based on query string"""
    query = query.lower().strip()
    results = []
    
    print(f"Searching for: '{query}'")
    
    for city in INDIAN_CITIES:
        print(f"Checking city: {city['name']}")
        # Search in city name, state, and pincode
        if (query in city["name"].lower() or 
            query in city["state"].lower() or 
            query == city["pincode"] or
            query in city["pincode"]):
            
            print(f"✅ Match found: {city['name']}")
            # Format the result
            result = {
                "name": city["name"],
                "lat": city["lat"],
                "lon": city["lon"],
                "address": f"{city['name']}, {city['state']}, India",
                "country": "India",
                "state": city["state"],
                "city": city["name"],
                "pincode": city["pincode"]
            }
            results.append(result)
            
            if len(results) >= limit:
                break
    
    print(f"Found {len(results)} results")
    return results

if __name__ == "__main__":
    print("Testing city search functionality...")
    
    # Test searches
    test_queries = ["Mumbai", "Goa", "Delhi", "Pune", "400001"]
    
    for query in test_queries:
        print(f"\n--- Testing: {query} ---")
        results = search_indian_cities(query)
        for result in results:
            print(f"  - {result['name']}, {result['state']}")
    
    print("\nTest completed!")
