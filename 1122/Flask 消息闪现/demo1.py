"""
Flask 消息闪现
一个好的基于GUI的应用程序会向用户提供有关交互的反馈。例如，桌面应用程序使用对话框或消息框，JavaScript使用警报用于类似目的。

在Flask Web应用程序中生成这样的信息性消息很容易。Flask框架的闪现系统可以在一个视图中创建消息，并在名为next的视图函数中呈现它。

Flask模块包含flash()方法。它将消息传递给下一个请求，该请求通常是一个模板。

flash(message, category)
    message参数是要闪现的实际消息。
    category参数是可选的。它可以是“error”，“info”或“warning”。

为了从会话中删除消息，模板调用get_flashed_messages()。
    get_flashed_messages(with_categories, category_filter)


"""