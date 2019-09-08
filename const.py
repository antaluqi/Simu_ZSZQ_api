"""定义一些名称"""



F_COLUMN_NAME=('资金余额','冻结资金','可用余额','可取资金','股票市值','总资产','资金账号')
S_COLUMN_NAME=('证券代码','证券名称','股票余额','可用余额','冻结数量','成本价','市价','盈亏比例(%)','市值','盈亏','交易市场','股东账号','资金账号')
E_COLUMN_NAME=('委托时间','证券代码','证券名称','委托数量','成交数量','委托类别','操作','委托价格','成交均价','合同编号','股东账户','交易市场','申报编号','备注','废单原因','备注信息','资金账号')
T_COLUMN_NAME=('成交日期','成交时间','证券代码','证券名称','操作','成交均价','成交数量','成交金额','成交编号','合同编号','申报编号','股东账户','交易市场','资金账号')



F_COLUMN_NAME_KEY={
    'f_curr_bal': '资金余额',
    'f_froz_bal': '冻结资金',
    'f_can_use_bal': '可用余额',
    'f_can_get_bal': '可取资金',
    'f_stock_val': '股票市值',
    'f_all_bal': '总资产',
    'f_account': '资金账号',
}


S_COLUMN_NAME_KEY={
    'code': '证券代码',
    'name': '证券名称',
    's_bal': '股票余额',
    's_can_use_bal': '可用余额',
    's_fros_bal': '冻结数量',
    's_cost_pri': '成本价',
    'market': '交易市场',
    's_account': '股东账户',
    'f_account': '资金账号',
}



SV_COLUMN_NAME_KEY={
    'code': '证券代码',
    'name': '证券名称',
    's_bal': '股票余额',
    's_can_use_bal': '可用余额',
    's_fros_bal': '冻结数量',
    's_cost_pri': '成本价',
    's_market_pri': '市价',
    's_profit_rat': '盈亏比例(%)',
    's_market_val': '市值',
    's_profit': '盈亏',
    'market': '交易市场',
    's_account': '股东账户',
    'f_account': '资金账号',
}

E_COLUMN_NAME_KEY={
    'e_time': '委托时间',
    'code': '证券代码',
    'name': '证券名称',
    'e_amount': '委托数量',
    'c_amount': '成交数量',
    'e_type': '委托类别',
    'opration': '操作',
    'e_pri': '委托价格',
    'c_avg_pri': '成交均价',
    'contract_no': '合同编号',
    's_account': '股东账户',
    'market': '交易市场',
    'declaratiom_no': '申报编号',
    'note': '备注',
    'scrap_order_reason ': '废单原因',
    'note_info': '备注信息',
    'f_account': '资金账号',
}

T_COLUMN_NAME_KEY={
    't_date': '成交日期',
    't_time': '成交时间',
    'code': '证券代码',
    'name': '证券名称',
    'opration': '操作',
    'c_avg_pri': '成交均价',
    'c_amount': '成交数量',
    'c_val': '成交金额',
    'c_no': '成交编号',
    'contract_no': '合同编号',
    'declaratiom_no': '申报编号',
    's_account': '股东账户',
    'market': '交易市场',
    'f_account': '资金账号',
}

F_COLUMN_KEY_NAME=dict(zip(F_COLUMN_NAME_KEY.values(),F_COLUMN_NAME_KEY.keys()))

S_COLUMN_KEY_NAME=dict(zip(S_COLUMN_NAME_KEY.values(),S_COLUMN_NAME_KEY.keys()))

SV_COLUMN_KEY_NAME=dict(zip(SV_COLUMN_NAME_KEY.values(),SV_COLUMN_NAME_KEY.keys()))

E_COLUMN_KEY_NAME=dict(zip(E_COLUMN_NAME_KEY.values(),E_COLUMN_NAME_KEY.keys()))

T_COLUMN_KEY_NAME=dict(zip(T_COLUMN_NAME_KEY.values(),T_COLUMN_NAME_KEY.keys()))

sTBNAME_TBNANE={
    'b':'balance',
    's':'stock',
    'e':'entrusts',
    't':'trades',
 }

sTBNAME_CNAME={
    'b':F_COLUMN_KEY_NAME.keys(),
    's':S_COLUMN_KEY_NAME.keys(),
    'e':E_COLUMN_KEY_NAME.keys(),
    't':T_COLUMN_KEY_NAME.keys(),
 }

sTBNAME_CKEY={
    'b':F_COLUMN_NAME_KEY.keys(),
    's':S_COLUMN_NAME_KEY.keys(),
    'e':E_COLUMN_NAME_KEY.keys(),
    't':T_COLUMN_NAME_KEY.keys(),
 }


sTBNAME_NKDICT={
    'b': F_COLUMN_KEY_NAME,
    's': S_COLUMN_KEY_NAME,
    'e': E_COLUMN_KEY_NAME,
    't': T_COLUMN_KEY_NAME,
}