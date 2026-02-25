Input "Enter the upper limit: ", n
Print ""
Print "Numbers till"; n; "divisible by both 3 and 7:"
For i = 21 To n
    If i Mod 21 = 0 Then
        Print i
    End If
next i
