"""
The program follows these requirements:
1. Each planet's surface gravity factor is stored in a named constant using the recommended naming
   convention (all uppercase with underscores).  The prefix 'f' is used for floating point constants.
2. The user is prompted to enter their name and their Earth weight.  A prefix 's' is used for the
   string variable (name) and 'f' for the floating‑point variable (weight).
3. The input weight (read as text) is converted to a floating‑point number (float).
4. The Earth weight is multiplied by each of the planet's surface gravity factors to compute the
   corresponding weight on that planet.  Each computed weight is stored in its own floating‑point
   variable with the prefix 'f'.
5. The output displays the user's name along with their weight on each planet.  The phrase
   "Solar System's" is included with a single quote as required.  The numeric weights are
   formatted to occupy 10 characters with two decimal places and are aligned as in the sample
   output from the assignment.
6. Comments are included throughout the code to explain each step.
"""

# Named constants for the surface gravity factors of each celestial body.
# The prefix 'f' denotes these are floating‑point constants.
f_MERCURY_GRAVITY = 0.38
f_VENUS_GRAVITY   = 0.91
f_MOON_GRAVITY    = 0.165
f_MARS_GRAVITY    = 0.38
f_JUPITER_GRAVITY = 2.34
f_SATURN_GRAVITY  = 0.93
f_URANUS_GRAVITY  = 0.92
f_NEPTUNE_GRAVITY = 1.12
f_PLUTO_GRAVITY   = 0.066

def main():
    """
    Main function to prompt the user and compute the planetary weights.
    """
    # Prompt the user for their name.  Prefix 's' for string variable.
    s_name = input("Enter your name: ")

    # Prompt the user for their Earth weight.  Prefix 'f' for floating‑point variable.
    # The input is initially a string, so we convert it to float.
    s_weight_input = input("Enter your weight on Earth (in pounds): ")
    
    # Convert the entered weight to a floating point value.  If conversion fails,
    # the program will raise a ValueError.  This is intentional to keep the
    # assignment straightforward.
    f_weight = float(s_weight_input)

    # Calculate the weight on each planet by multiplying the Earth weight by the
    # respective gravity factor.  Each result is stored in its own floating‑point variable.
    f_weight_mercury = f_weight * f_MERCURY_GRAVITY
    f_weight_venus   = f_weight * f_VENUS_GRAVITY
    f_weight_moon    = f_weight * f_MOON_GRAVITY
    f_weight_mars    = f_weight * f_MARS_GRAVITY
    f_weight_jupiter = f_weight * f_JUPITER_GRAVITY
    f_weight_saturn  = f_weight * f_SATURN_GRAVITY
    f_weight_uranus  = f_weight * f_URANUS_GRAVITY
    f_weight_neptune = f_weight * f_NEPTUNE_GRAVITY
    f_weight_pluto   = f_weight * f_PLUTO_GRAVITY

    # Display the results.  The formatted strings ensure that each weight takes
    # up exactly 10 characters with two decimal points.  The f-string syntax
    # facilitates this formatting easily.
    print()  # Blank line for readability
    print(f"{s_name}'s weight on the Solar System's bodies:")
    print("Planet     Weight")
    print("------------------")
    # Print each planet's weight.  The planet name is left‑aligned in a field of 10
    # characters, and the weight is right‑aligned in a field of 10 characters with
    # two decimal places.
    print(f"Mercury   {f_weight_mercury:10.2f}")
    print(f"Venus     {f_weight_venus:10.2f}")
    print(f"Moon      {f_weight_moon:10.2f}")
    print(f"Mars      {f_weight_mars:10.2f}")
    print(f"Jupiter   {f_weight_jupiter:10.2f}")
    print(f"Saturn    {f_weight_saturn:10.2f}")
    print(f"Uranus    {f_weight_uranus:10.2f}")
    print(f"Neptune   {f_weight_neptune:10.2f}")
    print(f"Pluto     {f_weight_pluto:10.2f}")


if __name__ == "__main__":
    main()
