#CMPT 120L 113
# Mars Rover Program
# Author: Jeremy Harrelson
# Created 9/6/2018

def main():
    size = input("How large is the photo's file size in bytes? \n")
    sizeForConversion = size * 8
    lowRate = sizeForConversion * 500
    highRate = sizeForConversion * 32000
    print("It would take between " + lowRate + " and " + highRate + ".")
main()