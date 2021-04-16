from behave import given, when, then


@given('Round time is show')
def is_displayed_time_page(context):
    context.app.time_screen.open()


@when('Tap start button')
def tap_start(context):
    context.app.time_screen.tap_start()


@when('Tap stop button')
def tap_stop(context):
    context.app.time_screen.tap_stop()


@when('Tab reset button')
def tap_reset(context):
    context.app.time_screen.tap_reset()


@then('Time should be started')
def time_should_be_started(context):
    context.app.time_screen.time_started()


@then('Time should be stopped')
def time_should_be_stopped(context):
    context.app.time_screen.time_stopped()


@then('Reset icon is displayed')
def is_displayed_reset_button(context):
    context.app.time_screen.is_displayed_reset()


@then('Favorites icon is displayed')
def is_displayed_favorites_button(context):
    context.app.time_screen.is_displayed_favorites()


@then('Settings icon is displayed')
def is_displayed_settings_button(context):
    context.app.time_screen.is_displayed_settings()


@then('Time is reset')
def time_should_be_reset(context):
    context.app.time_screen.time_should_be_reset()
