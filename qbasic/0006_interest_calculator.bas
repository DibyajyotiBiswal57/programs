CLS
PRINT "Choose the type of interest calculation:"
PRINT "1. Simple Interest"
PRINT "2. Compound Interest"
INPUT "Enter your choice (1 or 2): ", choice

INPUT "Enter Principal amount: ", P
INPUT "Enter Rate of Interest (%): ", R
INPUT "Enter Time (in years): ", T

IF choice = 1 THEN
    SI = (P * R * T) / 100
    PRINT "Simple Interest = "; SI
    PRINT "Total Amount = "; P + SI
ELSEIF choice = 2 THEN
    CI = P * ((1 + R / 100) ^ T - 1)
    PRINT "Compound Interest = "; CI
    PRINT "Total Amount = "; P + CI
ELSE
    PRINT "Invalid choice! Please select 1 or 2."
END IF

END
