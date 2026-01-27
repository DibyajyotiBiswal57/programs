  Print "For which 2D shape you want to find the area of?"
    Print "For square type = 1"
    Print "For rectangle type = 2"
    Print "For circle type = 3"
    Print "For triangle type = 4"
    Print "For parallelogram type = 5"
    Print "For trapezium type = 6"
    Print "For rhombus type = 7"

    Input area
    Cls
    If area = 1 Then
        Print "What is the side of the square?"
        Input side
        Print side * 4; "is the perimeter!"
    End If

    If area = 2 Then
        Print "What is the length of the rectangle?"
        Input length
        Print "What is the breadth?"
        Input breadth
        Print 2 * (length + breadth); "is the perimeter!"
    End If
    If area = 3 Then
        Print "What is the radius of the circle?"
        Input radius
        Print 2 * 22 / 7 * radius; "is the perimeter!"
    End If
    If area = 4 Then
        Print "What are the sides of the triangle?"
        Input s1
        Input s2
        Input s3
        Print s1+s2+s3; "is the perimeter!"
    End If

    If area = 6 Then
        Print "Enter the sides of the trapezium"
        Input s1
        Input s2
        Input s3
        Input s4

        Print s1 + s + s3 + s4; "is the perimeter!"
    End If

    If area = 5 Then
        Print "What is the length of the parallelogram?"
        Input length
        Print "What is the breadth?"
        Input breadth
        Print 2 * (length + breadth); "is the perimeter!"
    End If

    If area = 7 Then
        Print "What is the side of the rhombus?"
        Input side
        Print side * 4; "is the perimeter!"
    End If
End If
