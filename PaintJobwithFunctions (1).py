# Paint Job Estimator Assignment
#Kevin Lashley
#November 30, 2025

def getFloatInput(strPrompt):
    # Prompt user until positive, nonzero float is entered
    while True:
        strInput = input(strPrompt + ": ")     # Prompt for input
        try:
            fValue = float(strInput)
            if fValue > 0:
                return fValue
            else:
                print("Value must be greater than zero. Try again.")
        except:
            print("Invalid input. Enter a numeric value.")

def getGallonsOfPaint(fSqFeet, fFeetPerGallon):
    # Calculate gallons needed, round up with formula 
    fGallons = fSqFeet / fFeetPerGallon
    if int(fGallons) < fGallons:
        iGallons = int(fGallons) + 1
    else:
        iGallons = int(fGallons)
    return iGallons

def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

def getLaborCost(fTotalLaborHours, fLaborChargePerHour):
    return fTotalLaborHours * fLaborChargePerHour

def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

def getSalesTax(strState):
    # Returns sales tax rate by state
    if strState.upper() == 'CT':
        return 0.06
    elif strState.upper() == 'MA':
        return 0.0625
    elif strState.upper() == 'ME':
        return 0.085
    elif strState.upper() == 'NH':
        return 0.0
    elif strState.upper() == 'RI':
        return 0.07
    elif strState.upper() == 'VT':
        return 0.06
    else:
        return 0.0

def showCostEstimate(
    strLastName, strState, fSqFeet, fPaintPrice, fFeetPerGallon, 
    fLaborHoursPerGallon, fLaborChargePerHour, 
    iTotalGallons, fTotalLaborHours, fLaborCost, fPaintCost, 
    fSalesTaxRate, fTax, fTotalCost
):
    # Prepare formatted output lines
    strOutput = ""
    strOutput += "PAINT JOB ESTIMATE FOR: " + strLastName + "\n"
    strOutput += "State: " + strState + "\n"
    strOutput += "Square Feet: " + format(fSqFeet, ".2f") + "\n"
    strOutput += "Paint Price/gallon: $" + format(fPaintPrice, ".2f") + "\n"
    strOutput += "Feet Covered per Gallon: " + format(fFeetPerGallon, ".2f") + "\n"
    strOutput += "Labor Hours per Gallon: " + format(fLaborHoursPerGallon, ".2f") + "\n"
    strOutput += "Labor Charge per hour: $" + format(fLaborChargePerHour, ".2f") + "\n"
    strOutput += "-----------------------------------------\n"
    strOutput += "Gallons Required: " + str(iTotalGallons) + "\n"
    strOutput += "Total Labor Hours: " + format(fTotalLaborHours, ".2f") + "\n"
    strOutput += "Paint Cost: $" + format(fPaintCost, ".2f") + "\n"
    strOutput += "Labor Cost: $" + format(fLaborCost, ".2f") + "\n"
    strOutput += "Sales Tax Rate: " + format(fSalesTaxRate*100, ".2f") + "%\n"
    strOutput += "Sales Tax: $" + format(fTax, ".2f") + "\n"
    strOutput += "TOTAL COST: $" + format(fTotalCost, ".2f") + "\n"

    print(strOutput)

    strFileName = strLastName + "_PaintJobOutput.txt"
    outFile = open(strFileName, "w")
    outFile.write(strOutput)
    outFile.close()
    print("Output file created:", strFileName)

def main():
    # All variable names use the Hungarian notation:
    fSqFeet = getFloatInput("Enter Square Feet of the Wall")
    fPaintPrice = getFloatInput("Enter Paint Price")
    fFeetPerGallon = getFloatInput("Enter Feet per Gallon of Paint")
    fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon")
    fLaborChargePerHour = getFloatInput("Enter Painting Labor charge per hour")
    strState = input("Enter the state where the job will take place: ")
    strLastName = input("Enter the customer's last name: ")

    iTotalGallons = getGallonsOfPaint(fSqFeet, fFeetPerGallon)
    fTotalLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fTotalLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fSalesTaxRate = getSalesTax(strState)
    fTax = (fPaintCost + fLaborCost) * fSalesTaxRate
    fTotalCost = fPaintCost + fLaborCost + fTax
#Show and save the output
    showCostEstimate(
        strLastName, strState, fSqFeet, fPaintPrice, fFeetPerGallon, 
        fLaborHoursPerGallon, fLaborChargePerHour, 
        iTotalGallons, fTotalLaborHours, fLaborCost, fPaintCost, 
        fSalesTaxRate, fTax, fTotalCost
    )

main()
