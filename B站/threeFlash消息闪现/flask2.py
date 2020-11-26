from flask import Flask,flash,get_flashed_messages

app =  Flask(__name__)
app.debug = True
app.secret_key = 'flask'


@app.route('/page1')
def page1():
    # 存放数据到flash中 , 且info1,info2,info3归属于info这一类，error01归属于error这一类
    flash('info1','info')
    flash('info2','info')
    flash('info3','info')
    flash('error1','error')
    return 'success'


@app.route('/page2')
def page2():
    # 使用get_flashed_messages方法取出flash中的数据, 且只取info类的数据
    print(get_flashed_messages(category_filter = 'info'))
    return 'success'


if __name__ == '__main__':
    app.run()