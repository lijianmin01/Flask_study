from flask import Flask,flash,get_flashed_messages

app =  Flask(__name__)
app.debug = True
app.secret_key = 'flask'

@app.route('/page1')
def page1():
    # 存放数据到flash中
    flash('flash中存放的临时数据，get_flashed_messages方法取一次就没有了')
    return 'success'


@app.route('/page2')
def page2():
    # 使用get_flashed_messages方法取出flash中的数据
    print(get_flashed_messages())
    return 'success'


if __name__ == '__main__':
    app.run()