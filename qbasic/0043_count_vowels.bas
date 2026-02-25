Input "Enter a string: ", text$
count = 0
For i = 1 To Len(text$)
    If InStr("AEIOUaeiou", (Mid$(text$, i, 1))) > 0 Then
        count = count + 1
    End If
Next i
Print "There are"; count; "vowels in the string."
