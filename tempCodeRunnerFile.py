wordDoc = Document('/container/*.docx')
# table0 = wordDoc.tables[0]
# data0 = [[cell.text for cell in row.cells] for row in table0.rows]
# df0 = pd.DataFrame(data0)
# df0.columns = ['key', 'value']
# df_table1 = df0
# df_table1 = df_table1.drop([0])

# table1 = wordDoc.tables[1]
# data1 = [[cell.text for cell in row.cells] for row in table1.rows]
# df1 = pd.DataFrame(data1)
# df1.columns = ['key', 'value']
# df_table2 = df1
# df_table2 = df_table2.drop([0])


# key = ['projectName','pubManager','pubDepositer','pubSupervisor',
#              'pubFinanceConsultant','absFinancier','pubGuarantor','absAssetName',
#              'pubIntegratedCost','pubFundsUse','pubRepaySource','pubProspectiveEarnings',
#              'pubDueTime','virtualAmount','pubPrincipalType','projectGrade','absProjectSource',
#        'absIncomeRate','absPromanageRate','absTrustmanageRate','absCustodyFeeRate',
#               'absSuperviseRate','absFinanceRate','absInvestIncomeRate'
#        ]
# df_out = pd.concat([df_table1,df_table2])
# df_T = df_out.T
# df_T.columns = key
# df_T = df_T.drop('key')
# df_T = df_T.reset_index(drop=True)
# df_T