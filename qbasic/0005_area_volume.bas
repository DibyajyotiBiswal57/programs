Print "Do you want to find volume or area?"
Print "If volume type = 1"
Print "If area type = 2"
Input opt
Cls
If opt = 1 Then
    Print "For which 3D object you wish to find the volume of?"
    Print "If cuboid type = 1"
    Print "If cube type = 2"
    Print "If cylinder type = 3"
    Print "If cone type = 4"
    Print "If sphere type = 5"
    Input volume
    Cls
    If volume = 1 Then
        Print "What is the length?"
        Input length
        Print "What is the Breadth?"
        Input breadth
        Print "What is the height?"
        Input height
        Print (length * breadth * height); "is your volume!"
    End If
    If volume = 2 Then
        Print "What is the side?"
        Input length
        Print (length * length * length); "is your volume!"

    End If
    If volume = 3 Then
        Print "What is the radius?"
        Input radius
        Print "What is the height?"
        Input height
        Print (22 / 7 * radius * radius * height); "is your volume!"
    End If
    If volume = 4 Then
        Print "What is the radius?"
        Input radius
        Print "What is the height?"
        Input height
        Print (1 / 3 * 22 / 7 * radius * radius * height); "is your volume!"
    End If
    If volume = 4 Then
        Print "What is the radius?"
        Input radius
        Print (4 / 3 * 22 / 7 * radius * radius); "is your volume!"
    End If


End If
If opt = 2 Then
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
        Print side * side; "is the area!"
    End If

    If area = 2 Then
        Print "What is the length of the rectangle?"
        Input length
        Print "What is the breadth?"
        Input breadth
        Print length * breadth; "is the area!"
    End If
    If area = 3 Then
        Print "What is the radius of the circle?"
        Input radius
        Print 22 / 7 * radius * radius; "is the area!"
    End If
    If area = 4 Then
        Print "What is the height of the triangle?"
        Input height
        Print "What is the base?"
        Input base
        Print 1 / 2 * height * base; "is the area!"
    End If

    If area = 6 Then
        Print "What is the height of the trapezium?"
        Input height
        Print "Enter the first parllel side"
        Input s1
        Print "Enter the second parllel side"
        Input s2

        Print height * 1 / 2 * (s1 + s2); "is the area!"
    End If

    If area = 5 Then
        Print "What is the height of the parallelogram?"
        Input height
        Print "What is the base?"
        Input bas
        Print height * bas; "is the area!"
    End If

    If area = 7 Then
        Print "What is the length of the first diagonal?"
        Input d1
        Print "What is the length of the first diagonal?"
        Input d2
        Print 1 / 2 * d1 * d2; "is the area!"
    End If
End If
End
