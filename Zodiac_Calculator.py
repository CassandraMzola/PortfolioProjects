def get_zodiac_sign(day, month):
    if month < 1 or month > 12 or day < 1 or day > 31:
        return "Invalid date"

    # Determines the Zodiac sign based on day and month
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    else:
        return "Invalid date"

def get_zodiac_details(zodiac_sign):
    details = {
        "Aquarius": "Original, inventive, humanitarian, independent",
        "Pisces": "Compassionate, artistic, intuitive, gentle",
        "Aries": "Courageous, determined, confident, enthusiastic",
        "Taurus": "Reliable, patient, practical, devoted",
        "Gemini": "Adaptable, curious, affectionate, quick-witted",
        "Cancer": "Intuitive, sentimental, compassionate, protective",
        "Leo": "Generous, warm-hearted, creative, enthusiastic",
        "Virgo": "Loyal, analytical, kind, hardworking",
        "Libra": "Cooperative, diplomatic, gracious, fair-minded",
        "Scorpio": "Resourceful, brave, passionate, stubborn",
        "Sagittarius": "Generous, idealistic, great sense of humor",
        "Capricorn": "Responsible, disciplined, self-control, good managers"
    }
    return details.get(zodiac_sign, "No details available")

def get_zodiac_element(zodiac_sign):
    elements = {
        "Aquarius": "Air",
        "Pisces": "Water",
        "Aries": "Fire",
        "Taurus": "Earth",
        "Gemini": "Air",
        "Cancer": "Water",
        "Leo": "Fire",
        "Virgo": "Earth",
        "Libra": "Air",
        "Scorpio": "Water",
        "Sagittarius": "Fire",
        "Capricorn": "Earth"
    }
    return elements.get(zodiac_sign, "Unknown element")

def get_zodiac_symbol(zodiac_sign):
    symbols = {
        "Aquarius": "Water Bearer",
        "Pisces": "Fish",
        "Aries": "Ram",
        "Taurus": "Bull",
        "Gemini": "Twins",
        "Cancer": "Crab",
        "Leo": "Lion",
        "Virgo": "Maiden",
        "Libra": "Scales",
        "Scorpio": "Scorpion",
        "Sagittarius": "Archer",
        "Capricorn": "Goat"
    }
    return symbols.get(zodiac_sign, "Unknown symbol")

def get_zodiac_history(zodiac_sign):
    history = {
        "Aquarius": "In ancient Greek mythology, Aquarius is associated with Ganymede, the cupbearer to the gods.",
        "Pisces": "Pisces is associated with Aphrodite and Eros, who transformed into fish to escape the monster Typhon.",
        "Aries": "Aries is associated with the golden ram that saved Phrixus and Helle, children of King Athamas.",
        "Taurus": "In Greek mythology, Taurus is associated with the myth of the Minotaur.",
        "Gemini": "In Greek mythology, Gemini represents the twins Castor and Pollux.",
        "Cancer": "Cancer is associated with the crab that bit Hercules during his battle with the Hydra.",
        "Leo": "Leo is associated with the Nemean Lion slain by Hercules.",
        "Virgo": "Virgo is associated with Astraea, the goddess of innocence and purity.",
        "Libra": "Libra is associated with the scales of justice held by Themis, the Greek personification of divine law and custom.",
        "Scorpio": "Scorpio is associated with the scorpion that stung Orion in Greek mythology.",
        "Sagittarius": "Sagittarius is associated with the centaur Chiron, known for his wisdom and knowledge.",
        "Capricorn": "Capricorn is associated with the sea-goat, a mythological creature with the upper body of a goat and the lower body of a fish."
    }
    return history.get(zodiac_sign, "No historical background available")

def get_zodiac_compatibility(zodiac_sign):
    compatibility = {
        "Aquarius": "Best matches: Gemini, Libra. Challenges: Taurus, Scorpio.",
        "Pisces": "Best matches: Cancer, Scorpio. Challenges: Gemini, Sagittarius.",
        "Aries": "Best matches: Leo, Sagittarius. Challenges: Cancer, Capricorn.",
        "Taurus": "Best matches: Cancer, Virgo. Challenges: Leo, Aquarius.",
        "Gemini": "Best matches: Libra, Aquarius. Challenges: Virgo, Pisces.",
        "Cancer": "Best matches: Scorpio, Pisces. Challenges: Aries, Libra.",
        "Leo": "Best matches: Aries, Sagittarius. Challenges: Taurus, Scorpio.",
        "Virgo": "Best matches: Taurus, Capricorn. Challenges: Gemini, Sagittarius.",
        "Libra": "Best matches: Gemini, Aquarius. Challenges: Cancer, Capricorn.",
        "Scorpio": "Best matches: Cancer, Pisces. Challenges: Leo, Aquarius.",
        "Sagittarius": "Best matches: Aries, Leo. Challenges: Virgo, Pisces.",
        "Capricorn": "Best matches: Taurus, Virgo. Challenges: Aries, Libra."
    }
    return compatibility.get(zodiac_sign, "Compatibility details not available")

def get_user_input():
    name = input("Enter your name: ")
    birth_day = get_integer_input("Enter your birth day (1-31): ", 1, 31)
    birth_month = get_integer_input("Enter your birth month (1-12): ", 1, 12)
    return name, birth_day, birth_month

def get_integer_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    name, birth_day, birth_month = get_user_input()
    zodiac_sign = get_zodiac_sign(birth_day, birth_month)

    if zodiac_sign == "Invalid date":
        print("Invalid date entered. Please try again.")
    else:
        print(f"Hello, {name}! Your zodiac sign is {zodiac_sign}.")
        zodiac_details = get_zodiac_details(zodiac_sign)
        zodiac_element = get_zodiac_element(zodiac_sign)
        zodiac_symbol = get_zodiac_symbol(zodiac_sign)
        zodiac_history = get_zodiac_history(zodiac_sign)
        zodiac_compatibility = get_zodiac_compatibility(zodiac_sign)

        print(f"\nAdditional Details:")
        print(f"Personality traits: {zodiac_details}")
        print(f"Element: {zodiac_element}")
        print(f"Symbol: {zodiac_symbol}")
        print(f"Historical background: {zodiac_history}")
        print(f"Compatibility insights: {zodiac_compatibility}")

if __name__ == "__main__":
    main()

