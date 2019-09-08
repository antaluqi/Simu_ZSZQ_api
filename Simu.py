import sqlite3
from const import *
import requests,re

def ctrateTB():
    conn = sqlite3.connect('ZSZQ.db')
    create_balance_str='''CREATE TABLE IF NOT EXISTS balance
                                (  f_curr_bal REAL,
                                   f_froz_bal REAL,
                                   f_can_use_bal REAL,
                                   f_can_get_bal REAL,
                                   f_stock_val REAL,
                                   f_all_bal REAL,
                                   f_account TEXT);'''

    create_stock_str = '''CREATE TABLE IF NOT EXISTS stock
                                     (    code TEXT,
                                          name TEXT,
                                          s_bal REAL,
                                          s_can_use_bal REAL,
                                          s_fros_bal REAL,
                                          s_cost_pri REAL,
                                          market TEXT,
                                          s_account TEXT,
                                          f_account TEXT);'''


    create_stockv_str='''CREATE TABLE IF NOT EXISTS stock
                                     (    code TEXT,
                                          name TEXT,
                                          s_bal REAL,
                                          s_can_use_bal REAL,
                                          s_fros_bal REAL,
                                          s_cost_pri REAL,
                                          s_market_pri REAL,
                                          s_profit_rat REAL,
                                          s_market_val REAl,
                                          s_profit REAL,
                                          market TEXT,
                                          s_account TEXT,
                                          f_account TEXT);'''

    create_entrusts_str='''CREATE TABLE IF NOT EXISTS entrusts
                                 (e_time TEXT,
                                  code TEXT,
                                  name TEXT,
                                  e_amount INT,
                                  c_amount INTL,
                                  e_type TEXT,
                                  opration TEXT,
                                  e_pri REAL,
                                  c_avg_pri REAL,
                                  contract_no INT,
                                  s_account TEXT,
                                  market TEXT,
                                  declaratiom_no INT,
                                  note TEXT,
                                  scrap_order_reason TEXT,
                                  note_info TEXT,
                                  f_account TEXT);'''

    create_trades_str='''CREATE TABLE IF NOT EXISTS trades
                                 ( t_date DATE,
                                   t_time TEXT,
                                   code TEXT,
                                   name TEXT,
                                   opration TEXT,
                                   c_avg_pri REAL,
                                   c_amount REAL,
                                   c_val REAL,
                                   c_no INT,
                                   contract_no INT,
                                   declaratiom_no INT,
                                   s_account TEXT,
                                   market TEXT,
                                   f_account TEXT);'''

    conn.execute(create_balance_str)
    conn.execute(create_stock_str)
    conn.execute(create_entrusts_str)
    conn.execute(create_trades_str)
    conn.commit()
    conn.close()

def insertTestData():
    conn = sqlite3.connect('ZSZQ.db')
    insert_balance_str='''insert into 
                            balance ( f_curr_bal,
                                      f_froz_bal,
                                      f_can_use_bal,
                                      f_can_get_bal,
                                      f_stock_val,
                                      f_all_bal,
                                      f_account) 
                               VALUES( 5000.83,
                                       0,
                                       5000.83,
                                       5000.83,
                                       0,
                                       5000.83,
                                       1320011172);'''

    insert_stock_str='''insert into 
                          stock ( code,
                                  name,
                                  s_bal,
                                  s_can_use_bal,
                                  s_fros_bal,
                                  s_cost_pri,
                                  market,
                                  s_account,
                                  f_account) 
                           VALUES( 601398,
                                   '工商银行',
                                   100,
                                   100,
                                   0,
                                   5.30,
                                   '上海A股',
                                   'A467162210',
                                   1320011172);'''

    insert_entrusts_str='''insert into 
                              entrusts ( e_time,
                                          code,
                                          name,
                                          e_amount,
                                          c_amount,
                                          e_type,
                                          opration,
                                          e_pri,
                                          c_avg_pri,
                                          contract_no,
                                          s_account,
                                          market,
                                          declaratiom_no,
                                          note,
                                          scrap_order_reason,
                                          note_info,
                                          f_account) 
                                   VALUES( '23:58:52',
                                           601398,
                                           '工商银行',
                                           100,
                                           0,
                                           '0|买卖',
                                           '证券买入',
                                           5.300,
                                           0.000,
                                           10,
                                           'A467162210',
                                           '上海Ａ股',
                                           10,
                                           '已撤(买卖)',
                                           '无',
                                           '无',
                                           1320011172
                                           );'''

    insert_trades_str='''insert into 
                              trades (  t_date,
                                       t_time,
                                       code,
                                       name,
                                       opration,
                                       c_avg_pri,
                                       c_amount,
                                       c_val,
                                       c_no,
                                       contract_no,
                                       declaratiom_no,
                                       s_account,
                                       market,
                                       f_account) 
                                   VALUES( '2019-09-05',
                                           '23:58:52',
                                           601398,
                                           '工商银行',
                                           '证券买入',
                                           5.3,
                                           100,
                                           530,
                                           5234,
                                           5234,
                                           5234,
                                           'A467162210',
                                           '上海Ａ股',
                                           1320011172
                                           );'''

    conn.execute("delete from balance")
    conn.execute("delete from stock")
    conn.execute("delete from entrusts")
    conn.execute("delete from trades")
    conn.execute(insert_balance_str)
    conn.execute(insert_stock_str)
    conn.execute(insert_entrusts_str)
    conn.execute(insert_trades_str)
    conn.commit()
    conn.close()

