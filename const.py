"""定义一些名称"""

'''输出字典的keys'''

F_DICT_KEY=('资金余额','冻结资金','可用余额','可取资金','股票市值','总资产','资金账号')
S_DICT_KEY=('证券代码','证券名称','股票余额','可用余额','冻结数量','成本价','交易市场','股东账号','资金账号')
SV_DICT_KEY=('证券代码','证券名称','股票余额','可用余额','冻结数量','成本价','市价','盈亏比例(%)','市值','盈亏','交易市场','股东账号','资金账号')
E_DICT_KEY=('委托时间','证券代码','证券名称','委托数量','成交数量','委托类别','操作','委托价格','成交均价','合同编号','股东账户','交易市场','申报编号','备注','废单原因','备注信息','资金账号')
T_DICT_KEY=('成交日期','成交时间','证券代码','证券名称','操作','成交均价','成交数量','成交金额','成交编号','合同编号','申报编号','股东账户','交易市场','资金账号')

'''数据库表的column names'''

F_COLUMN_NAME=('f_curr_bal','f_froz_bal','f_can_use_bal','f_can_get_bal','f_stock_val','f_all_bal','f_account')
S_COLUMN_NAME=('code','name','s_bal','s_can_use_bal','s_fros_bal','s_cost_pri','market','s_account','f_account')
E_COLUMN_NAME=('e_time','code','name','e_amount','c_amount','e_type','opration','e_pri','c_avg_pri','contract_no','s_account','market','declaratiom_no','note','scrap_order_reason ','note_info','f_account')
T_COLUMN_NAME=('t_date','t_time','code','name','opration','c_avg_pri','c_amount','c_val','c_no','contract_no','declaratiom_no','s_account','market','f_account')

'''字段名column name -> 字典key'''

F_cNAME_2_dKEY=dict(zip(F_COLUMN_NAME,F_DICT_KEY))
S_cNAME_2_dKEY=dict(zip(S_COLUMN_NAME,S_DICT_KEY))
E_cNAME_2_dKEY=dict(zip(E_COLUMN_NAME,E_DICT_KEY))
T_cNAME_2_dKEY=dict(zip(T_COLUMN_NAME,T_DICT_KEY))

'''字典key -> 字段名column name '''

F_dKEY_2_cNAME=dict(zip(F_DICT_KEY,F_COLUMN_NAME))
S_dKEY_2_cNAME=dict(zip(S_DICT_KEY,S_COLUMN_NAME))
E_dKEY_2_cNAME=dict(zip(E_DICT_KEY,E_COLUMN_NAME))
T_dKEY_2_cNAME=dict(zip(T_DICT_KEY,T_COLUMN_NAME))

'''简写表名 -> 全表名'''

stNAME_2_tNANE={
    'b':'balance',
    's':'stock',
    'e':'entrusts',
    't':'trades',
 }

'''简写表名 -> 字段名column name'''

stNAME_2_cNAME={
    'b':F_COLUMN_NAME,
    's':S_COLUMN_NAME,
    'e':E_COLUMN_NAME,
    't':T_COLUMN_NAME,
 }

'''简写表名 -> 输出字典key'''

stNAME_2_dKEY={
    'b':F_DICT_KEY,
    's':S_DICT_KEY,
    'e':E_DICT_KEY,
    't':T_DICT_KEY,
 }

'''简写表名 -> （字典key 字段cn）是对照表'''

stNAME_2_K2N={
    'b': F_dKEY_2_cNAME,
    's': S_dKEY_2_cNAME,
    'e': E_dKEY_2_cNAME,
    't': T_dKEY_2_cNAME,
}

'''简写表名 -> （字段cn 字典key）是对照表'''

stNAME_2_N2K={
    'b': F_cNAME_2_dKEY,
    's': S_cNAME_2_dKEY,
    'e': E_cNAME_2_dKEY,
    't': T_cNAME_2_dKEY,
}