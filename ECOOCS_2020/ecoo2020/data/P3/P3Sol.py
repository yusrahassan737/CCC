# Name: Yusra Hassan
# Date: April 1, 2021
# Description: Solution to ECOO 2020 P3 (Solve a number captcha based on its dimensions and a pattern it makes with -  and *)
# Purpose: Practice for ECOO

openFile = open("data.in", "r")

T = int(openFile.readline())
for i in range(T):
    # Variables
    digits = ""
    N = int(openFile.readline())
    for j in range(N):
        proportions = openFile.readline()
        H = int(proportions[:proportions.find(" ")])
        W = int(proportions[proportions.find(" ") + 1:])
        # find out what digit it is
        # add it to the digits string

openFile.close()
