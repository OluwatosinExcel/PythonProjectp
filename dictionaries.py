
MonthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "My": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(MonthConversion["Dec"])
print(MonthConversion.get("Feb"))
print(MonthConversion.get("Luv", "Not a valid key"))