#inter Planetry Weights

# Declare Named Constants for each of the planet Surface Gravity Factors
MERCURY_SURFACE_GRAVITY_FACTOR = 0.38
VENUS_SURFACE_GRAVITY_FACTOR = 0.91
MARS_SURFACE_GRAVITY_FACTOR = 0.38
JUPITER_SURFACE_GRAVITY_FACTOR = 2.34
SATURN_SURFACE_GRAVITY_FACTOR = 1.06
URANUS_SURFACE_GRAVITY_FACTOR = 0.92
NEPTUNE_SURFACE_GRAVITY_FACTOR = 1.19
PLUTO_SURFACE_GRAVITY_FACTOR = 0.06

# Prompt the user for a Name and their Earth Weight
sUserName = input("Enter your name: ")
sEarthWeightInput = input("Enter your Earth weight: ")

# Convert the entered Weight to the appropriate numeric data type
fEarthWeight = float(sEarthWeightInput)

# Multiple the Earth Weight by each of the planet’s Surface Gravity Factor
fMercuryWeight = fEarthWeight * MERCURY_SURFACE_GRAVITY_FACTOR
fVenusWeight = fEarthWeight * VENUS_SURFACE_GRAVITY_FACTOR
fMarsWeight = fEarthWeight * MARS_SURFACE_GRAVITY_FACTOR
fJupiterWeight = fEarthWeight * JUPITER_SURFACE_GRAVITY_FACTOR
fSaturnWeight = fEarthWeight * SATURN_SURFACE_GRAVITY_FACTOR
fUranusWeight = fEarthWeight * URANUS_SURFACE_GRAVITY_FACTOR
fNeptuneWeight = fEarthWeight * NEPTUNE_SURFACE_GRAVITY_FACTOR
fPlutoWeight = fEarthWeight * PLUTO_SURFACE_GRAVITY_FACTOR

# Output the results as per the sample output requirements
print(f"\n{sUserName}, here is your weight in the Solar System's planets:")
print(f"Mercury:   {fMercuryWeight:10.2f}")
print(f"Venus:     {fVenusWeight:10.2f}")
print(f"Mars:      {fMarsWeight:10.2f}")
print(f"Jupiter:   {fJupiterWeight:10.2f}")
print(f"Saturn:    {fSaturnWeight:10.2f}")
print(f"Uranus:    {fUranusWeight:10.2f}")
print(f"Neptune:   {fNeptuneWeight:10.2f}")
print(f"Pluto:     {fPlutoWeight:10.2f}")