from behave import given, when, then


@given('Round time is show')
def is_displayed_time_page(context):
    context.app.time_page.open()


@when('Tap start button')
def tap_start(context):
    context.app.time_page.tap_start()


@when('Tap stop button')
def tap_stop(context):
    context.app.time_page.tap_stop()


@then('Time should be started')
def time_should_be_started(context):
    context.app.time_page.time_started()


@then('Time should be stopped')
def time_should_be_stopped(context):
    context.app.time_page.time_stopped()
