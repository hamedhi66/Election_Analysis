voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]
for xxx,yyy  in voting_data.items():
    print(f"{xxx}['county'] county has {yyy}['registered_voters'] registered voters")