def get_table_data(t_name):
    with sqlite3.connect('ZSZQ.db') as conn:
        tableName=sTBNAME_TBNANE[t_name]
        key=sTBNAME_CNAME[t_name]
        value=conn.execute("select * from %s"%(tableName)).fetchall()
        result=[]
        for v in value:
            result.append(dict(zip(key,v)))
        if t_name=='b':
            s=get_table_data('s')
            result[0]['股票市值']=0 if s==[] else sum([v['市值'] for v in s])
            return result[0]
        elif t_name=='s':
           for s in result:
              quote = get_sQuote(s['证券代码'])[s['证券代码']]
              s['市价']=quote['最新价格']
              s['盈亏比例(%)']=round((quote['最新价格']-s['成本价'])/s['成本价']*100,2)
              s['市值']=quote['最新价格']*s['股票余额']
              s['盈亏']=round(quote['最新价格']-s['成本价'],2)
        return result

def add_table_data(stb_name,data):
    if isinstance(data,dict)==False:
        return {'success':False,'mag':'参数2必须为dict'}

    with sqlite3.connect('ZSZQ.db') as conn:
        if stb_name not in sTBNAME_TBNANE.keys():
            return {'success': False, 'mag': '表%s不存在' % (stb_name)}
        tb_name=sTBNAME_TBNANE[stb_name]
        if conn.execute("select name from sqlite_master where type='table' and name = '%s'"%(tb_name) ).fetchall()==[]:
            return {'success':False,'mag':'表%s不存在'%(tb_name)}
        cName=sTBNAME_CNAME[stb_name]
        if (set(data.keys())<=set(cName))==False:
            return {'success':False,'mag':'请检查数据字段是否匹配表字段'}
        data=dict([(sTBNAME_NKDICT[stb_name][k], v) for k, v in data.items()])
        print(data)

def get_sQuote(codeList):
    if isinstance(codeList,str):
        codeList=[codeList]
    if isinstance(codeList,list)==False:
        raise ValueError('输入值必须为list或str')
    result={}
    cl=['s_sh'+c if c[0]=='6' else ('s_'+c if c[0]=='s' else 's_sz'+c) for c in codeList]
    url="http://qt.gtimg.cn/q=%s"%(','.join(cl))
    qStr=requests.get(url).text
    for q in qStr.split(";\n"):
        qInfoL=re.split('[="~]',q)
        if len(qInfoL)<10:
            continue
        r={'市场标志':int(qInfoL[2]),
           '证券名称':qInfoL[3],
           '证券代码':qInfoL[4],
           '最新价格':float(qInfoL[5]),
           '涨跌额':float(qInfoL[6]),
           '涨跌幅':float(qInfoL[7]),
           '成交量':int(qInfoL[8]),
           '成交额':int(qInfoL[9]),
           '总市值':float(qInfoL[11]) if qInfoL[11]!="" else None,
           '涨停价':round((float(qInfoL[5])-float(qInfoL[6]))*1.1,2),
           '跌停价':round((float(qInfoL[5])-float(qInfoL[6]))*0.9,2)
           }
        result[qInfoL[4]]=r
    return  result


def entrust(code,bs,price,amount):
    # code 的输入判定
    quote=get_sQuote([code])
    if code not in quote.keys():
        return {'success':False,'mag':'交易代码%s不存在'%(code)}

    # 交易方向的输入判定
    if bs not in ['b','s','cb','cs']:
        return {'success':False,'mag':'交易类型输入有误%s,应为[b,s,cb,cs]中的一种'}

    #价格的输入判定
    priStr=str(float(price))
    if len(priStr[priStr.find(".")+1:])>2:
        return {'success':False,'mag':'价格不能小于分'}

    if float(price)>quote[code]['涨停价'] or float(price)<quote[code]['跌停价']:
        return {'success':False,'mag':'价格输入在涨跌停价格[%.2f,%.2f]范围之外'%(quote[code]['跌停价'],quote[code]['涨停价'])}

    # 交易数量的输入判定
    if amount==0 or amount%100!=0:
        return {'success':False,'mag':'购买数量必须为100的整数倍'}

    # 可用资金判定
    balance=get_table_data('b')
    if price*amount>balance['可用余额']:
        return {'success':False,'mag':'可用资金不足'}





