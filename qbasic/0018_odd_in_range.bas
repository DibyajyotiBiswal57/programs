Cls
Print "This program finds odd numbers between 2 numbers."
Input "Enter the start number (m): ", m
Input "Enter the end number (n): ", n

For i = m To n
    If i Mod 2 <> 0 Then
        Print i
    End If
Next i

End

