Cls
Input "Enter a string: ", text$
reversed$ = ""
For i = Len(text$) To 0 Step -1
    reversed$ = reversed$ + Mid$(text$, i, 1)
Next i
If reversed$ = text$ Then
    Print "This string is a Palindrome."
Else
    Print "This string is not a Palindrome."
End If
