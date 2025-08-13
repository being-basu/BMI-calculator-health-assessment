# BMI Health Assessment

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Return the BMI category based on value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_health_advice(category):
    """Provide basic health tips based on BMI category."""
    advice = {
        "Underweight": "Increase calorie intake with healthy foods and consult a nutritionist.",
        "Normal weight": "Maintain a balanced diet and regular exercise.",
        "Overweight": "Focus on a calorie-controlled diet and increase physical activity.",
        "Obese": "Seek professional medical advice and start a monitored weight loss plan."
    }
    return advice[category]

def main():
    print("===== BMI Calculator & Health Risk Assessment =====")
    
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender (M/F): ")
    
    try:
        height_cm = float(input("Enter your height in cm: "))
        weight_kg = float(input("Enter your weight in kg: "))
    except ValueError:
        print("❌ Invalid input! Please enter numeric values for height and weight.")
        return
    
    height_m = height_cm / 100  # convert cm to meters
    bmi = calculate_bmi(weight_kg, height_m)
    category = get_bmi_category(bmi)
    advice = get_health_advice(category)
    
    print("\n===== Health Report =====")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print(f"Health Advice: {advice}")

if __name__ == "__main__":
    main()
