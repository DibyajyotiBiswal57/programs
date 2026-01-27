Cls
Print "This program checks if a number is prime or not."
Input "Enter a number: ", num
count = 0

For i = 1 To num
    If num Mod i = 0 Then
        count = count + 1
    End If
Next i

If count = 2 Then
    Print "It is a prime number."
Else
    Print "It is not a prime number."
End If

