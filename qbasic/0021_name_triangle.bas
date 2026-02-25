Cls
Input "Enter a string: ", text$
For i = 0 To (Len(text$)-1)
    Print Mid$(text$, 0, (i + 2))
Next i
