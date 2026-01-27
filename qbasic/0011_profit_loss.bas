Print "This program finds if you incurred a profit or loss on selling an article."
Print "Enter the cost price of the article."
Input a
Print "Enter the selling price of the article."
Input b
If a < b Then
    Print "You have a profit of"; b - a; "rupees"
    Print "The profit percentage is "; ((b - a) / a) * 100; "%"
Else
    Print "You have a loss of"; a - b; "rupees"
    Print "The loss percentage is"; ((a - b) / a) * 100; "%"
End If

