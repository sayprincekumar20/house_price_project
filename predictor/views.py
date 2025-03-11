import joblib
import numpy as np
import pandas as pd
from django.shortcuts import render

# Load trained model
model = joblib.load("housing_model.joblib")

# Define feature lists
numeric_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking',
                    'total_bed_bath', 'luxury_score', 'comfort', 'space_capacity',
                    'accessibility', 'total_rooms', 'amenities', 'space_per_rooms',
                    'bathroom_parking', 'bedroom_parking', 'accessibility_score',
                    'basement_heating', 'total_utilities']

categorical_binary = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                      'airconditioning', 'prefarea', 'large_house']

furnishing_options = ['furnish_furnished', 'furnish_semi-furnished', 'furnish_unfurnished']

FEATURE_COLUMNS = numeric_features + categorical_binary + furnishing_options

def home(request):
    if request.method == "POST":
        form_data = {}
        missing_fields = []

        # Validate numerical features
        for feature in numeric_features:
            value = request.POST.get(feature)
            if value is None or value.strip() == "":
                missing_fields.append(feature)
            else:
                form_data[feature] = float(value)

        # Validate binary categorical features (Yes/No → 1/0)
        for feature in categorical_binary:
            value = request.POST.get(feature)
            if value is None:
                missing_fields.append(feature)
            else:
                form_data[feature] = 1 if value == "Yes" else 0

        # Validate furnishing options (one-hot encoding)
        selected_furnishing = request.POST.get("furnishing")
        if selected_furnishing not in furnishing_options:
            missing_fields.append("furnishing")
        for option in furnishing_options:
            form_data[option] = 1 if option == selected_furnishing else 0

        # If there are missing fields, return an error
        if missing_fields:
            return render(request, 'home.html', {
                'error': f"Missing input for: {', '.join(missing_fields)}",
                'numeric_features': numeric_features,
                'categorical_binary': categorical_binary,
                'furnishing_options': furnishing_options
            })

        # Convert to Pandas DataFrame
        input_data = pd.DataFrame([form_data], columns=FEATURE_COLUMNS)
        
        # Make prediction
        prediction = model.predict(input_data)[0]/100
        
        return render(request, 'home.html', {
            'prediction': prediction,
            'numeric_features': numeric_features,
            'categorical_binary': categorical_binary,
            'furnishing_options': furnishing_options
        })

    return render(request, 'home.html', {
        'numeric_features': numeric_features,
        'categorical_binary': categorical_binary,
        'furnishing_options': furnishing_options
    })
