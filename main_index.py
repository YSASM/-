from datetime import datetime
from functools import reduce
import random
from flask import Flask,render_template,url_for,request
import MySQLdb
db = MySQLdb.connect("localhost", "root", "root", "dingpiaoxitong", charset='utf8' )
cursor = db.cursor()
app = Flask(__name__)
def toint(s):
    return reduce(lambda x,y:x*10+y, map(lambda s:{'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s], s))
def get_sql(string):
    # 执行sql语句
    cursor.execute(string)
    # 获取执行结果
    rows = cursor.fetchall()
    arr = []
    temp = []
    # 数据处理并返回一个数组
    for row in rows:
        for r in row:
            temp.append(str(r))
        arr.append(temp)
        temp = []
    return arr
def write_sql(string):
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(string)
        # 提交到数据库执行
        db.commit()
    except:
        db.rollback()

@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')
@app.route("/search/",methods=['POST'])
def search():
    return render_template('search.html')
@app.route("/buy/",methods=['POST'])
def buy():
    return render_template('buy.html')
@app.route("/unbuy/",methods=['POST'])
def unbuy():
    arr = get_sql("SELECT * FROM userinfo LEFT JOIN dingpiaoinfo ON userinfo.`Userid`=dingpiaoinfo.`Userid` RIGHT JOIN dingpiao ON dingpiaoinfo.`Dingdanid`=dingpiao.`Dingdanid` WHERE dingpiaoinfo.`Dingdanid` IN (SELECT dingpiao.`Dingdanid` FROM dingpiao LEFT JOIN tuipiao ON dingpiao.`Dingdanid` = tuipiao.`Dingdanid` WHERE tuipiao.`Dingdanid` IS NULL);")
    string = ""
    count = 1
    for i in arr:
        string+=(str(count)+":  身份证号:"+i[0]+" 姓名:"+i[1]+" 性别:"+i[2]+" 电话:"+i[3]+" 订单号:"+i[4]+" 车次号:"+i[6]+" 订单时间:"+i[8]+" 订票数:"+i[9]+" 总价:"+i[10]+" 订票渠道:"+i[12]+"\n")
        count+=1
    return render_template('unbuy.html',back = string)
def is_chinese(string):
    for c in string:
        if not ('\u4e00' <= c <= '\u9fa5'):
            return False
    return True
@app.route("/buy_add/",methods=['POST'])
def buy_add():
    Trainid=request.form.get('Trainid')
    username=request.form.get('username')
    xingbie=request.form.get('xingbie')
    userid=request.form.get('userid')
    phone=request.form.get('phone')
    dingpiaoshu=request.form.get('dingpiaoshu')
    if Trainid!='' and username!='' and userid!='' and phone!='' and dingpiaoshu!='' and xingbie!='':
        dingdanhao=str(datetime.now().strftime("%Y%m%d%H%M%S"))+str(random.randint(1,9))+Trainid
        dingpiaoqudao=request.form.get('dingpiaoqudao')
        price = get_sql("SELECT price FROM train WHERE trainid='"+Trainid+"';")[0][0]
        startday = str(get_sql("SELECT startday FROM train WHERE trainid='"+Trainid+"';")[0][0])
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if price:
            allprice = str(toint(price)*toint(dingpiaoshu))
            if is_chinese(username):
                if xingbie == '男' or xingbie == '女':
                    updatepiaoshu = toint(get_sql("SELECT piaoshu FROM train WHERE trainid='"+Trainid+"';")[0][0])-1
                    print(updatepiaoshu)
                    if not get_sql("SELECT * FROM userinfo WHERE username='"+username+"';") or get_sql("SELECT userid FROM userinfo WHERE username='"+username+"';")[0][0] != userid:
                        write_sql("INSERT INTO userinfo VALUE('"+userid+"','"+username+"','"+xingbie+"','"+phone+"');")
                    write_sql("INSERT INTO dingpiao VALUE('"+dingdanhao+"','"+dingpiaoqudao+"');")
                    write_sql("INSERT INTO dingpiaoinfo VALUE('"+dingdanhao+"','"+userid+"','"+Trainid+"','"+startday+"','"+time+"','"+dingpiaoshu+"','"+allprice+"');")
                    updatepiaoshu = toint(get_sql("SELECT piaoshu FROM train WHERE trainid='"+Trainid+"';")[0][0])-1
                    write_sql("UPDATE train SET piaoshu = '"+str(updatepiaoshu)+"' WHERE trainid='"+Trainid+"';")
                    return render_template('buy.html',error='购票成功！')
                else :
                    return render_template('buy.html',error='请输入正确性别！')
            else:
                return render_template('buy.html',error='请输入中文名长度小于10！')
        else:
            return render_template('buy.html',error='请输入正确的车次号！') 
    return render_template('buy.html',error='不能有空项！')
@app.route("/unbuy_add/",methods=['POST'])
def unbuy_add():
    id=toint(request.form.get('id'))
    arr = get_sql("SELECT * FROM userinfo LEFT JOIN dingpiaoinfo ON userinfo.`Userid`=dingpiaoinfo.`Userid` RIGHT JOIN dingpiao ON dingpiaoinfo.`Dingdanid`=dingpiao.`Dingdanid` WHERE dingpiaoinfo.`Dingdanid` IN (SELECT dingpiao.`Dingdanid` FROM dingpiao LEFT JOIN tuipiao ON dingpiao.`Dingdanid` = tuipiao.`Dingdanid` WHERE tuipiao.`Dingdanid` IS NULL);")
    dingdanhao1 = arr[id-1][4]
    dingpiaoqudao1 = arr[id-1][12]
    write_sql("INSERT INTO tuipiao VALUE('"+dingdanhao1+"','"+dingpiaoqudao1+"');")
    return render_template('unbuy.html',back = "退票成功")
@app.route("/trainid_search/",methods=['POST'])
def Trainid():
    arr = get_sql("SELECT * FROM train;")
    string = ""
    count = 1
    for i in arr:
        string+=(str(count)+":  车号:"+i[0]+" 始发地:"+i[1]+" 目的地:"+i[2]+" 发车日期:"+str(i[3])+" 开出时刻:"+str(i[4])+" 到达时刻:"+str(i[5])+" 剩余票数:"+i[6]+" 票价:"+i[7]+"\n")
        count+=1
    return render_template('search.html',back = string)

@app.route("/userid_search/",methods=['POST'])
def Userid():
    arr = get_sql("SELECT * FROM userinfo;")
    string = ""
    count = 1
    for i in arr:
        string+=(str(count)+":  身份证号:"+i[0]+" 姓名:"+i[1]+" 性别:"+i[2]+" 电话:"+i[3]+"\n")
        count+=1
    return render_template('search.html',back = string)

@app.route("/userbyinfo_search/",methods=['POST'])
def Userbyinfo():
    arr = get_sql("SELECT * FROM userinfo LEFT JOIN dingpiaoinfo ON userinfo.`Userid`=dingpiaoinfo.`Userid` LEFT JOIN dingpiao ON dingpiaoinfo.`Dingdanid`=dingpiao.`Dingdanid`;")
    string = ""
    count = 1
    for i in arr:
        string+=(str(count)+":  身份证号:"+i[0]+" 姓名:"+i[1]+" 性别:"+i[2]+" 电话:"+i[3]+" 订单号:"+i[4]+" 车次号:"+i[6]+" 订单时间:"+i[8]+" 订票数:"+i[9]+" 总价:"+i[10]+" 订票渠道:"+i[12]+"\n")
        count+=1
    return render_template('search.html',back = string)
@app.route("/userUnbyinfo_search/",methods=['POST'])
def UserUnbyinfo():
    arr = get_sql("SELECT * FROM userinfo LEFT JOIN dingpiaoinfo ON userinfo.`Userid`=dingpiaoinfo.`Userid` RIGHT JOIN tuipiao ON dingpiaoinfo.`Dingdanid`=tuipiao.`Dingdanid`")
    string = ""
    count = 1
    for i in arr:
        string+=(str(count)+":  身份证号:"+i[0]+" 姓名:"+i[1]+" 性别:"+i[2]+" 电话:"+i[3]+" 订单号:"+i[4]+" 车次号:"+i[6]+" 订单时间:"+i[8]+" 订票数:"+i[9]+" 总价:"+i[10]+" 订票渠道:"+i[12]+"\n")
        count+=1
    return render_template('search.html',back = string)
app.run()

