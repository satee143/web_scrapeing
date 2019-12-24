import pandas as pd

# name='Sheet_name_2')df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],index=['row 1', 'row 2'],columns=['col 1', 'col 2'])
# # # df2 = df1.copy()
# # # with pd.ExcelWriter('output.xlsx') as writer:
# # #     df1.to_excel(writer, sheet_name='Sheet_name_1')
# # #     pd.DataFrame([['e', 'f'], ['g', 'h']],index=['row 3', 'row 4'],columns=['col 3', 'col 4']).to_excel(writer, sheet_

weather_stuff=pd.DataFrame(
        {'DAY':'wed',
         'DATE':'20/12',
         'HIGH TEMP':35,
         'LOW TEMP':14,
         'TYPE OF WEATHER':'cool'
        },
{'DAY':'Tue',
         'DATE':'20/12',
         'HIGH TEMP':35,
         'LOW TEMP':14,
         'TYPE OF WEATHER':'cool'
        }
    )

print(weather_stuff)